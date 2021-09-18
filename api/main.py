from fastapi import FastAPI
from mongoengine import connect

connect('todo_api_db', host='mongodb://localhost')

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Opa, tá funcionando. Estamos respondendo da raiz da API!!!'}
