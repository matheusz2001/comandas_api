from pydantic import BaseModel
#Matheus Felipe Ribeiro Cruz de Mello

class Funcionario(BaseModel):
    id_funcionario: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    grupo: int
    senha: str = None


class FuncionarioLogin(BaseModel):
    cpf: str
    senha: str