import mysql.connector

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config
    
    def __enter__ (self):
        """Returns a cursor"""
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor(buffered=True)
        """If buffered is True, the cursor fetches all rows from
        the server after an operation is executed. This is useful when
        queries return small result sets. buffered can be used alone,
        or in combination with the dictionary or named_tuple argument. """
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

