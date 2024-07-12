#import comp_scrap as cs
import datetime

def i(collection, dic):
    collection.insert_one(dic)

def d(db, ct):
    ct2 = ct - datetime.timedelta(days=7)
    for j in db.list_collection_names():
        if j <= str(ct2.date()):
            db[j].drop()
        
def search(db, d):
    if str(d) in db.list_collection_names():
        for j in db[str(d)].find({}, {'_id':0}):
            print('\n')
            for key, value in j.items():
                print(key, ' -> ', value)
    else:
        print('no data available for this date!')