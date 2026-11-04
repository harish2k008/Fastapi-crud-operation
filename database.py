import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,sessionmaker
from sqlalchemy import String,Boolean

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__="todos"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String)
    description:Mapped[str|None]=mapped_column(String,nullable=True)
    
class User(Base):
   __tablename__="userdetail"
   id:Mapped[int]=mapped_column(primary_key=True)
   name:Mapped[str]=mapped_column(String)
   password:Mapped[str]=mapped_column(String)



load_dotenv()

DatabaseUrl=os.getenv("Database_Url")

engine=create_engine(DatabaseUrl)
SessionLocal=sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

"""db=SessionLocal()

todo = Todo(title="Learn FastAPI", description="Practice PostgreSQL")
db.add(todo)
db.commit()
db.close()"""

"""todos=db.query(Todo).all()
print(todos)
for todo in todos:
    print(todo.id, todo.title, todo.description)"""