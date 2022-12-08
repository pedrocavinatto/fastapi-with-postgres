from fastapi import FastAPI, HTTPException
from database import Database
from Classes.User import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Giropops Stringus Girus"}

@app.get("/users")
async def users():
    try:
        db = Database("fastapizada", "postgres", "postgres", "localhost", 5432);
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
    print(user)
    try:
        db = Database("fastapizada", "postgres", "postgres", "localhost", 5432);
        cursor = db.connect()
        cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (user.name, user.email, user.age))
        db.close()
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.args)