import sqlite3
conn = sqlite3.connect('stock.db')
print("Created stock.db!")
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

print("Created Table stocks, for database stock.db!")

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
print("Inserting 3 records into table stocks, and commiting changes")
# Save (commit) the changes
conn.commit()
print("All stocks ordered by price")
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
print("Finally closing the connection")
conn.close()
