import pyodbc


class db_helper:

    def __init__(self, csv_file_nm, sql_server_nm, db_nm, db_table_nm):
        conn = self.connect_db(sql_server_nm, db_nm)
        self.insert_data(conn, csv_file_nm, db_table_nm)
        conn.close

    def connect_db(self, sql_server_nm, db_nm):
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + sql_server_nm + ';DATABASE=' + db_nm + ';Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_string)
        return conn

    def insert_data(self, conn, csv_file_nm, db_table_nm):
        qry = "BULK INSERT " + db_table_nm + " FROM '" + csv_file_nm + "' WITH (DATAFILETYPE = 'char', FIRSTROW = 6, FIELDTERMINATOR = ',')"
        cursor = conn.cursor()
        success = cursor.execute(qry)
        conn.commit()
        cursor.close