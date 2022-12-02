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
    
db_file = "inventory.db"

conn = None
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)

    # Create tables
    cur = conn.cursor()
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()

def create_tables(cur):
    # conn = None
    try:
    #     conn = sqlite3.connect(db_file)
    #     print(sqlite3.version)

    #     # Create tables
    #     cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS user(PRIMARY KEY(userID))")
        cur.execute("CREATE TABLE IF NOT EXISTS shelf(PRIMARY KEY(shelfID), slotcount INT NOT NULL, FOREIGN KEY (userID) REFERENCES user(userID) ON DELETE CASCADE")
        cur.execute("CREATE TABLE IF NOT EXISTS slot(PRIMARY KEY(slotnum), capacity INT NOT NULL, itemcount INT NOT NULL, PRIMARY KEY(shelfID), FOREIGN KEY(shelfID) REFERENCES shelf(shelfID)")
        cur.execute("CREATE TABLE IF NOT EXISTS item(PRIMARY KEY(itemID), stock INT NOT NULL, VARCHAR(30) description, price DECIMAL(19,2), FOREIGN KEY (slotnum) REFERENCES slot(slotnum) ON DELETE CASCADE")
        cur.execute("CREATE TABLE tag(PRIMARY KEY(tagname), itemcount INT NOT NULL)")
        cur.execute("CREATE TABLE itemhastag(PRIMARY KEY(itemID, tagname), FOREIGN KEY (itemID) REFERENCES item(itemID), FOREIGN KEY (tagname) REFERENCES tag(tagname)")

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    
def insert_item(cur, conn, itemidparam, stock, descr, price, slotnum):
    cur.execute(f"INSERT INTO item (itemID, stock, description, price, slotnum) VALUES ({itemidparam}, {stock}, {descr}, {price}, {slotnum})")
    conn.commit()

def insert_user(cur, conn, userid):
    cur.execute(f"INSERT INTO user (userID) VALUES ({userid})")
    conn.commit()

def insert_shelf(cur, conn, shelfid, slotcount, userid):
    cur.execute(f"INSERT INTO shelf (shelfIDparam, slotcounparamt, useridparam) VALUES ({shelfid}, {slotcount}, {userid})")
    conn.commit()

def insert_slot(cur, conn, slotnum, capacity, itemcount, shelfid):
    cur.execute(f"INSERT INTO slot (slotnum, capacity, itemcount, shelfid) VALUES ({slotnum}, {capacity}, {itemcount}, {shelfid})")
    conn.commit()

def insert_tag(cur, conn, tagname, itemcount):
    cur.execute(f"INSERT INTO tag (itemID, stock, description, price, slotnum) VALUES ({tagname}, {itemcount})")
    conn.commit()

def remove_item(cur,  conn, itemid):
    cur.execute(f"REMOVE FROM item WHERE itemID='{itemid}")
    conn.commit()

def remove_user(cur, conn, userid):
    cur.execute(f"REMOVE FROM user WHERE itemID='{userid}")
    conn.commit()

def remove_shelf(cur, conn, shelfid):
    cur.execute(f"REMOVE FROM shelf WHERE itemID='{shelfid}")
    conn.commit()

def remove_slot(cur, conn, shelfid, slotid):
    cur.execute(f"REMOVE FROM slot WHERE itemID='{slotid} AND shelfid='{shelfid}")
    conn.commit()    

def remove_tag(cur, conn, tagname, itemid):
    cur.execute(f"REMOVE FROM tag WHERE itemID='{tagname}")
    cur.execute(f"REMOVE FROM itemhastag WHERE tagname='{tagname}' AND itemID='{itemid}")
    conn.commit()
