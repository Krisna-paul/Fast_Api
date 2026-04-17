from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    ID: int
    Name: str
    Age: int

app = FastAPI()

@app.get("/user", response_model = User)

def read():
    return User(ID = 2008034, Nmae = "krisna", Age = 30)