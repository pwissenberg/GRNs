import requests
import logging

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
        '''
        link = f"https://biodbnet.abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.json?method=db2db&input=" \
               f"{type_input_id}&inputValues={input_id_list}&outputs={type_output_id}&format=col"
        try:
            response = requests.get(url=link)
            #Input
            test = response.json()[0]
            #requested output
            input_id_list = response.json()[1]#[0][self.get_right_json_parameter(type_input_id)]
            #test = response.json()
            list_response = response.json()[1][self.get_right_json_parameter(type_output_id)]
            # Write response to the logger
            logging.info(list_response)
            return list_response
        except:
            logging.critical('REQUEST FAILED WITH FOLLOWING LINK')
            logging.critical(link)

        def batch_processing_requests(self):
            '''Unfortunately the server cannnot process all of the ids at once (lenth of url) and does not provide a
            body property so. The ids need to be splitted in batches.If tested a little bit and 650 ids worked.'''
            pass

        def get_right_json_parameter(id: str):
            if id == 'EnsemblGeneId&taxonId=9606':
                return 'Ensembl Gene ID'
            elif id == 'hgncid':
                return 'HGNC ID'
            elif id == 'genesymbol':
                return 'Gene Symbol'
            elif id == 'geneid':
                return 'Gene ID'

