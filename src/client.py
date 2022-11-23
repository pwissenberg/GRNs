import requests
import logging

BATCH_SIZE = 650

logging.basicConfig(
    level=logging.CRITICAL,
    format='{asctime} {levelname:<8} {message}',
    style='{',
    filename='log.log',
    filemode='w'
)

class Client(object):

    def __init__(self):
        pass

    def download_dataset(self, url: str, output_path: str, filename: str):
        '''Downloads a single dataset from a specifc url.
        :param str url: Specified dataset url
        :param str output_path: Specified location for the output file
        :param str filename: Defines the name of the output file
        '''

        with requests.get(url) as req:
            with open(output_path + filename, 'wb') as f:
                f.write(req.content)

    def download_datasets_from_file(self, file_input_path: str, file_output_path: str = './'):
        '''The function gets as input a file with different data sets and downloads all the files

        :param str file_input_path: Defines the input file. The file stores all of the different links(one per line).
        :param str file_output_path: Defines the output path. If it is not specified, it is stored in the working
        directory
        :return list: Returns a list of all the different file names
        '''

        names_of_datasets = []
        with open(file_input_path, 'r') as read:
            for index, line in enumerate(read):
                link = line.replace('\n', '')
                name = str(link).split(sep='/')[-1]
                names_of_datasets.append(name)
                self.print_progress_of_download(name, link)
                self.download_dataset(link, file_output_path, name)
        return names_of_datasets

    def print_progress_of_download(self ,file_name: str, url: str):
        '''Prints the progress of the download.

        :param str file_name: The name of the file.
        :param str url: The URL of the downloaded data set.
        '''

        print('_______________________________________________________________________________________________________')
        print('Download of following dataset: ', file_name)
        print(url)

    def mapping_of_the_ids(self,input_id_list: str,type_input_id: str, type_output_id: str):
        '''Maps the different GeneIDs from one database to another database.

        :param str input_id_list: a string seperating the ids by comma. e.g. <geneId>,<geneId>,...,<geneId>
        :param str type_input_id: defines the type of the input ids
        :param str type_output_id: defines the type of the output ids
        :return list: returns a list of the requested output ids
        '''
        link = f"https://biodbnet.abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.json?method=db2db&input=" \
               f"{type_input_id}&inputValues={input_id_list}&outputs={type_output_id}&format=col"
        try:
            response = requests.get(url=link).json()
            #Input
            input_ids_list = response[0].get(self.get_right_json_parameter(type_input_id))#.get(self.get_right_json_parameter(type_output_id))
            #requested output
            output_ids_list = response[1].get(self.get_right_json_parameter(type_output_id))
            # Write response to the logger
            logging.info('Following link worked:')
            logging.info(link)
            return output_ids_list
        except Exception as e:
            logging.critical('REQUEST FAILED WITH FOLLOWING LINK')
            logging.critical(link)
            logging.critical('REQUEST FAILED WITH FOLLOWING EXCEPTION')
            logging.critical(e)

    def batch_processing_requests(self, input_values: list, type_input_id: str, type_output_id: str):
        '''Unfortunately the server cannnot process all of the ids at once (lenth of url) and does not provide a
        body property so. The ids need to be splitted in batches.If tested a little bit and 650 ids worked.

        :param list input_values: list of input ids, which need to be mapped
        :param str type_input_id: given id type of the input
        :param str type_output_id: id type of the output
        :return list: complete list of all mapped output ids
        '''
        final_list = []
        iterations = int(len(input_values) / BATCH_SIZE)
        residues = len(input_values) - iterations * BATCH_SIZE
        while len(input_values) >= BATCH_SIZE:
            input_string = ','.join(input_values[:BATCH_SIZE])
            del (input_values[:BATCH_SIZE])
            final_list.extend(self.mapping_of_the_ids(input_string, type_input_id, type_output_id))
        # for the residues
        if residues > 0:
            input_string = ','.join(input_values[:residues])
            final_list.extend(self.mapping_of_the_ids(input_string, type_input_id, type_output_id))
        return final_list

    def get_right_json_parameter(self, id_type: str):
        '''To access the server response

        :param str id_type: Give the right Parameter to acces the data in the json object.
        :return str: The right attribute
        '''

        if id_type == 'EnsemblGeneId&taxonId=9606':
            return 'Ensembl Gene ID'
        elif id_type == 'hgncid':
            return 'HGNC ID'
        elif id_type == 'genesymbol':
            return 'Gene Symbol'
        elif id_type == 'geneid':
            return 'Gene ID'

