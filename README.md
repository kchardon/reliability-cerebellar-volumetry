# Reliability of Cerebellar Volumetry

This repository contains the data and code used for the publication *Towards Reliable Measurement of Cerebellar Morphology : A comparative assessment of segmentation pipelines* by Katia Chardon<sup>1,2</sup>, Ting Xu<sup>3</sup>, Marie Chupin<sup>4</sup>, Edouard Duchesnay<sup>1</sup>, Davide Boido<sup>1</sup> and Charles Laidi<sup>2,5</sup>.

These materials have been made available to promote reproducibility and open science. The Hangzhou Normal University open dataset (HNU) used in this publication is available through the Consortium for Reliability and Reproducibility [1].

<sup>1</sup> BAOBAB, NeuroSpin, CEA, Université Paris-Saclay, CNRS, Gif-sur-Yvette, France 
<sup>2</sup> Institut Mondor de Recherche Biomédicale (IMRB), INSERM, Université Paris-Est Créteil, Créteil, France 
<sup>3</sup> Child Mind Institute, New York, NY, USA 
<sup>4</sup> CATI, NeuroSpin, CEA, Université Paris-Saclay, Gif-sur-Yvette, France 
<sup>5</sup> UNIACT, NeuroSpin, CEA, Université Paris-Saclay, Gif-sur-Yvette, France

## Abstract

**Background.** Characterizing cerebellar morphology is fundamental for accurately mapping its structure and function across individuals, yet remains challenging due to its densely foliated architecture. Although multiple automated segmentation pipelines exist, the measurement reproducibility of these tools has not been benchmarked. **Methods.** We conducted a systematic assessment of robustness for cerebellar morphology estimates using four commonly used pipelines: one classic parcellation method (CERES), two deep-learning methods (ACAPULCO, DeepCERES), and one voxel-based morphometry toolbox (SUIT). Leveraging the HNU test-retest dataset, which provides MRI scans for ten timepoints per individual over a month, we evaluated the test-retest reliability for each of four pipelines using ReX, an integrative tool for quantifying and optimizing measurement reliability and individual differences. We quantified intra- and inter-individual variability, as well as the Intraclass Correlation Coefficient (ICC), for each pipeline at both global and region-of-interest levels. **Results.** Overall, all pipelines yielded highly reliable segmentation volumes (ICC > 0.8). Across pipelines, DeepCERES demonstrated the strongest performance, exhibiting high inter-individual consistency and low intra-individual variability. Importantly, our analysis highlighted substantial heterogeneity in reliability across lobules for each method. Lobule X consistently showed reduced reliability whereas lobules I-V were reliably estimated across all pipelines. **Conclusion.** Our work evaluated the robustness of cerebellar segmentation pipelines. While DeepCERES offers a robust global performance, substantial lobule-specific variability underscores the need for reliability-aware pipeline selection to optimize morphology estimation in research.

## Data

The `data` folder contains the following files:

- `subjects.csv`: List of all subjects used.
- `all_volumes_cm3_METHOD.csv`: Volumes outputs from each method.
- `all_volumes_cm3_METHOD_scaled.csv`: Scaled volumes outputs from each method.
- `METHOD_all_lobules_ICC.csv`: Intraclass correlation coefficients (ICC), Between Variation and Within Variation computed with ReX [2] from the scaled volumes.

For the analysis computed using all subjects with no failures for each method (except SUIT), the volumes and ICC files have the same name with `_ALLGOODDATA` at the end. Additionally, the subjects files for each method are named `subjects_METHOD.csv`.

## Code

The `code` folder contains the following scripts and notebooks:

- `process_SUIT.sh`: Shell script to get the volumes data from the SUIT outputs.
- `hnu_get_suit_volumes.py`: Python script called by `process_SUIT.sh` to process SUIT data.
- `data_prep.ipynb`: Jupyter notebook to prepare the volumes data for ICC computation with ReX.
- `analysis.ipynb`: Jupyter notebook for statistics and plots.

The notebooks also exist with `_ALLGOODDATA` at the end for analysis using all subjects with no failures.

## Requirements

To run the code in this repository, you will need the following dependencies:

- Bash (for running shell scripts)
- Python 3 with the required libraries listed in `requirements.txt`
- Jupyter Notebook

## Reproducing the Analysis

To run the same analysis, follow these steps:

1. Obtain the HNU data.
2. Run SUIT [3], CERES [4], ACAPULCO [5], and DeepCERES [6] on the data.
3. Change the path in each code file to match your directory structure.
4. Run `process_SUIT.sh` to get the final SUIT data.
5. Use `data_prep.ipynb` to prepare the volumes data for ICC computation with ReX.
6. Use ReX to compute ICC, Between Variation and Within Variation (containerized or online, with the model named two-way random in ReX).
7. Use `analysis.ipynb` to generate the final results and plots.

## License

This repository is licensed under the [MIT License](LICENSE.md). By using, distributing, or modifying this software and data, you agree to the terms and conditions outlined in the license.

## References

[1] Zuo XN, Anderson JS, Bellec P, Birn RM, Biswal BB, Blautzik J, et al. An open science resource for establishing reliability and reproducibility in functional connectomics. Sci Data. 2014 Dec 9;1(1). Available from: http://dx.doi.org/10.1038/sdata.2014.49

[2] Xu T, Kiar G, Cho JW, Bridgeford EW, Nikolaidis A, Vogelstein JT, et al. ReX: an integrative tool for quantifying and optimizing measurement reliability for the study of individual differences. Nat Methods. 2023 June 1;20(7):1025–8. Available from: http://dx.doi.org/10.1038/s41592-023-01901-3

[3] Diedrichsen J. A spatially unbiased atlas template of the human cerebellum. NeuroImage. 2006 Oct;33(1):127–38. Available from: http://dx.doi.org/10.1016/j.neuroimage.2006.05.056

[4] Romero JE, Coupé P, Giraud R, Ta VT, Fonov V, Park MTM, et al. CERES: A new cerebellum lobule segmentation method. NeuroImage. 2017 Feb;147:916–24. Available from: http://dx.doi.org/10.1016/j.neuroimage.2016.11.003

[5] Han S, Carass A, He Y, Prince JL. Automatic cerebellum anatomical parcellation using U-Net with locally constrained optimization. NeuroImage. 2020 Sept;218:116819. Available from: http://dx.doi.org/10.1016/j.neuroimage.2020.116819

[6] Morell-Ortega S, Ruiz-Perez M, Gadea M, Vivo-Hernando R, Rubio G, Aparici F, et al. DeepCERES: A deep learning method for cerebellar lobule segmentation using ultra-high resolution multimodal MRI. NeuroImage. 2025 Mar;308:121063. Available from: http://dx.doi.org/10.1016/j.neuroimage.2025.121063