from fastapi import FastAPI
from mongoengine import connect

from api.config import settings
from api.users.routers import users

connect('todo_api_db', host=settings.MONGO_URL)

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Opa, tá funcionando. Estamos respondendo da raiz da API!!!'}


app.include_router(users.router)
