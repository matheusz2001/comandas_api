from pydantic import BaseModel
#Matheus Felipe

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str