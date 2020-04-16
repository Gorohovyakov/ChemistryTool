from abc import ABC, abstractmethod
from ...algorithms import IsomorphismABC


class MoleculeABC(IsomorphismABC, ABC):
    def __init__(self):
        self._atoms = {}
        self._bonds = {}

    @abstractmethod
    def add_atom(self, element: str, number: int):
        ...

    @abstractmethod
    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        ...


__all__ = ['MoleculeABC']
