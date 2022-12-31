from fastapi import FastAPI, HTTPException
from database import Database
from Classes.User import User
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Env variables
db_name = os.environ['POSTGRES_DB']
db_user = os.environ['POSTGRES_USER']
db_password = os.environ['POSTGRES_PASSWORD']
db_host = os.environ['POSTGRES_HOST']
db_port = os.environ['POSTGRES_PORT']


@app.get("/")
async def root():
    return {"message": "Giropops Stringus Girus"}

@app.get("/users")
async def users():
    try:
        db = Database(db_name, db_user, db_password, db_host, db_port);
        cursor = db.connect()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        db.close()
        usuarios = []
        for user in users:
            usuarios.append(User(id=user[0], name=user[1], email=user[2], age=user[3]))
        return usuarios
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.args)

@app.post("/users", status_code=201)
async def create_user(user: User):
    try:
        db = Database(db_name, db_user, db_password, db_host, db_port);
        cursor = db.connect()
        cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (user.name, user.email, user.age))
        db.close()
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.args)