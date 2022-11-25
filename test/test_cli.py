import unittest
from typer.testing import CliRunner


from src.cli import app

runner = CliRunner()

class TestCli(unittest.TestCase):
    runner = CliRunner()

    def test_download(self):
        '''
        Testing the download functionality of the cli command
        '''
        self.runner.invoke(app, ['download','test_download_datasets.txt'])

    def test_format(self):
        self.runner.invoke(app, ['format', 'test_format_grndb.txt', 'grndb'])
