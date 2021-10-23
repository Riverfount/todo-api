from fastapi import FastAPI
from mongoengine import connect

from api.config import settings
from api.users.routers import users

connect('todo_api_db', host=settings.MONGO_URL)

description = """
Esta é uma API para registro de tarefas a fazer.

## Resources

### Users
Com esse resource nós podemos registrar os dados do usuário. Seguindo como abaixo:
- GET - Listar todos os usuários
- GET {ID} - Listar detalhes do usuário por ID
- POST - Criar um novo usuário
- PATCH {ID} - Alterar um usuário existente por seu ID
- DELETE {ID} - Deletar um usuário por seu ID

### Todo
Com esse resource nós podemos registrar os dados das tarefas a serem feitas. Seguindo como abaixo:
- GET - Listar todas as tarefas
- GET {ID} - Listar detalhes das tarefas por ID
- POST - Criar uma nova tarefa
- PATCH {ID} - Alterar uma tarefa existente por seu ID
- DELETE {ID} - Alterar o status da tarefa para "Done" (tarefa realizada)

"""

app = FastAPI(
    title='TODO API',
    description=description,
    version='0.1.0',
    contact={
        'name': 'Riverfount - aka Vicente Marçal',
        'email': 'vicente.marcal@gmail.com',
    }
)


@app.get('/')
def home():
    return {'message': 'Opa, tá funcionando. Estamos respondendo da raiz da API!!!'}


app.include_router(users.router)
