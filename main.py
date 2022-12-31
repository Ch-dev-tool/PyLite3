# import all package we nee to : 
from rich.console import Console
import sys
import os
import json
import errno


# define my input manager class : 

class inputHandller:
    def __init__(self, project_path="", entry_script=""):
        # initial value ::
        self.project_path = project_path
        self.entry_script = entry_script
        self.my_console = Console()
        self.save_state()
    def save_state(self):
        # save folder path and main script as an json file attributes :
        self.my_console.print(
            f"\n\t [bold black] {self.project_path} and {self.entry_script} has been initialized  [/]\n")
        data = {
            'path':self.project_path,
            'main':self.entry_script,
            'database_uri':'Database/my_db.sqlite',
            'tables':[],
            'modals':[],
            'migrations':[]
        }
        # create config folder :
        try:
            directory_config ="config"
            os.mkdir(directory_config)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(directory_config):
                pass
        with open("config/data_file.json", "w") as write_file:
            json.dump(data, write_file)
        return
# execution state : 

if __name__ == "__main__":
    try:
        my_console = Console()
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
    except  Exception as e:
        my_console.print("\n\t[bold red][error] ==> "+str(e)+"[/]")