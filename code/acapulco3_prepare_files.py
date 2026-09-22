#!/usr/bin/env python3

"""
Created on 14/02/2026 by Katia Chardon
"""

import os
import pandas as pd

#==============================================================================
#==============================================================================
# Prepare ACAPULCO's output files
# To be run before data_prep.ipynb

# Merge the different output files from ACAPULCO
# to get one file per session with all the subjects

# Here is the organization of the folders. 
# Don't hesitate to modify the code to match yours.

# The ACAPULCO_DIR should be organized by subjects and then by sessions
# ACAPULCO_DIR
# |_ sub-XX
#    |_ ses-XX
# 
# The FREESURFER_DIR should be organized by sessions and then by subjects
# FREESURFER_DIR
# |_ ses-XX
#    |_ sub-XX
#
# You will obtain the Cereb_vols_ses-XX.csv files in OUTPUT_DIR
#==============================================================================
#==============================================================================


#==============================================================================
# Set-up
#==============================================================================

ACAPULCO_DIR = "HNU/derivatives/acapulco3"
FREESURFER_OUTPUT = "HNU/derivatives/freesurfer"  
OUTPUT_DIR = "reliability-cerebellar-volumetry/outputs/acapulco3"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


CEREBEL_COLS = [
    "Corpus Medullare", "Left Crus I", "Left Crus II", "Left I-III",
    "Left IV", "Left IX", "Left V", "Left VI", "Left VIIB", "Left VIIIA",
    "Left VIIIB", "Left X", "Right Crus I", "Right Crus II", "Right I-III",
    "Right IX", "Right V", "Right VI", "Right VIIB", "Right VIIIA",
    "Right VIIIB", "Right X", "Rigt IV", "Vermis IX", "Vermis VI",
    "Vermis VII", "Vermis VIII", "Vermis X"
]

def col_to_dotname(name):
    """Convert 'Left Crus I' -> 'Left.Crus.I'"""
    return name.replace(" ", ".").replace("-", ".")

#==============================================================================
# Collect all data grouped by session
#==============================================================================

sessions = {}
for sub in sorted(os.listdir(ACAPULCO_DIR)):
    if not sub.startswith("sub-"):
        continue
    sub_path = os.path.join(ACAPULCO_DIR, sub)
    for ses in sorted(os.listdir(sub_path)):
        if not ses.startswith("ses-"):
            continue
        csv_path = os.path.join(sub_path, ses, "input_n4_mni_seg_post_volumes.csv")
        if not os.path.exists(csv_path):
            print(f"  [WARN] Missing: {csv_path}")
            continue
        # Skip empty files
        if os.path.getsize(csv_path) == 0:
            print(f"  [WARN] Empty file, skipping: {csv_path}")
            continue
        # Read the volumes file
        df = pd.read_csv(csv_path)
        # Skip if file has no usable content
        if df.empty or "name" not in df.columns:
            print(f"  [WARN] Unexpected format, skipping: {csv_path}")
            print(f"         Columns found: {df.columns.tolist()}")
            continue
        vol_dict = dict(zip(df["name"], df["volume"]))
        # Read eTIV from FreeSurfer aseg.stats
        etiv = None
        aseg_path = os.path.join(FREESURFER_OUTPUT, ses, sub, "stats", "aseg.stats")
        if os.path.exists(aseg_path):
            with open(aseg_path) as f:
                for line in f:
                    if line.startswith("# Measure EstimatedTotalIntraCranialVol"):
                        etiv = float(line.split(",")[3])
                        break
            if etiv is None:
                print(f"  [WARN] eTIV not found in {aseg_path}")
        else:
            print(f"  [WARN] aseg.stats not found: {aseg_path}")
        # Build the row
        row = {"ID": sub}
        row["Background"] = vol_dict.get("Background", None)
        for col in CEREBEL_COLS:
            row[col_to_dotname(col)] = vol_dict.get(col, None)
        row["Total_Cerebel_Vol"] = sum(
            vol_dict.get(col, 0) for col in CEREBEL_COLS
        )
        row["eTIV"] = etiv
        sessions.setdefault(ses, []).append(row)

#==============================================================================
# Write one CSV per session
#==============================================================================

for ses, rows in sessions.items():
    out_df = pd.DataFrame(rows)
    # Enforce column order
    ordered_cols = (
        ["ID", "Background"]
        + [col_to_dotname(c) for c in CEREBEL_COLS]
        + ["Total_Cerebel_Vol", "eTIV"]
    )
    out_df = out_df[ordered_cols]
    out_df.index = range(1, len(out_df) + 1)
    out_path = os.path.join(OUTPUT_DIR, f"Cerebel_vols_{ses}.csv")
    out_df.to_csv(out_path, index=True)
    print(f"[OK] Written: {out_path}  ({len(out_df)} subjects)")