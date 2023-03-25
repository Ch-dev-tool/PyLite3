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
                                f"\t [bold blue] check Modal { command_arr[2]  } ..  [/]")
                        except:
                            raise Exception(
                                'Table name is null '
                                )
                        # check if there is a model with the same name of the table:
                        modal_state = Provider.CheckModel(
                            global_config['modals'], command_arr[2])
                        if not modal_state:
                            raise Exception(
                                f'There is no Modal {command_arr[2] }  '
                            )
                    # manage make Modal provider :
                    if flag_sliter[0] == 'make' and flag_sliter[1] == 'Modal':
                        try:
                            # check if there is a modal name as args :
                            self.Printer.print(
                                f"\n\t [bold blue] check Modal { command_arr[2]  } ..  [/]")
                            response_state = Provider.MakeModal(
                                                                global_config['path'],
                                                                command_arr[2]
                                                                )
                            # check response state if is equale to 299:
                            if response_state is True:
                                print( response_state )
                                modal_name = command_arr[2]
                                self.Printer.print(
                                    f"\n\t [bold blue] { modal_name  } Modal  created  [/]")
                                # add new modal to the global config :
                                message_add_modal = Provider.AppendModal(
                                                    global_config,
                                                     modal_name
                                                     )
                                self.Printer.print(
                                    f"\n\t [bold blue] { message_add_modal  }  [/]")
                            else:
                                print( response_state )
                                self.Printer.print(
                                    f"\n\t [bold red][error] ==> error create Modal <{ command_arr[2]  }>  [/]")
                        except Exception as e:
                            raise Exception(
                                'Modal name is null '+str(e)
                            )
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
