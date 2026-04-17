from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    ID: int
    Name: str
    Age: int

app = FastAPI()

@app.get("/user", response_model = User)

def get_user():
    return User(ID=1, Name="Krisna", Age=30)
