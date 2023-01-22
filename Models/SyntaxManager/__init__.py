from rich.console import Console
from Models.Providers.Provider import Provider
class CommandManager:
    # define the alowed commands : 
    def __init__(self):
        """
        define all command and flags allowed : 
        
        """
        self.Allowed_command = {
            'make':['Modal','Migration'],
            'create':['Table','DataBase']
        }
        self.Printer = Console()
    def manage_command(self, command_arr=[],global_config={}):
        # check command :
        if command_arr[0] == 'manager':
            # check the rest :
            # command must be a base-command:flag
            flag_sliter = command_arr[1].split(':')
            # check if flag_spliter is a base command : 
            if flag_sliter[0] in self.Allowed_command:
                # check if the flag is allowed by the command base :
                if flag_sliter[1] in self.Allowed_command[flag_sliter[0]]:
                    # manage the create providers :
                    if flag_sliter[0] == 'create' and flag_sliter[1] == 'DataBase':
                        # call provider static methos to manage task ;
                        create_state = Provider.CreateDatabase(global_config['database_uri'])
                        if create_state == True:
                            self.Printer.print(
                                f"\t[bold blue] { global_config['database_uri']  } => created  [/] \n")
                    # manager create tabel providers:
                    if flag_sliter[0] == 'create' and flag_sliter[1] == 'Table':
                        # step 1 check syntax and the table name must be non null 
                        try: 
                            self.Printer.print(
                                f"\t[bold blue] { command_arr[2]  } => created  [/] \n")
                        except:
                            raise Exception(
                                'Table name is null '
                                )
                        # check if there is a model with the same name of the table:
                        # 
                    return
                else:
                    raise Exception(
                        f' { flag_sliter[1] } not supported by { flag_sliter[0]} ')
            else:
                raise Exception(
                    f'{ flag_sliter[0] } is not a valid command or option :( '
                )
        else:
            raise Exception(
                'all Pylite3 command must started with manager'
            )
