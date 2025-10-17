"""
API de Gestão de Investimentos
Desenvolvida com FastAPI, SQLModel e MySQL
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_db_and_tables
import os
import glob
from importlib import import_module

# Inicializar FastAPI com metadados para documentação
app = FastAPI(
    title="API de Gestão de Investimentos",
    description="""
    API RESTful para gerenciar clientes investidores e suas ações (stocks).
    
    ## Funcionalidades
    
    * **Clientes**: Gerenciamento completo de clientes investidores
    * **Stocks**: Gerenciamento completo de ações compradas
    
    ## Perfis de Investidor
    
    * **Conservador**: Perfil mais conservador, prefere investimentos de baixo risco
    * **Moderado**: Perfil equilibrado entre risco e retorno
    * **Agressivo**: Perfil mais agressivo, busca maiores retornos
    
    ## Mercados Suportados
    
    * **NASDAQ**: Mercado americano
    * **IBOV**: Índice Bovespa (mercado brasileiro)
    """,
    version="1.0.0",
    contact={
        "name": "Seu Nome",
        "email": "seu.email@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://portfolio-front-eta-five.vercel.app"
        "http://localhost:8501",
        "http://localhost:5173",
        "http://localhost:8080",
        "http://localhost:3000"
        # Adicionar dominio apos deploy do front-end
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criar tabelas na inicialização
@app.on_event("startup")
def on_startup():
    """Executado ao iniciar a aplicação"""
    print("🚀 Iniciando API de Investimentos...")
    create_db_and_tables()
    print("✅ API pronta para uso!")

# Auto-carregar routers dos use_cases
working_directory = os.path.dirname(os.path.abspath(__file__))
use_cases_directory = os.path.join(working_directory, "use_cases")
routes = glob.glob(os.path.join(use_cases_directory, "**/index.py"), recursive=True)

print("\n📂 Carregando rotas...")
for route in routes:
    relative_path = os.path.relpath(route, working_directory)
    module_name = os.path.splitext(relative_path)[0].replace(os.path.sep, '.')

    try:
        module = import_module(module_name)
        if hasattr(module, 'router'):
            app.include_router(module.router)
            print(f"   ✅ {module_name}")
    except Exception as e:
        print(f"   ❌ Erro ao carregar {module_name}: {e}")

print("\n")

@app.get(
    "/",
    tags=["Root"],
    summary="Endpoint raiz",
    description="Retorna informações básicas sobre a API"
)
def root():
    """
    Endpoint raiz da API.
    
    Retorna informações sobre a API e links úteis.
    """
    return {
        "message": "API de Gestão de Investimentos",
        "version": "1.0.0",
        "status": "online",
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "clientes": "/clientes",
            "stocks": "/stocks"
        }
    }

@app.get(
    "/health",
    tags=["Health"],
    summary="Health check",
    description="Verifica se a API está funcionando"
)
def health_check():
    """
    Endpoint para health check.
    
    Útil para monitoramento e verificação de disponibilidade.
    """
    return {"status": "healthy"}