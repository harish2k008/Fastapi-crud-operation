from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session, sessionmaker
from database import Todo
from todo import get_db
from schema import TodoList, TodoUpdate

app=FastAPI()

@app.post("/start")

def create_todos(pytodo:TodoList ,db:Session=Depends(get_db)):

    new_todo=Todo(
        title=pytodo.title,
        description=pytodo.description
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)


@app.get("/retrieve/{todo_id}")

def get_todos(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if todo is None:
        raise HTTPException(status_code=404,detail="Not Found broh!!")

    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description
    }

@app.put("/update/{todo_id}")

def update_todo(todo_id:int,data:TodoUpdate,db:Session=Depends(get_db)):

    todo=db.query(Todo).fiter(Todo.id==todo_id).first()

    if todo is None:
        raise HTTPException(status_code=404,detail="Not found broh")

    todo.title=data.title
    todo.description=data.description

    db.commit()
    db.refresh(todo)


    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description
    }


@app.delete("/todos")
def delete_multiple_todos(
    todo_ids: list[int],
    db: Session = Depends(get_db)
):
    todos = db.query(Todo).filter(Todo.id.in_(todo_ids)).all()

    if not todos:
        raise HTTPException(status_code=404, detail="No todos found")

    deleted_count = len(todos)

    for todo in todos:
        db.delete(todo)

    db.commit()

    return {
        "message": "Todos deleted successfully",
        "deleted_count": deleted_count
    }
