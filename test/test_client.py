import unittest
from src.client import Client
import pathlib as pl
import os

class TestClient(unittest.TestCase):

    client = Client()

    def assert_is_file(self, path):
        '''Checks if a file exists'''
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_download_dataset(self):
        '''Tests if download and renaming of the dataset-file works'''

        test_url = 'https://fastest.fish/lib/downloads/1KB.bin'
        self.client.download_dataset_from_url(test_url, './', 'test.bin')
        self.assert_is_file('./test.bin')
        os.remove('./test.bin')

    def test_download_dataset_from_file(self):
        '''Tests if the download of multiple files works'''
        dataset_names = self.client.download_datasets_from_file('test_multiple_files_download')
        self.assertListEqual(dataset_names, ['1KB.bin', '1KiB.bin'])
        os.remove('1KB.bin')
        os.remove('1KiB.bin')

    def test_mapping_of_ids(self):
        '''Checks if the mapping of the IDs work properly'''
        #Testing Ensemble to genesymbol mapping and vice versa
        converted_ids_list = self.client.mapping_of_the_ids('ENSG00000000938,ENSG00000001084','EnsemblGeneId&taxonId=9606', 'genesymbol')
        self.assertListEqual(converted_ids_list, ['FGR','GCLC'])
        converted_ids_list = self.client.mapping_of_the_ids('FGR,GCLC','genesymbol','EnsemblGeneId&taxonId=9606')
        self.assertListEqual(converted_ids_list, ['ENSG00000000938', 'ENSG00000001084'])

        #Testing hgncid to genesymbol and vice versa
        converted_ids_list = self.client.mapping_of_the_ids('HGNC:3031,HGNC:700','hgncid', 'genesymbol')
        self.assertListEqual(converted_ids_list, ['ARID3A','ARNT'])
        converted_ids_list = self.client.mapping_of_the_ids('ARID3A,ARNT', 'genesymbol', 'hgncid')
        self.assertListEqual(converted_ids_list,['HGNC:3031','HGNC:700'])


    def test_batch_processing_requests(self):
        '''Tests if the batch_processing_requests works properly by
        using an input list above the threshhold of the server'''

        input_hgncid =['HGNC:3031' for _ in range(1, 750)]
        input_hgncid.extend(['HGNC:700' for _ in range(1,50)])
        result_list = self.client.batch_processing_requests(input_hgncid, 'hgncid', 'genesymbol')
        solution_list = ['ARID3A' for _ in range(1,750)]
        solution_list.extend(['ARNT' for _ in range(1,50)])
        self.assertListEqual(result_list, solution_list)

if __name__ == '__main__':
    unittest.main()