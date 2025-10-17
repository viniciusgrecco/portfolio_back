# repositories/base_repository.py
from typing import Generic, TypeVar, Type, List, Optional
from sqlmodel import SQLModel, select
from sqlmodel import Session

T = TypeVar("T", bound=SQLModel)

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def add(self, obj: T) -> T:
        """Adiciona e salva um objeto (commit + refresh)."""
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def get(self, id: int) -> Optional[T]:
        """Recupera por id (ou None)."""
        return self.session.get(self.model, id)

    def list(self, offset: int = 0, limit: int = 100) -> List[T]:
        """Lista objetos com paginação simples."""
        statement = select(self.model).offset(offset).limit(limit)
        results = self.session.exec(statement)
        return results.all()

    def update(self, obj: T) -> T:
        """
        Para SQLModel, normalmente basta merge/commit.
        Assume que 'obj' já tem primary key e está anexado ou é um objeto sincronizável.
        """
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def delete(self, obj: T) -> None:
        """Deleta um objeto."""
        self.session.delete(obj)
        self.session.commit()
