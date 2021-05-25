import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import display, Image
from PIL import Image


def get_picture_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print('abs_path =', abs_path)
    dir_files = os.listdir(abs_path)
   # print(dir_files)
    return dir_files


picture_list = get_picture_list('pictures')
print("picture list", picture_list)


def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print('Creating database and table schema')
        sql = '''create table if not exists PICTURES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PICTURE BLOB,
        TYPE TEXT,
        FILE_NAME TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print('Schema exists\n')
    return conn

def insert_picture(conn, picture_file):
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()



def extract_picture(cursor, picture_id):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = :id"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename



conn = create_or_open_db('picture_db.sqlite')
cur = conn.cursor()
#picture_file = "./pictures/hamim.jpg"
#insert_picture(conn, picture_file)
#filename = extract_picture(cur, 1)
#cur.close()
#conn.close()
#Image(filename='./'+filename)
print("All FILE_NAMES FROM PICTURES directory listed below & outputting picture_file at index 1 aka hamim.jpg")
for fn in picture_list:
    picture_file = "./pictures/"+fn
    insert_picture(conn, picture_file)
    filename = extract_picture(cur, 1)
    image = Image.open(filename)
    #image = Image.open(filename='./'+filename)

image.show(filename)

     
for r in conn.execute("SELECT FILE_NAME FROM PICTURES"):
    print(r[0])

cur.close()
conn.close()

