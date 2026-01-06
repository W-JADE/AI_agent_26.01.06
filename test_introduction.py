from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path
from datetime import datetime
import csv

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def introduction(request:Request) :
    return templates.TemplateResponse(
        "join-us.html",{"request":request}
    )
    
@app.post("/join")
def introduction(
    requst : Request,
    name : str =Form(...),
    age : str =Form(...),
    address : str =Form(...),
    phone : str =Form(...),
    email : str =Form(...),
    gender : str =Form(...)
) :
    print(">>> [POST] - /join", name,address,age,email,phone,gender)
    return {
        "name" : name,
        "age" : age,
        "address" : address,
        "phone" : phone,
        "email" : email,
        "gender" : gender,
    }