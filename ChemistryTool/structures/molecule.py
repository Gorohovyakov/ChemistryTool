from .abc import MoleculeABC
from ..algorithms import Isomorphism
from collections import Counter
from ..periodictable import *


class Molecule(Isomorphism, MoleculeABC):
    """Создаем пустой объект Molecule"""

    def add_atom(self, element: Element, number: int):
        """Добавляем атомы и их номер.
        Если атом с таким номером уже есть - ошибка
        """
        if not isinstance(element, Element):
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

    def get_atom(self, number: int) -> Element:
        """
        возвращает эллемент по номеру атома
        """
        if number in self._atoms:
            return self._atoms[number]
        else:
            raise KeyError("Atom not exist")

    def get_bond(self, start_atom: int, end_atom: int) -> int:
        """
        возвращает кратность связи между двумя атомами
        """
        # переделать более красиво
        try:
            if start_atom in self._bonds[end_atom] and end_atom in self._bonds[start_atom]:
                return self._bonds[start_atom][end_atom]
            else:
                raise IndexError("Bond not exist")
        except KeyError:
            raise KeyError("Atom not exist")

    def delete_atom(self, number: int):
        """
        удаление атома и его связей
        """
        if number in self._atoms:
            del self._atoms[number]
            del self._bonds[number]
            for i in self._bonds.values():
                if number in i:
                    del i[number]
        else:
            raise KeyError("Atom not exist")

    def delete_bond(self, start_atom: int, end_atom: int):
        """
        удаление связи между атомами
        """
        if start_atom in self._bonds[end_atom] and end_atom in self._bonds[start_atom]:
            del self._bonds[end_atom][start_atom]
            del self._bonds[start_atom][end_atom]
        else:
            raise KeyError("Bond not exist")

    def update_atom(self, element: Element, number: int):
        """
        Замена атома на другой
        """
        if number not in self._atoms:
            raise KeyError("Atom not exist")
        elif element == self._atoms[number]:
            return None
        else:
            self._atoms[number] = element

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        """
        изменение кратности связи
        """
        if start_atom in self._bonds[end_atom] and end_atom in self._bonds[start_atom]:
            if bond_type == self._bonds[end_atom][start_atom]:
                return None
            else:
                self._bonds[end_atom][start_atom] = self._bonds[start_atom][end_atom] = bond_type
        else:
            raise KeyError("Bond not exist")

    def __enter__(self):
        """
        Контекст менеджер. сохранение молекулы до изменений
        """
        self._backup_atoms = {k: v for k, v in self._atoms.items()}
        self._backup_bonds = {k: v for k, v in self._bonds.items()}

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._atoms = {k: v for k, v in self._backup_atoms.items()}
            self._bonds = {k: v for k, v in self._backup_bonds.items()}

    def __str__(self):
        """
        брутто-формула вида: C2H6O
        """
        _valence = {"C": 4, "H": 1, "N": 3, "O": 2}
        if len(self._atoms) == 1:
            if self._atoms[1] == H():
                return "H2"
            mol_str = "{}{}".format(self._atoms[1], "H" + str(_valence[self._atoms[1]])) if self._atoms[1] != "O" \
                else "{}{}".format("H" + str(_valence[self._atoms[1]]), self._atoms[1])
            return mol_str

        mol = Counter()
        for atm in self._atoms.values():
            mol[atm.__str__()] += 1
        if H().__str__() not in mol:
            mol[H().__str__()] = 0

        tmp = 0
        for k, v in self._atoms.items():
            v = v.__str__()
            for g in self._bonds[k].values():
                tmp += g
            mol[H().__str__()] += _valence[v] - tmp
            tmp = 0
        return "".join(["{}{}".format(el, "" if mol[el] == 1 else mol[el]) for el in sorted(mol, key=lambda k: k.__str__())])

    def __repr__(self):
        return f"{self._atoms.values()}"


__all__ = ["Molecule"]
