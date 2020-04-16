from .abc import MoleculeABC
from ..algorithms import Isomorphism


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

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        """Добавляем связь между атомами еще не связанными
        иначе - ошибка.
        """
        if len(self._atoms) < 2:
            raise IndexError("At least 2 atoms are needed")
        # Проверка уже имеющихся связей
        elif start_atom in self._bonds and end_atom in self._bonds[start_atom]:
            raise KeyError("Bond exist")
        # замыкание
        elif start_atom == end_atom:
            raise ValueError("The closure of a graph")
        # если и только если они есть в atoms
        if start_atom in self._atoms and end_atom in self._atoms:
            # связь уже была у обоих
            if start_atom in self._bonds and end_atom in self._bonds:
                self._bonds[start_atom][end_atom] = bond_type
                self._bonds[end_atom][start_atom] = bond_type
            # новая связь
            else:
                # Обработка случя с циклом
                try:
                    self._bonds[start_atom][end_atom] = bond_type
                except KeyError:
                    self._bonds[start_atom] = {end_atom: bond_type}
                try:
                    self._bonds[end_atom][start_atom] = bond_type
                except KeyError:
                    self._bonds[end_atom] = {start_atom: bond_type}
        # в atoms их нет
        else:
            raise KeyError("Atom not exist")

    def __str__(self):
        return f"Atoms: {self._atoms}\nBonds: {self._bonds}"

    def __repr__(self):
        return f"({self._atoms}, {self._bonds})"


__all__ = ["Molecule"]
