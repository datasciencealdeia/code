from fastapi import FastAPI, HTTPException
import datetime

app = FastAPI()

dict_pessoas = {}

#...
@app.post("/adicionar-pessoa")
def adicionar_pessoa(cpf: int, nome: str):
   if cpf in dict_pessoas:
      raise HTTPException(status_code=400, detail="CPF já cadastrado.")
   dict_pessoas[cpf] = (cpf, nome)
  
@app.get('/nome-pessoa/{cpf}')
def nome_pessoa(cpf: int):
   if cpf not in dict_pessoas:
      raise HTTPException(status_code=400, detail="Pessoa inexistente.")
   return dict_pessoas[cpf][1]

@app.get('/teste_async')
async def teste(id: int):
   return "Teste " + str(id)

@app.get('/teste_sync')
def teste_sync(id: int):
   return "Teste Sync " + str(id)