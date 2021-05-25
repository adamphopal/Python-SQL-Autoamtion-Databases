import sqlite3

def Main():
	try:
		con = sqlite3.connect('test.db')
    
		cur = con.cursor() 
		cur.executescript("""DROP TABLE IF EXISTS Bruins;
				CREATE TABLE Bruins(Id INT, Name TEXT, Insta TEXT);
				INSERT INTO Bruins VALUES(1, 'Summer Ray', 'sommerray');
				INSERT INTO Bruins VALUES(2, 'Kim Kardashian', 'kimkardashian');""")
    
		bruins = ((3, 'Jamie Stone', 'imjamiestone'),
			(4, 'Drake', 'chamagnepapi'),
			(5, 'Jen Selter', 'jenselter'))

		cur.executemany("INSERT INTO Bruins VALUES(?, ?, ?)", bruins)

		con.commit()

		cur.execute("SELECT * FROM Bruins")
		data = cur.fetchall()
		
		for row in data:
			print(row)

	except sqlite3.Error as e:
		if con:
			con.rollback()
	finally:
		if con:
			con.close()

if __name__ == '__main__':
	Main()



#first go to terminal and type sqlite3 test.db, to create a database
	#.exit to leave 
