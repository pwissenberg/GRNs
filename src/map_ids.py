import requests
import pandas as pd
import argparse

ensemble = 'EnsemblGeneId&taxonId=9606'
ids = ['genesymbol', 'hgncid', 'ensemble']

def get_right_json_parameter(id):
    if id == ensemble:
       return 'Ensembl Gene ID'
    elif id == 'hgncid':
        return 'HGNC ID'
    elif id == 'genesymbol':
        return 'Gene Symbol'


def send_request(input_string, input_ids, output_ids):
    response = requests.get(
        url=f"https://biodbnet.abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.json?method=db2db&input={input_ids}&inputValues={input_string}&outputs={output_ids}&format=col")
    print(f"https://biodbnet.abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.json?method=db2db&input={input_ids}&inputValues={input_string}&outputs={output_ids}&format=col")

    gene_ensemble_list = response.json()[0][get_right_json_parameter(input_ids)]
    list_response = response.json()[1][get_right_json_parameter(output_ids)]
    if len(gene_ensemble_list) == len(list_response):
        print(list_response)
        return list_response
    else:
        print('Mistake, some of the ids could not be matched!!')

#Portins teh size of input to meet the constraints of the database
def portion(input_values, input_ids, output_ids):
    final_list = []
    interations = int(len(input_values)/850)
    residues = len(input_values)-interations*850

    while len(input_values)>850:
        input_string = ','.join(input_values[:850])
        del(input_values[:850])
        print(len(input_values))
        final_list.extend(send_request(input_string,input_ids,output_ids))
    #for the residues
    if residues > 0:
        input_string = ','.join(input_values[:residues])
        final_list.extend(send_request(input_string,input_ids,output_ids))
    print(len(final_list))
    return final_list

# Read in input file
parser = argparse.ArgumentParser(description="Gets as input an txt-File and converts it to the asked ID")
parser.add_argument("-in", "--input_id", type=str ,help="ID in the input", required=True)
parser.add_argument("-out", "--output_id", type=str ,help="ID in the output", required=True)
parser.add_argument("-infile", "--input_file", type=str,help="txt-File containing the input data", required=True)
parser.add_argument("-outfile", "--output_file", type=str,help="txt-File containing the output data", required=True)

args = parser.parse_args()
input_id = args.input_id
output_id = args.output_id

if not(input_id in ids) or not(output_id in ids):
    print('Please use for --input or -out the right arguments. See also in the README.md')

input_file = args.input_file
output_file = args.output_file
if(input_id == 'ensemble'):
    input_id = ensemble
if(output_id == 'ensemble'):
    output_id = ensemble

#Get first input columns
df = pd.read_csv(input_file, sep='\t')
data = df.iloc[:,0].to_list()


df['TF_mapped'] = portion(data,input_id,output_id)
#Get second input columns
data = df.iloc[:,1].to_list()
df['gene_mapped'] = portion(data,input_id,output_id)
df = df[['TF_mapped','gene_mapped']].copy()
df.rename(columns={"TF_mapped": "TF"}, inplace=True)
df.rename(columns={"gene_mapped": "gene"}, inplace=True)

df.to_csv(output_file,sep='\t', columns=['TF','gene'], index=False)


