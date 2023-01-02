
from Models.SyntaxManager import CommandManager
from Models.SchemaManager import Schema
from Models.SqlManager import SqlContext
# create my class manager : 

class Manager:
    def __init__(self, config={}):
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
    def start_watch(self, user_command=""):
        # start my syntaxe manager:
        self.syntax_handler.manage_command(user_command)
        return         