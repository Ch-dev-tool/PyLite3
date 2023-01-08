
from Models.SyntaxManager import CommandManager
from Models.SchemaManager import Schema
from Models.SqlManager import SqlContext
from rich.console import Console
# create my class manager : 

class Manager:
    def __init__(self, config={},arg_list=[]):
        # expected config dict : 
        """
        {
            'path':self.project_path,
            'main':self.entry_script,
            'database_uri':'Database/my_db.sqlite',
            'tables':[],
            'modals':[],
            'migrations':[]
        }
        """
        self.current_configuration = config
        self.my_console = Console()
        self.system_args = arg_list
        self.syntax_handler = CommandManager()
        self.schema_handler = Schema(
                                    db_uri=self.current_configuration['database_uri'],
                                    schema_config={
                                        'tables':self.current_configuration['tables'],
                                        'Models': self.current_configuration['modals'],
                                        'State':[]
                                    },
                                    sql_manager=SqlContext(db_uri=self.current_configuration['database_uri']))
        # for now all configuration done :) 
    # define methode to start all services :
    def start_watch(self):
        # start my syntaxe manager:
        # the command is an splited string => is an lsit :
        # filter my argument : ignore python main.py execution comand:
        self.system_args = self.system_args[1:]
        try:
            self.syntax_handler.manage_command(
                self.system_args, self.current_configuration)
        except  Exception as e:
            self.my_console.print("\n\t[bold red][error] ==> "+str(e)+"[/] \n")
        return 