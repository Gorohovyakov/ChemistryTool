from collections import Counter
from .abc import MoleculeABC
from ..algorithms import Isomorphism
from ..periodictable import *


class Molecule(Isomorphism, MoleculeABC):
    """Создаем пустой объект Molecule"""

    def add_atom(self, element: Element, number: int):
        """Добавляем атомы и их номер.
        Если атом с таким номером уже есть - ошибка
        """
        if not isinstance(number, int):
            raise TypeError("Key must be a number")
        elif not isinstance(element, Element):
            raise TypeError("Not an atom")
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

    def get_atom(self, number: int) -> Element:
        """
        возвращает эллемент по номеру атома
        """
        try:
            return self._atoms[number]
        except KeyError as e:
            raise KeyError("Atom not exist")

    def get_bond(self, start_atom: int, end_atom: int) -> int:
        """
        возвращает кратность связи между двумя атомами
        """
        try:
            return self._bonds[start_atom][end_atom]
        except KeyError as e:
            raise KeyError("Atom or Bond not exist")

    def delete_atom(self, number: int):
        """
        удаление атома и его связей
        """
        try:
            del self._atoms[number]
            # удаляем значения по ключу
            for i in self._bonds.pop(number):
                del self._bonds[i][number]
        except KeyError as e:
            raise KeyError("Atom not exist")

    def delete_bond(self, start_atom: int, end_atom: int):
        """
        удаление связи между атомами
        """
        try:
            del self._bonds[end_atom][start_atom]
            del self._bonds[start_atom][end_atom]
        except KeyError as e:
            raise KeyError("Bond not exist")

    def update_atom(self, element: Element, number: int):
        """
        Замена атома на другой
        """
        try:
            # isinstance(element, Element)?
            self._atoms[number] = element
        except KeyError:
            raise KeyError("Index not exist")

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        """
        изменение кратности связи
        """
        try:
            if isinstance(bond_type, int):
                raise TypeError("Bond type must be an integer")
            elif bond_type == self._bonds[end_atom][start_atom]:
                return None
            else:
                self._bonds[end_atom][start_atom] = self._bonds[start_atom][end_atom] = bond_type
        except KeyError:
            raise KeyError("Bond not exist")

    def __enter__(self):
        """
        Контекст менеджер. сохранение молекулы до изменений
        """
        self._backup_atoms = self._atoms.copy()
        self._backup_bonds = {k: v.copy() for k, v in self._bonds.items()}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._atoms = self._backup_atoms.copy()
            self._bonds = {k: v.copy() for k, v in self._backup_bonds.items()}
        del self._backup_atoms
        del self._backup_bonds


    def __str__(self):
        """
        брутто-формула
        """
        return "".join([str(k)+str(v) for k, v in Counter(self._atoms.values()).items()])

    def __repr__(self):
        return f"{self._atoms.values()}"


__all__ = ['Molecule']
