import dbm

# open existing file
db = dbm.open('websites', 'w')
# add another item
db['www.wrox.com'] = 'wrox home page'
# Verify the previous item remains
if db['www.python.org'] is not None:
    print('Found www.python.org')
else:
    print('Error: Missing item')
# Iterate over the keys . May be slow.
# May use a lot of memory.
for key in db.keys():
    print("key = ", key, "Value = ", db[key])
del db['www.wrox.com']
print("After deleting www.wrox.com, we have:")
for key in db.keys():
    print("key = ", key, " Value = ", db[key])
# close and save to disk
db.close()
