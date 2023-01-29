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
        for modal_item in modal_list:
            if modal_item == table_name:
                return True
        return  False
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
                # step 4 reate __init__.py to define modal ad a python pack 
                with open(directory_modal+"/__init__.py","w") as write_file:
                    check_state += 99
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(directory_modal):
                    pass
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(directory_modal):
                pass
        return check_state == 299