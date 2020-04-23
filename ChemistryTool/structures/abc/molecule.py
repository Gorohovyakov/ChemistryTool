from abc import ABC, abstractmethod
from typing import Dict
from ...algorithms.abc import IsomorphismABC
from ...periodictable.element import Element


class MoleculeABC(IsomorphismABC, ABC):
    __slots__ = ('_atoms', '_bonds', '_charges', '_backup_atoms', '_backup_bonds')

    def __init__(self):
        self._atoms: Dict[int, Element] = {}
        self._bonds: Dict[int, Dict[int, int]] = {}
        self._charges: Dict[int, int] = {}

    @abstractmethod
    def get_atom(self, number: int) -> Element:
        ...

    @abstractmethod
    def get_bond(self, start_atom: int, end_atom: int) -> int:
        ...

    @abstractmethod
    def add_atom(self, element: Element, number: int, charge: int = 0):
        # todo:  element.attach(self, number)
        ...

    @abstractmethod
    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        ...

    @abstractmethod
    def delete_atom(self, number: int):
        ...

    @abstractmethod
    def delete_bond(self, start_atom: int, end_atom: int):
        ...

    @abstractmethod
    def update_atom(self, element: Element, number: int):
        ...

    @abstractmethod
    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        ...

    @abstractmethod
    def __enter__(self):
        ...

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    @abstractmethod
    def __str__(self):
        ...


__all__ = ['MoleculeABC']

