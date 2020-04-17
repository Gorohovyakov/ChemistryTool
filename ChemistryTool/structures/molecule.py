from .abc import MoleculeABC
from ..algorithms import Isomorphism


<<<<<<< HEAD
atom_set = {'C', 'O', 'N'}  # минимальный набор органика


class Molecule(Isomorphism, MoleculeABC):
    """Создаем пустой объект Molecule"""

    def add_atom(self, element: str, number: int):
        """Добавляем атомы и их номер.
        Если атом с таким номером уже есть - ошибка
        """
        if element not in atom_set:
            raise ValueError("Not an atom")
        elif number in self._atoms:
            raise KeyError("Atom is already in the graph")
        else:
            self._atoms[number] = element
            self._bonds[number] = {}

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        """Добавляем связь между атомами еще не связанными
        иначе - ошибка.
        """
        # если и только если они есть в atoms
        if start_atom in self._atoms and end_atom in self._atoms:
            # замыкание
            if start_atom == end_atom:
                raise ValueError("The closure of a graph")
            # связь уже есть
            elif end_atom in self._bonds[start_atom]:
                raise KeyError("Bond exist")
            # новая связь
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[end_atom][start_atom] = bond_type
        else:
            raise KeyError("Atom not exist")

    def __str__(self):
        return f"Atoms: {self._atoms}\nBonds: {self._bonds}"

    def __repr__(self):
        return f"({self._atoms}, {self._bonds})"


__all__ = ["Molecule"]
=======
class Molecule(Isomorphism, MoleculeABC):
    def add_atom(self, element: str, number: int):
        ...

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        ...


__all__ = ['Molecule']
>>>>>>> master
