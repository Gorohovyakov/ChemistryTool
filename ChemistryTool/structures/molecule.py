from .abc import MoleculeABC
from ..algorithms import Isomorphism


class Molecule(Isomorphism, MoleculeABC):
    def add_atom(self, element: str, number: int):
        ...

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        ...


__all__ = ['Molecule']
