"""
Configuração do banco de dados
Gerencia conexão com MySQL e criação de tabelas
"""
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não configurada no arquivo .env")

engine = create_engine(
    DATABASE_URL,
    echo=True,  # Mostra queries SQL no console (útil para debug)
    pool_pre_ping=True,  # Verifica conexões antes de usar
)

def create_db_and_tables() -> None:
    """
    Cria todas as tabelas no banco de dados.
    Só cria se não existirem (não apaga dados existentes).
    
    IMPORTANTE: Importar os models aqui para que o SQLModel os reconheça.
    """
    # Importar models para registrar no metadata
    from models.client_model import ClienteModel
    from models.stock_model import StockModel
    
    SQLModel.metadata.create_all(engine)
    print("✅ Tabelas criadas/verificadas com sucesso!")

def get_session():
    """
    Dependency para obter sessão do banco.
    Usado nas rotas FastAPI com Depends(get_session).
    
    Yields:
        Session: Sessão do SQLModel para interagir com o banco
    """
    with Session(engine) as session:
        yield session