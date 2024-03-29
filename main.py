# import all package we nee to : 
from rich.console import Console
import sys
import os
import json
import errno

from Models.ManagerModel.manage import Manager
# define my input manager class : 

class inputHandller:
    def __init__(self, project_path="", entry_script=""):
        # initial value :
        self.project_path = project_path
        self.entry_script = entry_script
        self.my_console = Console()
    @staticmethod
    def get_config():
        # this method is allowd only if the project already initialized 
        # read json data from config/data_file.json:
        with open('config/data_file.json', 'r') as source_data:
            return json.load(source_data)
    def save_state(self):
        # save folder path and main script as an json file attributes :
        self.my_console.print(
            f"\n\t [bold black] {self.project_path} and {self.entry_script} has been initialized  [/]\n")
        self.data = {
            'path':self.project_path,
            'main':self.entry_script,
            'database_uri':'Database/my_db.sqlite',
            'tables': json.dumps([]),
            'modals': json.dumps([]),
            'migrations': json.dumps([])
        }
        # create config folder :
        try:
            directory_config ="config"
            os.mkdir(directory_config)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(directory_config):
                pass
        with open("config/data_file.json", "w") as write_file:
            json.dump(self.data, write_file)
# execution state : 

if __name__ == "__main__":
    try:
        my_console = Console()
        # check if the command is an setup command ==> len(sys.argv) == 1 or more ( configuration command )
        if len( sys.argv )==2:
            folder_target = sys.argv[1]
            if folder_target == ".":
                folder_target = "current_folder"
                folder_path = os.getcwd()
                my_console.print(
                    f"\t[bold underline blue] { folder_path } initialized[/] \n")
                # get all files :
                file_list = os.listdir(folder_path)
                detected_files = []
                # filter only python files : 
                for file_name in file_list:
                    if os.path.isfile(file_name) and file_name.split('.')[1] == 'py':
                        my_console.print(
                            f"\t[bold black] { file_name }[/][bold blue]  detected  [/] \n")
                        detected_files.append(file_name)
                file_input =my_console.input(
                    "\t[bold blue] Select your entry script :  [/]"
                )
                # check if the file selected is in the file list :
                response = False
                while response == False:
                    if file_input in detected_files:
                        response = True
                        break
                    file_input = my_console.input(
                        "\n\t[bold red] Select a valid entry script :  [/]"
                    )
                my_console.print(
                    f" \n\t[underline black]{ file_input }[/] [bold blue] selected as main script   [/] \n")
                # all is good : we ned to create our manager :
                my_handler = inputHandller(folder_path,file_input)
                my_handler.save_state()
        if len(sys.argv) > 2:
            # is an configuration command :
            # step 1 : check if the folder has ben initialised :
            configuration_state = False
            for item in os.listdir(os.getcwd()):
                if item == "config" and os.path.isdir(item):
                    configuration_state = True
                    break
            if configuration_state == False:
                my_console.print("\n\t [black] your folder has not inisialized yet :(  [/] \n")
                exit()
            else:
                # start managing command by the manager class :
                config_data = inputHandller.get_config()
                my_manager = Manager(config_data,sys.argv)
                # start :
                my_manager.start_watch()
    except  Exception as e:
        my_console.print("\n\t[bold red][error] ==> "+str(e)+"[/] \n")