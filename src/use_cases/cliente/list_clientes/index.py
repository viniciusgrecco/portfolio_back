# use_cases/cliente/list_clientes/index.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from use_cases.cliente.list_clientes.list_clientes_use_case import ListClientesUseCase
from database import get_session

list_clientes_use_case = ListClientesUseCase()
router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get(
    "",
    summary="Listar todos os clientes",
    description="Retorna uma lista com todos os clientes cadastrados no sistema",
    response_description="Lista de clientes",
    responses={
        200: {
            "description": "Lista de clientes",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "nome": "João",
                            "sobrenome": "Silva",
                            "perfil": "moderado",
                            "idade": 30
                        },
                        {
                            "id": 2,
                            "nome": "Maria",
                            "sobrenome": "Santos",
                            "perfil": "agressivo",
                            "idade": 28
                        }
                    ]
                }
            }
        }
    }
)
def list_clientes(session: Session = Depends(get_session)):
    """
    Lista todos os clientes cadastrados no sistema.
    
    Retorna uma lista vazia se não houver clientes cadastrados.
    """
    return list_clientes_use_case.execute(session)