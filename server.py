from fastapi import FastAPI, Request
import json, os
from initDb import initLocalDb
from students import read, create, update, delete, readOne
from studentSchema import Student

app = FastAPI()

@app.get("/")
def getDefaultData():
    return { "status": "success", "msg": "Default page loaded successfully" }

@app.get("/students/read")
def getStudentsData():
    initLocalDb()
    return read()

@app.get("/students/read/")
def getStudentData(request: Request):
    initLocalDb()
    return readOne(request.query_params.get("id", None))

@app.post("/students/create")
def getStudentData(student: Student):
    initLocalDb()
    return create(student)

@app.post("/students/update/")
def getStudentData(student: Student):
    initLocalDb()
    return update(student)

@app.post("/students/delete/")
def getStudentData(request: Request):
    initLocalDb()
    return delete(request.query_params.get("id", None))