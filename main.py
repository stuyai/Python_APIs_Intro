from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

with open("number.txt", "w")  as f:
    f.write(str(1)) 

@app.get("/iterate")
def iterate():
    with open("number.txt", "r+") as f:
        ret = f.read()
        number = int(ret.strip() if ret != "" else 1)
        f.seek(0)
        f.write(str(number + 1))
        f.truncate()
    return {"Number": number}

names = []


@app.get("/names")
def get_names():
    return {"names": names}


@app.post("/addname/{name}", response_model=str)
def addname(name: str):
    names.append(name)
    return name

right_num = 0
@app.put("/set_right_num/{s_num}", response_model=str)
def set_right_num(s_num:str):
    global right_num
    right_num = int(s_num)
    return str(right_num)

@app.get("/right_num")
def get_right_num():
    return {"right_num": str(right_num)}