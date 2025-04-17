from pydantic import BaseModel
#Matheus Felipe Ribeiro Cruz de Mello

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str = None
    valor_unitario: float
    foto: bytes = None