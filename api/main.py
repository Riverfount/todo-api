from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Opa, tá funcionando. Estamos respondendo da raiz da API!!!'}
