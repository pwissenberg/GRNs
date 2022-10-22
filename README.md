# NeEDL_GRN_data_pipeline
Data-preprocessing for the [GenEpiSeeker-project](https://github.com/biomedbigdata/genepiseeker_dev)
##Installation
Use the package manager [pip3](https://docs.python.org/3/installing/index.html) to install the packages.
```bash
pip3 install requests
pip3 install pandas
pip3 install argparse
pip3 install numpy
```
##Usage 
It downloads the GRNs from the specific databases and transform the data sets to the right format for the NeEDL project.
```bash
python3 pip_data.py -in ../resources/test -out final_GRN.txt
```
- **-in**: defines the path to the input file. The file contains per line one link to a file
- **-out**: defines the path of the final finished dataset
##Project-Structure
- data-🗂: this folder serves cache for all the single datasets
- resources-🗂: contains allready scrapped links to all the dataset from the databases
- src-🗂: contains all the code-snippets
##Tasks
* [x] Downloading files
* [x] Concatenating all datasets
* [x] Works with [GRNdb](http://www.grndb.com/) & [HumanBase](https://hb.flatironinstitute.org/download)
* [] Optimization for large amount of data
* [] Should work with adjacenc matrixe
###Contact
If you have any questions pls, do not hesitate to contact me! :)
<!-- Tables -->
| Name | Email                                                   |
| -----|---------------------------------------------------------|
|Paul Wissenberg | [paul.wissenberg@tum.de](mailto:paul.wissenberg@tum.de) |