from application.mongodb.mongo_connect import mongo

user1 = {"_id": "06",
            "username": "test1",
            "password": "01234",
            "privilege": "0",
        }

#user_id = mongo.db.testuser.insert_one(user1)
collist = mongo.db.collection_names()
for col in collist:
    print(collist)

dbase = mongo.db.testuser.find()

for doc in mongo.db.testuser.find({"username": "test1"}):
    print(doc)