import os
import errno

class Provider:
    @staticmethod
    def CreateDatabase(db_uri=""):
        created_state = False
        if len(db_uri)==0:
            raise Exception(
                'Database uri must be a valid path'
            )
        # create the folder container :
        try:
            os.mkdir(db_uri.split('/')[0])
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                pass
        # create new file as a data base : 
        with open(db_uri, "a+") as created_data_base:
            created_state = True
        return created_state
    @staticmethod
    def CheckModel(modal_list=[],table_name=""):
        return  table_name in modal_list
    @staticmethod
    def AppendModal(global_config={},modal_name=""):
        # create new migration
        new_modals_list = global_config['modals']
        new_migration_list.append(modal_name)
        print(f"\n  { modal_name } { new_modals_list }")
        migration = dict(
            name = f"Create New Table for modal : { modal_name }",
            state=False
        )
        new_migration_list = global_config['migrations']
        print(f"\n { migration } { new_migration_list }")
        # update global config file : 
        current_data = {
            'path': global_config['path'],
            'main': global_config['main'],
            'database_uri': global_config['database_uri'],
            'tables': [],
            'modals': new_modals_list,
            'migrations': new_migration_list
        }
        print(f"\n { current_data }")
        with open("../../config/data_file.json", "w+") as write_file:
            json.dump(current_data, write_file)
        return f" config/data_file.json has been Updated -> New Modal created "
    @staticmethod
    def MakeModal(project_uri="",modal_name=""):
        check_state = 404
        # step 1 create a Folder named Modals :
        try:
            directory_modal  = project_uri+"/Modals"
            os.mkdir(directory_modal)
            check_state -= 4 
            # step 2 create file __init__.py to define folder as python pack 
            with open(directory_modal+"/__init__.py", "w") as write_file:
                check_state -= 100
            directory_modal += '/'+str(modal_name)
            # step 3  create folder with the same name of the modal_name
            try:
                os.mkdir(directory_modal)
                check_state -= 100
                # step 4 create __init__.py to define modal ad a python pack 
                with open(directory_modal+"/__init__.py","w") as write_file:
                    check_state += 99
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(directory_modal):
                    pass
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(directory_modal):
                pass
        return check_state == 299