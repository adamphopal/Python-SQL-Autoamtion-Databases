import sqlite3
from employee import Employee
from PIL import Image
from pydub import AudioSegment
from pydub.playback import play
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
import pandas as pd
import pickle


conx = sqlite3.connect('employee.db')
conx2 = create_engine("sqlite:///employee.db")

#df = pd.read_sql_query("SELECT * FROM employees", conx2)
#print(df.head())
#df = pd.DataFrame('employee.db')
#df = pd.DataFrame("SELECT * FROM employees", conx2)
#df.head()
df = pd.to_pickle(conx, conx2)
df2 = pd.read_pickle(conx, conx2)
print(df2.head())
