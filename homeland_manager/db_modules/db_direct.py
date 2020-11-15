import sqlite3

class DBconnetcion():
    sqlite_file = 'db.sqlite3'

    def __init__(self):
        conn = sqlite3.connect('db.sqlite3')
        self.c = conn.cursor()

    def get_common_dues_for_date(self, date):
        self.c.execute(f'''SELECT * FROM homeland_manager_commondue
                         WHERE tax_date_id = (SELECT id FROM homeland_manager_paymentdate
                                              WHERE dates="{date}")''')
        all_rows = self.c.fetchall()
        return all_rows

    def get_elevator_dues_for_date(self, date):
        self.c.execute(f'''SELECT * FROM homeland_manager_elevatordue
                          WHERE tax_date_id = (SELECT id FROM homeland_manager_paymentdate
                                              WHERE dates="{date}")''')
        all_rows = self.c.fetchall()
        return all_rows


    def close_db_connection(self):
        # Closing the connection to the database file
        self.c.close()