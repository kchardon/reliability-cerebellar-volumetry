#!/bin/bash

#==============================================================================
#==============================================================================
# Created on 08/09/2025 by Katia Chardon

# Process SUIT outputs of HNU to get the volumes of each lobule

# Here is the organization of the folders. 
# Don't hesitate to modify the code to match yours.

# The source_data should be organized by sessions and then by subjects
# The Suit folder is named "SuitX" with X being the number of the session,
# except for session 1 which is just named "Suit"
# source_data
# |_ Suit
#    |_ sub-XX
# |_ Suit2
#    |_ sub-XX
#
# code is where you have the hnu_get_suit_volumes.py file
# env is the folder of the python environment
#
# You will obtain in dest_data, this organisation
# dest_data
# |_ sub-XX
#    |_ ses-XX
# with all the intermediate files and the final sub-XX_ses-XX_volumes.csv
#==============================================================================
#==============================================================================
echo "Process SUIT outputs -------"

# Variables

code=reliability-cerebellar-volumetry/code
env=reliability-cerebellar-volumetry/.reliability
dest_data=reliability-cerebellar-volumetry/outputs/suit
source_data=HNU/derivatives

mkdir $dest_data

# Process data

for ses in {1..10}; do
    # Format session number as two digits
    ses_str=$(printf "%02d" $ses)
    echo Session $ses_str
    
    # Folder in source
    if [ "$ses" -eq 1 ]; then
        suit_folder=${source_data}/Suit
    else
        suit_folder=${source_data}/Suit${ses}
    fi

    # For each subject
    for sub_folder in "$suit_folder"/sub*; do
        # Subject name
        sub=$(basename "$sub_folder")
        echo Subject $sub

        # SUIT output
        filename="wd${sub}_ses-${ses_str}_T1w_n4_mni_seg1.nii"
        filepath="${sub_folder}/${filename}"

        # Output folder for the subject and the session
        sub_output=$dest_data/$sub/ses-$ses_str
        mkdir -p $sub_output

        # We correct the NaN if there are some
        corr_out=$sub_output/${filename%.nii}_corr.nii.gz
        fslmaths $filepath -nan $corr_out

        # Atlas to subject space
        atlas_out=$sub_output/atlas.nii.gz
        flirt -in $source_data/Lobules-SUIT.nii -ref $corr_out -out $atlas_out

        # Binarize subject image
        bin_out=$sub_output/${filename%.nii}_bin.nii.gz
        fslmaths $corr_out -bin $bin_out

        # Atlas x bin
        final=$sub_output/final_atlas.nii.gz
        fslmaths $atlas_out -mul $bin_out $final

        # Extract volumes
        source $env/bin/activate
        python3 $code/hnu_get_suit_volumes.py $final $filepath $sub_output/${sub}_ses-${ses_str}_volumes.csv

    done
done

echo "END"