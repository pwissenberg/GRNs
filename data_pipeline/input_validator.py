import typer
from rich import print
import os
from .client import Client
from .parser import Parser
from .grand_parser import GrandParser
from .grndb_parser import GrndbParser
from .humanbase_parser import HumanBaseParser

DATA_BASES = ['grndb', 'grand', 'humanbase']
STATISTIC_OPERATIONS = ['log_plot', 'plot', 'fitting_summary']

class InputValidator(object):


    def check_existence_of_paths(self, paths: list[str]):
        '''
        Checks if all of the links are existing. If not: it stops the program.

        :param list[str] paths: list of paths to check
        '''
        for path in paths:
            if (os.path.exists(path) == False):
                print('[bold red]Alert![/bold red] :boom: This path does not exist: [green]' + path + '[/green]')
                raise typer.Exit()

    def check_database(self, dbs: list[str]):
        '''
        Checks if it is one of the databases

        :param list[str] dbs: list of database names
        '''

        for database in dbs:
            if database not in DATA_BASES:
                print('[bold red]Alert![/bold red] :boom: Please use only the keywords [green] (grand, grndb, humanbase'
                      ')[/green] for the database argument!')
                raise typer.Exit()

    def create_parser(self, parser_str: str):
        '''Create the right parser object

        :param str parser_str: define the parser
        :return object: the right parser object
        '''

        if parser_str == 'grand':
            return GrandParser()
        elif parser_str == 'grndb':
            return GrndbParser()
        elif parser_str == 'humanbase':
            return HumanBaseParser()

    def check_statistics(self, statistics: list[str]):
        '''
        checks if it is one of the statistics operations
        :param list[str] statistics: defines which statistics operation should be applied
        '''
        for stat in statistics:
            if stat not in STATISTIC_OPERATIONS:
                print('[bold red]Alert![/bold red] :boom: Please use only the keywords [green] (log_plot, plot, '
                      'fitting_summary)[/green] for the database argument!')
                raise typer.Exit()