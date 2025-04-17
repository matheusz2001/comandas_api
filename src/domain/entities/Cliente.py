from pydantic import BaseModel
#Matheus Felipe Ribeiro Cruz de Mello

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str