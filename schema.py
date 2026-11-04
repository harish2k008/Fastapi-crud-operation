from pydantic import BaseModel
class TodoList(BaseModel):
    title:str
    description:str|None=None
    
class TodoUpdate(BaseModel):
    title: str
    description: str | None = None

class Detail(BaseModel):
    name:str
    password:str    

class updateDetail(BaseModel):
    name:str
    password:str   