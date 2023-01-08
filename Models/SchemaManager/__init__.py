
from Models.SqlManager import SqlContext

# Schema is a user Model present an sql table :


class Schema:
    def __init__(self, db_uri="",schema_config={}, sql_manager=SqlContext()):
        # schema config is an python dict as 
        """
        {
            tables:[]
            Models:[]
            State:[]
        }
        """
        self.db_uri = db_uri
        self.configuration = schema_config
        self.sqlHandler = sql_manager