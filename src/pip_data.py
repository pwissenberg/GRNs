import argparse
import requests
import pandas as pd
import numpy as np

#Reduces the size of the memory
def downcast_dtypes(df):
    _start = df.memory_usage(deep=True).sum() / 1024 ** 2
    float_cols = [c for c in df if df[c].dtype == 'float64']
    int_cols = [c for c in df if df[c].dtype in ['int64','int32']]
    df[float_cols] = df[float_cols].astype(np.float32)
    df[int_cols] = df[int_cols].astype(np.int32)
    _end = df.memory_usage(deep=True).sum() / 1024 ** 2
    saved = (_start - _end) / _start * 100
    print(f"Saved {saved:.2f}%")
    return df

# Loads all datasets
def get_all_dfs(list_of_filenames:[]):
    data_frames = []
    for file in list_of_filenames:
        data = pd.read_csv(file, sep='\t', header=None, usecols=[0,1])
        #data = data[['TF','gene']].copy()
        data = downcast_dtypes(data)
        data_frames.append(data)
    return data_frames

#Creating the union of all the datasets
def create_union(list: []):
    return pd.concat(list)

#Downloading all the data sets
def download_datasets(file_path: str):
    names_of_datasets = []
    with open(input_file_path, 'r') as read:
        for index, line in enumerate(read):
            link = line.replace('\n', '')
            name = str(link).split(sep='/')[-1]
            names_of_datasets.append(name)
            print(link)
            print(str(name).split(sep='/')[-1])

            with requests.get(link) as rq:
                with open('../data/' + name, "wb") as file:
                    file.write(rq.content)
    return names_of_datasets

#Write final data set
def write_file(dataframe, output_file):
    dataframe.to_csv('GRN_nodes_all_nodes', sep='\t', index=False, header=False)

parser = argparse.ArgumentParser(description="Gets as input an txt-File and downloads the corresponding Files")
parser.add_argument('-in','--input', type=str, help='Path to the file with the links.')
parser.add_argument('-out','--output', type=str, help='Path to the final GRN')
args = parser.parse_args()
input_file_path = args.input
output_path = args.output

dataset_file_names = download_datasets(input_file_path)
df_sets = get_all_dfs(dataset_file_names)
final_data_set = create_union(df_sets)
final_data_set.drop_duplicates(keep='first', inplace=True)
write_file(final_data_set, output_path)

