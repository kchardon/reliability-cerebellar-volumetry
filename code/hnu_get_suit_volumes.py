#!/usr/bin/env python3

"""
Created on 14/02/2025 by Katia Chardon
"""

import sys
from nilearn.maskers import NiftiLabelsMasker
import pandas as pd

#==============================================================================
#==============================================================================
# run by hnu_SUIT.sh

# Get a CSV file with the lobules volumes given an atlas and a subject file
# The atlas is the final atlas placed in the subject space and multiplied by the binarized subject file
# The subject file is the original output from SUIT
#==============================================================================
#==============================================================================


#==============================================================================
# Function to get the CSV file
#==============================================================================

def process_images(atlas_path, subject_path, output_path):
    """Extract time series from the subject image using the atlas."""

    # Masker with the atlas
    masker = NiftiLabelsMasker(
        labels_img=atlas_path,
        verbose=5,
    )

    # Extraction of temporal series
    time_series = masker.fit_transform(subject_path)

    # DataFrame of temporal series
    df = pd.DataFrame(time_series)
    df.to_csv(output_path, index=False)

    print(f"Output saved to {output_path}")

#==============================================================================
# Main function that calls the CSV function on the given  files
#==============================================================================

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: process_atlas.py <atlas_path> <subject_path> <output_path>")
        print("The atlas is the final atlas placed in the subject space and multiplied by the binarized subject file")
        print("The subject file is the original output from SUIT")
        sys.exit(1)

    atlas_path = sys.argv[1]
    subject_path = sys.argv[2]
    output_path = sys.argv[3]

    process_images(atlas_path, subject_path, output_path)
