import unittest
from typer.testing import CliRunner


from cli import app

runner = CliRunner()

class TestCli(unittest.TestCase):
    runner = CliRunner()

    def test_download(self):
        '''
        Testing the download functionality of the cli command
        '''

        result = self.runner.invoke(app, ['download','test_download_datasets.txt'])
        assert result.exit_code == 0

    def test_format(self):
        '''
        Testing if the cli command format works
        '''

        result = self.runner.invoke(app, ['format', 'test_format_grndb.txt', 'grndb'])
        assert result.exit_code == 0