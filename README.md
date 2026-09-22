# Reliability of Cerebellar Volumetry

This repository contains the data and code used for the publication *Towards Reliable Measurement of Cerebellar Morphology : A comparative assessment of segmentation pipelines* by Katia Chardon<sup>1,2</sup>, Marie Chupin<sup>3</sup>, Ting Xu<sup>4</sup>, Edouard Duchesnay<sup>1</sup>, Davide Boido<sup>1</sup> and Charles Laidi<sup>2,5</sup>.

These materials have been made available to promote reproducibility and open science. The Hangzhou Normal University open dataset (HNU) used in this publication is available through the Consortium for Reliability and Reproducibility (https://fcon_1000.projects.nitrc.org/indi/CoRR/html/hnu_1.html) [1].

<sup>1</sup> BAOBAB, NeuroSpin, CEA, Université Paris-Saclay, CNRS, Gif-sur-Yvette, France
<sup>2</sup> Institut Mondor de Recherche Biomédicale (IMRB), INSERM, Université Paris-Est Créteil, Créteil, France
<sup>3</sup> Centre d'acquisition et de traitement des images (CATI), US52-UAR2031, CEA, ICM, Sorbonne Université, CNRS, INSERM, AP-HP, Ile-de-France, France
<sup>4</sup> Child Mind Institute, New York, NY, USA
<sup>5</sup> UNIACT, NeuroSpin, CEA, Université Paris-Saclay, Gif-sur-Yvette, France

## Abstract

**Background.** Characterizing cerebellar morphology is fundamental for accurately mapping its structure and function across individuals, yet remains challenging due to its densely foliated architecture. Although multiple automated segmentation pipelines exist, the measurement reproducibility of these tools has not been comprehensively benchmarked. **Methods.** We conducted a systematic assessment of reliability for cerebellar morphology estimates using four commonly used pipelines: one classic parcellation method (CERES), two deep-learning methods (ACAPULCO, DeepCERES), and one voxel-based morphometry toolbox (SUIT). Leveraging the HNU dataset, which provides MRI scans for ten timepoints per individual over a month, we evaluated the test-retest reliability for each of the four pipelines using ReX, an integrative tool for quantifying and optimizing measurement reliability and individual differences. We quantified intra- and inter-individual variability, as well as the Intraclass Correlation Coefficient (ICC), for each pipeline at both global and region-of-interest levels. We used two pools of data: a common dataset of 12 subjects x 5 sessions to benchmark all the pipelines, and method-specific datasets including pools of subjects with 5 valid sessions for each pipeline to assess the generalizability of our findings. **Results.** Overall, all pipelines yielded highly reliable segmentation volumes (ICC > 0.87). DeepCERES demonstrated the most consistent performance across all metrics and subject pools, while SUIT achieved the highest ICC on the common dataset but showed decreased reliability when evaluated on a larger subject pool. Importantly, our analysis highlighted substantial heterogeneity in reliability across lobules for each method. Lobule X consistently showed reduced reliability whereas lobules I-V, VI, Crus I, IX, and VIIIB were reliably estimated across all pipelines. **Conclusion.** While all pipelines demonstrated strong reliability, DeepCERES showed the most robust and consistent performance overall. Substantial lobule-specific variability and method-dependent failure rates underscore the need for reliability-aware pipeline selection to optimize cerebellar morphology estimation in research.

## Data

The `data` folder contains the following files:

- `subjects.csv`: List of all subjects and sessions used.
- `METHOD_all_volumes_cm3.csv`: Volumes outputs from each method.
- `METHOD_all_volumes_cm3_scaled.csv`: Scaled volumes outputs from each method.
- `METHOD_all_lobules_ICC.csv`: Intraclass correlation coefficients (ICC), Between Variation and Within Variation computed with ReX [2] from the scaled volumes.

For the analysis computed using all subjects with no failures for each method, the volumes and ICC files have the same name with `_ALLGOODDATA` at the end. Additionally, the subjects files for each method are named `subjects_METHOD.csv`.

## Code

The `code` folder contains the following scripts and notebooks:

- `process_SUIT.sh`: Shell script to get the volumes data from the SUIT outputs.
- `hnu_get_suit_volumes.py`: Python script called by `process_SUIT.sh` to process SUIT data.
- `acapulco3_prepare_files.py` : Python script to prepare the ACAPULCO outputs.
- `data_prep.ipynb`: Jupyter notebook to prepare the volumes data for ICC computation with ReX.
- `analysis.ipynb`: Jupyter notebook for statistics and plots.

The notebooks also exist with `_ALLGOODDATA` at the end for analysis using all subjects with no failures.

## Requirements

To run the code in this repository, you will need the following dependencies:

- Bash (for running shell scripts)
- Python 3 with the required libraries listed in `requirements.txt`
- Jupyter Notebook

## Reproducing the Analysis

You can run only the analysis part using the already computed ICC files with `analysis.ipynb`.

To run entirely the same analysis, follow these steps:

1. Obtain the HNU data.
2. Run SUIT [3], CERES [4], ACAPULCO (ver. 0.2.0 and 0.3.0) [5], and DeepCERES [6] on the data.
3. Create the `outputs` folder in the repository.
4. Create a python environment with the libraries from `requirements.txt`. In the codes, the environment is named `.reliability` and is inside the repository.
5. Change the path in each code file to match your directory structure.
6. Run `process_SUIT.sh` to get the final SUIT data.
7. For ACAPULCO v0.3.0, run `acapulco3_prepare_files.py`.
8. For ACAPULCO v0.2.0, run the ENIGMA QC if you have access to it and put the `QC+vols` folders of each session in `outputs/acapulco2/ses-XX`. Otherwise, use `acapulco3_prepare_files.py` by changing the paths. Don't forget to also change the paths in `data_prep_ALLGOODDATA.ipynb`. In any case, put the outputs in `outputs/acapulco2`.
9. For CERES and DeepCERES, copy the output folders downloaded from their platform inside `outputs/ceres/output` and `outputs/deepCeres/output`. The folders and files should be named `sub-XX_ses-XX_T1w_jobXXXX_archive/report_jobXXXX.csv`.
10. Use `data_prep.ipynb` (and `data_prep_ALLGOODDATA.ipynb`) to prepare the volumes data for ICC computation with ReX. Change `save` to `True` to save the output files. They will be saved in `outputs/METHOD` as `METHOD_all_volumes_cm3.csv` and `METHOD_all_volumes_cm3_scaled.csv` (respectively as `METHOD_all_volumes_cm3_ALLGOODDATA.csv` and `METHOD_all_volumes_cm3_scaled_ALLGOODDATA.csv`).
11. Use ReX to compute ICC, Between Variation and Within Variation (containerized or online, with the model named two-way random in ReX).
12. Put the ReX outputs in `outputs` and name them `METHOD_all_lobules_ICC.csv` and `METHOD_all_lobules_ICC_ALLGOODDATA.csv`.
13. Use `analysis.ipynb` (and `analysis_ALLGOODDATA.ipynb`) to generate the final results and plots.

## License

- Code: MIT License ([`LICENSE`](LICENSE.md))
- Figures and CSV metrics: CC-BY-NC 4.0 ([`LICENSE-DATA`](LICENSE-DATA.md))

The figures and derived data are based on the HNU dataset from the Consortium for Reliability and Reproducibility (CoRR), accessed via INDI / NITRC. Consistent with the policies of the 1000 Functional Connectome Project, usage of the original data is unrestricted for non-commercial research purposes only. Original CoRR data are not redistributed in this repository.

## References

[1] Zuo XN, Anderson JS, Bellec P, Birn RM, Biswal BB, Blautzik J, et al. An open science resource for establishing reliability and reproducibility in functional connectomics. Sci Data. 2014 Dec 9;1(1). Available from: http://dx.doi.org/10.1038/sdata.2014.49

[2] Xu T, Kiar G, Cho JW, Bridgeford EW, Nikolaidis A, Vogelstein JT, et al. ReX: an integrative tool for quantifying and optimizing measurement reliability for the study of individual differences. Nat Methods. 2023 June 1;20(7):1025–8. Available from: http://dx.doi.org/10.1038/s41592-023-01901-3

[3] Diedrichsen J. A spatially unbiased atlas template of the human cerebellum. NeuroImage. 2006 Oct;33(1):127–38. Available from: http://dx.doi.org/10.1016/j.neuroimage.2006.05.056

[4] Romero JE, Coupé P, Giraud R, Ta VT, Fonov V, Park MTM, et al. CERES: A new cerebellum lobule segmentation method. NeuroImage. 2017 Feb;147:916–24. Available from: http://dx.doi.org/10.1016/j.neuroimage.2016.11.003

[5] Han S, Carass A, He Y, Prince JL. Automatic cerebellum anatomical parcellation using U-Net with locally constrained optimization. NeuroImage. 2020 Sept;218:116819. Available from: http://dx.doi.org/10.1016/j.neuroimage.2020.116819

[6] Morell-Ortega S, Ruiz-Perez M, Gadea M, Vivo-Hernando R, Rubio G, Aparici F, et al. DeepCERES: A deep learning method for cerebellar lobule segmentation using ultra-high resolution multimodal MRI. NeuroImage. 2025 Mar;308:121063. Available from: http://dx.doi.org/10.1016/j.neuroimage.2025.121063