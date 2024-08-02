from fastapi import FastAPI
from dbreq import data, get_info_for_id
from pydantic import BaseModel

app = FastAPI(
    title="Tred"
)


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return get_info_for_id(user_id)

class Inf(BaseModel):
    id: int
    user_name: str
    contacts: str



@app.post("/users")
def add_users(datas: list[Inf]):
    data.extend(datas)
    return {"status":200, "data": data}



