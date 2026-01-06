from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() :
    obj = {
        "message" : "안녕하세요!",
        "user": "실습시간입니다!"
    }
    return obj

@app.get("/hello")
def hello01(name="hong") :
    print("name is", name)
    return {
        "name":name
    }
    
@app.post("/hello")
def hello02(name="hong") :
    print("name is", name)
    return {
        "name":name
    }
    
