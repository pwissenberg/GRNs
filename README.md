# NeEDL_GRN_data_pipeline
Data-preprocessing for the [GenEpiSeeker-project](https://github.com/biomedbigdata/genepiseeker_dev)

## Installation
Use the package manager [pip3](https://docs.python.org/3/installing/index.html) to install the packages.
```bash
pip3 install requests
pip3 install pandas
pip3 install argparse
pip3 install numpy
#Install everything with one line
pip3 install requests pandas argparse numpy
```
## Usage 
Downloading the GRNs from the specific databases and transform the data sets to the right format for the NeEDL project.
```bash
#Runs the script with an input-file which contains all of the links
python3 pip_data.py -in ../resources/test -out final_GRN.txt
```
- **-in**: defines the path to the input file. The file contains per line one link to a file
- **-out**: defines the path of the final finished dataset <br><br>
Mapping different IDs between the databases. In portions the size of IDs and executes several API calls to [biodbnet](https://biodbnet-abcc.ncifcrf.gov/)
```bash
#Conversion from one ID to another
python3 map_ids.py -in hgncid -out ensemble -infile ../output/test_hgnc.txt -outfile ../output/test_ensemble.txt
```
- **-in**: defines the ids from the input file
- **-out**: defines the ids from the output file
- **-infile**: defines the path of the input file
- **-outfile**: defines the path of the output file <br> <br>
**!!The conversion works only with the GeneSymbols, Ensemble and HGNC_ID!!! Please following identifier for the program call: genesymbol, hgncid, ensemble**
## Project-Structure
- data-🗂: this folder serves cache for all the single datasets, which were downloaded
- resources-🗂: contains allready scrapped links to all the dataset from the databases
- src-🗂: contains all the code-snippets
- output-🗂: stores the final GRNs
## Tasks
* [x] Downloading files
* [x] Concatenating all datasets
* [x] Works with [GRNdb](http://www.grndb.com/) & [HumanBase](https://hb.flatironinstitute.org/download)
* [x] Mapping between HGNC_ID, Ensemble and GeneSymbols
* [ ] EntrezID is missing in the mapping part
* [ ] Optimization for large amount of data
* [ ] Should work with adjacenc matrixe
* [ ] **Extension for Mapping**: At the moment it only executes API calls to biodbnet, you could extend it, if outliers occur that it could be checked in the [genenames-database](https://www.genenames.org/tools/multi-symbol-checker/)
### Contact
If you have any questions pls, do not hesitate to contact me! :)
<!-- Tables -->
| Name              | Email                                                   |
|-------------------|---------------------------------------------------------|
| Paul Wissenberg   | [paul.wissenberg@tum.de](mailto:paul.wissenberg@tum.de) |
| Mira Kreuzer      | [mira.kreuzer@tum.de](mailto:mira.kreuzer@tum.de) |
| Norman Roggendorf | [norman.roggendorf@tum.de](mailto:norman.roggendorf@tum.de) |
| Markus Hoffmann   | [markus.hoffman@tum.de](mailto:markus.hoffman@tum.de) |
|Christian Hoffmann   | [christian.hoffmann@tum.de](mailto:christian.hoffmann@tum.de) |