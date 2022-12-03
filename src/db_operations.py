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

        self.conn = None
        self.conn = sqlite3.connect(db_file,check_same_thread=False)
        self.cur = self.conn.cursor()

    # def create_tables(self):
    # conn = None
        # try:
    #     conn = sqlite3.connect(db_file)
    #     print(sqlite3.version)

    #     # Create tables
    #     cur = conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user(user_id TEXT PRIMARY KEY)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS shelf(shelfID TEXT PRIMARY KEY, slotcount INTEGER NOT NULL, user_id TEXT, FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS slot(slotnum INTEGER, capacity INTEGER NOT NULL, itemcount INTEGER NOT NULL, shelfID TEXT, PRIMARY KEY(slotnum, shelfID) FOREIGN KEY(shelfID) REFERENCES shelf(shelfID))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS item(itemID INTEGER PRIMARY KEY, stock INTEGER NOT NULL, description TEXT, price FLOAT, slotnum INTEGER, shelfID TEXT, FOREIGN KEY (slotnum) REFERENCES slot(slotnum), FOREIGN KEY (shelfID) REFERENCES slot(shelfID) ON DELETE CASCADE)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS tag(tagname TEXT PRIMARY KEY, itemcount INTEGER NOT NULL)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS itemhastag(itemID INTEGER, tagname TEXT, PRIMARY KEY(itemID, tagname), FOREIGN KEY (itemID) REFERENCES item(itemID), FOREIGN KEY (tagname) REFERENCES tag(tagname))")
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
    # except Error as e:
        # print(e)
    # finally:
        # if conn:
            # conn.close()

    
    def insert_item(self, itemid, stock, descr, price, slotnum, shelfID):
        self.cur.execute(f"INSERT INTO item (itemID, stock, description, price, slotnum, shelfID) VALUES (?,?,?,?,?,?)",(itemid, stock, descr, price, slotnum, shelfID))
        self.conn.commit()

    def insert_user(self, userid):
        self.cur.execute(f"INSERT INTO user (user_id) VALUES (:userid)",{"userid":userid})
        self.conn.commit()

    def insert_shelf(self, shelfid, slotcount, userid):
        self.cur.execute(f"INSERT INTO shelf (shelfID, slotcount, user_id) VALUES (?,?,?)",(shelfid, slotcount, userid))
        self.conn.commit()

    def insert_slot(self, slotnum, capacity, itemcount, shelfid):
        self.cur.execute(f"INSERT INTO slot (slotnum, capacity, itemcount, shelfid) VALUES (?,?,?,?)",(slotnum, capacity, itemcount, shelfid))
        self.conn.commit()

    def insert_tag(self, tagname, itemcount):
        self.cur.execute(f"INSERT INTO tag (itemID, stock, description, price, slotnum) VALUES (?,?)",(tagname, itemcount))
        self.conn.commit()

    def get_item(self, itemID=None, shelfID=None): 
        cur = None 
        if itemID:
            cur = self.cur.execute("""SELECT * FROM item WHERE itemID = :itemID""",{"shelfid":itemID})
            
        else:
            if shelfID:
                cur = self.cur.execute("""SELECT * FROM item WHERE shelfID = :shelfID""",{"shelfID":shelfID})
            else:
                cur = self.cur.execute("""SELECT * FROM item""")
        return cur.fetchall()

    def get_shelf(self, shelfID):
        self.cur.execute("""SELECT * FROM item WHERE shelfID = :shelfID""",{"shelfID":shelfID})

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
