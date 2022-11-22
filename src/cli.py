import argparse

parser = argparse.ArgumentParser(description="Gets as input an txt-File and downloads the corresponding Files")

parser.add_argument('-in','--input', type=str, help='Path to the file with the links.')
parser.add_argument('-out','--output', type=str, help='Path to the final GRN')
args = parser.parse_args()
input_file_path = args.input
output_path = args.output
dataset_file_names = download_datasets(input_file_path)
df_sets = get_all_dfs(dataset_file_names)
final_data_set = create_union(df_sets)
write_file(final_data_set, output_path)