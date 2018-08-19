from application.mongodb.mongo_connect import mongo

if __name__ == "__main__":
    count = 0
    for user in mongo.db.user.find():
        print(user['username'], )
        count = count + 1
    print(count)
