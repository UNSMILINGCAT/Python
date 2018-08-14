import dbm

db = dbm.open('websites', 'c')
# add an item.
db['www.python.org'] = 'Python home page'
print(db['www.python.org'])
# close and save to disk
db.close()
