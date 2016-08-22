
db = connect_db('host')
try:
    db.query()  # Fails, Raise
except:
    pass
finally:
    db.close()

"========"

with connect_db('host') as db:
    db.query()
# ...
print("More work")