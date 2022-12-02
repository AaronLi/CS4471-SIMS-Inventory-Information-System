import sqlite3
from sqlite3 import Error

# db_file = "inventory.db"

# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()

# def create_tabled(conn):
#     hh


# #if __name__ == '__main__':
#  #   create_connection(r".")
class InventoryDB: 
    def __init__(self):

        db_file = "inventory.db"

        conn = None
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()

    # def create_tables(self):
    # conn = None
        # try:
    #     conn = sqlite3.connect(db_file)
    #     print(sqlite3.version)

    #     # Create tables
    #     cur = conn.cursor()
        self.self.cur.execute("CREATE TABLE IF NOT EXISTS user(PRIMARY KEY(userID))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS shelf(PRIMARY KEY(shelfID), slotcount INT NOT NULL, FOREIGN KEY (userID) REFERENCES user(userID) ON DELETE CASCADE")
        self.cur.execute("CREATE TABLE IF NOT EXISTS slot(PRIMARY KEY(slotnum), capacity INT NOT NULL, itemcount INT NOT NULL, PRIMARY KEY(shelfID), FOREIGN KEY(shelfID) REFERENCES shelf(shelfID)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS item(PRIMARY KEY(itemID), stock INT NOT NULL, VARCHAR(30) description, price DECIMAL(19,2), FOREIGN KEY (slotnum) REFERENCES slot(slotnum) ON DELETE CASCADE")
        self.cur.execute("CREATE TABLE IF NOT EXISTS tag(PRIMARY KEY(tagname), itemcount INT NOT NULL)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS itemhastag(PRIMARY KEY(itemID, tagname), FOREIGN KEY (itemID) REFERENCES item(itemID), FOREIGN KEY (tagname) REFERENCES tag(tagname)")
    
    def __del__(self):
            self.conn.close()
    # except Error as e:
        # print(e)
    # finally:
        # if conn:
            # conn.close()

    
    def insert_item(self, itemidparam, stock, descr, price, slotnum):
        self.cur.execute(f"INSERT INTO item (itemID, stock, description, price, slotnum) VALUES ({itemidparam}, {stock}, {descr}, {price}, {slotnum})")
        self.conn.commit()

    def insert_user(self, userid):
        self.cur.execute(f"INSERT INTO user (userID) VALUES ({userid})")
        self.conn.commit()

    def insert_shelf(self, shelfid, slotcount, userid):
        self.cur.execute(f"INSERT INTO shelf (shelfIDparam, slotcounparamt, useridparam) VALUES ({shelfid}, {slotcount}, {userid})")
        self.conn.commit()

    def insert_slot(self, slotnum, capacity, itemcount, shelfid):
        self.cur.execute(f"INSERT INTO slot (slotnum, capacity, itemcount, shelfid) VALUES ({slotnum}, {capacity}, {itemcount}, {shelfid})")
        self.conn.commit()

    def insert_tag(self, tagname, itemcount):
        self.cur.execute(f"INSERT INTO tag (itemID, stock, description, price, slotnum) VALUES ({tagname}, {itemcount})")
        self.conn.commit()

    def remove_item(self, itemid):
        self.cur.execute(f"REMOVE FROM item WHERE itemID='{itemid}")
        self.conn.commit()

    def remove_user(self, userid):
        self.cur.execute(f"REMOVE FROM user WHERE itemID='{userid}")
        self.conn.commit()

    def remove_shelf(self, shelfid):
        self.cur.execute(f"REMOVE FROM shelf WHERE itemID='{shelfid}")
        self.conn.commit()

    def remove_slot(self, shelfid, slotid):
        self.cur.execute(f"REMOVE FROM slot WHERE itemID='{slotid} AND shelfid='{shelfid}")
        self.conn.commit()    

    def remove_tag(self, tagname, itemid):
        self.cur.execute(f"REMOVE FROM tag WHERE itemID='{tagname}")
        self.cur.execute(f"REMOVE FROM itemhastag WHERE tagname='{tagname}' AND itemID='{itemid}")
        self.conn.commit()
