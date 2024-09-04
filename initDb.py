import json, os
file_name = "db.json"
def initLocalDb():
    if not os.path.exists(file_name):
        print(f"DB is not presented creating one")
        with open(file_name, 'w') as file:
            file.write('{ "students": [] }')
            print("DB created successfully")
    print("DB already initialised!")

def getDBData():
    return json.load(open(file_name))

def updataDB(data):
    with open(file_name, 'w') as file:
        file.write(json.dumps(data))
    return { "status": "success" }