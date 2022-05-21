"""
DatabaseSettingModule
------------------------
This a a Module which has Class for Database

"""

class Database(object):
    """Databse Class which is responsible for connectin to database"""
    def __init__(self,connection_string) -> None:
        """
        This is connection string to connect to sql server
        """
        self.connection_string = connection_string

    def connect(self) -> True:
        """
        This method is used to connect to database
        """
        print("connected to database")
        return True