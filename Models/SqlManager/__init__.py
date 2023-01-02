


# define my class manager for all sql query and CRUD Operations 


class SqlContext:
    def __init__(self,db_uri=""):
        # database url : 
        self.Db_target = db_uri