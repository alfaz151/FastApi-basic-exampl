from initDb import getDBData, updataDB
def read():
    data = getDBData()
    return data["students"]

def readOne(id):
    if not id:
        return { "status": "unsucess", "error": "Insufficient data! Student id not found"}
    data = (getDBData())["students"]
    for student in data:
        if student["id"] == id:
            return student
        
def create(student):
    if not (student.id or student.name):
        return { "status": "unsuccess", "error": "Insufficient data! Student id or name not found" }
    data = getDBData()
    data["students"].append(student)
    updataDB(data)
    return { "status": "success", "msg": "Student created sucessfully" }

def update(student):
    studentpresent = false, i = 0
    if not (student["id"] or student["name"]):
        return { "status": "unsuccess", "error": "Insufficient data! Student id or name not found" }
    data = getDBData()
    while i < len(data["students"]):
       if data["students"][i]["id"] == student["id"]:
           data["students"][i]["name"] = student["name"]
           studentpresent = True 
           break
    updataDB(data)
    if not studentpresent:
        return { "status": "unsuccess", "error": f"Student with id {student["id"]} not found" }
    return { "status": "success", "msg": f"Student with id {student["id"]} updated successfully" } 

def delete(id):
    studentpresent = false, i = 0
    if not id:
        return { "status": "unsuccess", "error": "Insufficient data! Student id not found" }
    data = getDBData()
    while i < len(data["students"]):
       if data["students"][i]["id"] == id:
           data["students"].pop(i)
           studentpresent = True 
           break
    updataDB(data)
    if not studentpresent:
        return { "status": "unsuccess", "error": f"Student with id {id} not found" }
    return { "status": "success", "msg": f"Student with id {id} deleted successfully" }
