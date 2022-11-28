# The GRN-Pipeline
This project is about **downloading**, **parsing** and **combining** different **Gene Regulatory Networks(GRN)** or 
**Gene Interaction Networks** from three different public availbale-databases for GRNs. Is uses the following databases:
- [GRNdb](http://www.grndb.com/)
- [Gene Regulatory Network Database](https://grand.networkmedicine.org/)
- [HumanBase](https://hb.flatironinstitute.org/download)

## Motivation
In another coding project at our [research group](https://biomedical-big-data.de/) at the TUM, we were investigating how 
to build more meaningful SNP-SNP interaction models. In the need to find other information sources to improve the 
accuracy of th SNP-SNP-interaction predicting model. I have build a data-pipeline to download predicted GRNs from the
mentioned databases. Due to some missing APIs, I needed to web-scrape all the needed single URLs and then parse them in
the right format to feed the SNP-SNP interaction model. Another idea was to build a **"general" GRN** to construct a 
baseline.

## Installation/Setup
Use the package manager [pip3](https://docs.python.org/3/installing/index.html) to install the packages.
Programming Language :: Python :: 3.9

```bash
#Recommendation: Use a local environment and ensure that the local environment is actived
python3 -m venv venv
source env/bin/activate

pip3 install --upgrade cython
pip3 install -r requirements.txt
```
## Examples
These examples are to demonstrate the pipeline directly from the terminal. Therefore, I provided short constructed input 
files. If you want to download all the GRNs and conduct transformation and analysis, please use the files in the 
resource folder, which contain all the scrapped links to the datasets. 
```bash
#Download to two GRNS


#Formatting of the GRNs


#Concatenating of the GRNs


# Complete data pipeline from Download to Concatenating

#Visualizing the data

```

## Usage 
Downloading the GRNs from the specific databases and transform the data sets to the right format for the SNP-SNP-interaction 
project.
### Downloading the specifc Dataset or GRNs
```bash
#Runs the script with an input-file which contains all of the links
python3 cli.py download <input_file> <output_folder>
```
- **input_file**: defines the path to the input file. The file contains per line one link to a file/dataset/GRN
- **out_folder**: optional argument to provide a path to store the dowloaded datasets
### Formatting the downloaded Dataset
In the following step, the downloaded GRNs are parsed in the right format. Due to inconsistent use of different IDs at 
the databases. I used the [biodbnet-API](https://biodbnet-abcc.ncifcrf.gov/) to map all different IDs for Genes to their 
Gene Symbol and omitted every other information of the datasets. Due to the lack of scale at the API, every big request 
needed tp be batched. In addition, in the GRAND-database, the GRNs were only provided in the adjacency format, so they
needed a special parsing.
```bash
#Conversion from one ID to another
python3 cli.py format <input_file> <input_db> <output_folder>
```
- **input_file**: every line in the file should store a file-path to a dataset
- **input_db**: defines the name of database to tell the program the input dataset format **!!!Please use only the 
following arguments for the respective database:'grndb', 'grand', 'humanbase'!!!**
- **output_folder**: defines an optional path if the formatted datasets should be stored in the working directory
### Build Union of Datasets
To build a "general GRN", I provided the functionality to build a union between several datasets. It is important that 
the datasets were formated before that step.
```bash
#Conversion from one ID to another
python3 cli.py union <input_file> <output_file>
```
- **input_file**: every line in the file should store a file-path to a 'formatted' dataset
- **output_file**: defines the name of the finished output_file
### Complete Pipeline
Conducts every single step sequentially.
```bash
#Conversion from one ID to another
python3 cli.py complete <input_file> <input_db> <output_folder>
```
- **input_file**: every line in the file should store a file-path to a 'formatted' dataset
- **input_db**: defines the name of database to tell the program the input dataset format **!!!Please use only the 
following arguments for the respective database:'grndb', 'grand', 'humanbase'!!!**
- **output_file**: defines the name of the finished output_file
### Visualize final GRN
A lot of networks in realty do not follow a normal distribution. This applies also to the degree GRN's degree 
distribution. Instead, if we are plotting the degree distribution of the nodes (genes) in a GRN, it should follow a 
power law distribution. So that is the reason why I build the visualization feature. The visualization feature enables
the possibility to plot the degree distribution of the nodes, the log-log-transformed degree distribution, and 
the summary-statistics feature. In the characteristics feature, I conducted a log-log-transformation and tested if
it fits an OLS regression.
```bash
#Conducts degree distribution
python3 cli.py visualize <input_file> plot

#Conducts log-log-transformed degree distribution
python3 cli.py visualize <input_file> log_plot

#Prints fitting characteristics
python3 cli.py visualize <input_file> fitting_summary
```
- **input_file**: it should be a file, which was formatted before this step
**!!!Only use plot, log_plot and fit_summary!!!**

## Example formatted File
All the output files should have the same format: **Headerline with TF & Gene, then gene represented by its ID \t next 
ID\n 
```
TF	Gene
ARID3A	ARID3A
ARID3A	PLA2G15
ARNT	RORA
.   
.
```
## Project-Structure
- data_pipline-🗂: this folder serves cache for all the single datasets, which were downloaded
- resources-🗂: contains already scrapped links to all the dataset from the three databases
- cli.py: contains the command line tool interface
- test -🗂: contains some tests
## Tasks
* [x] Downloading files
* [x] Concatenating all datasets
* [x] Works with [GRNdb](http://www.grndb.com/), [HumanBase](https://hb.flatironinstitute.org/download) & GRAND
* [x] Mapping between HGNC_ID, Ensemble and GeneSymbols
* [x] EntrezID is missing in the mapping part
* [x] Optimization for large amount of data
* [x] Works with adjacency matrices
* [ ] **Extension for Mapping**: At the moment it only executes API calls to biodbnet, you could extend it, if outliers occur that it could be checked in the [genenames-database](https://www.genenames.org/tools/multi-symbol-checker/)

### Contact
If you have any questions pls, do not hesitate to contact me! :)
<!-- Tables -->
| Name              | Email                                                   |
|-------------------|---------------------------------------------------------|
| Paul Wissenberg   | [paul.wissenberg@tum.de](mailto:paul.wissenberg@tum.de) |