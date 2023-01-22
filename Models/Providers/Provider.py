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