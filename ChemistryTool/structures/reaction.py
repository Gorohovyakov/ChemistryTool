from .abc import ReactionABC, MoleculeListABC
from .molecule import Molecule


class MoleculeList(MoleculeListABC):
    def insert(self, i, molecule):
        if isinstance(molecule, Molecule):
            self._data.insert(i, molecule)
        else:
            raise TypeError('Only Molecule acceptable')

    def __getitem__(self, i):
        if isinstance(i, slice):
            ml = object.__new__(MoleculeList)
            ml._data = self._data[i]
            return ml
        return self._data[i]

    def __setitem__(self, i, molecule):
        # переделать
        if isinstance(i, slice):
            # проверка все mol, Mol
            if all(isinstance(mol, Molecule) for mol in molecule):
                self._data[i] = molecule
        elif isinstance(molecule, Molecule):
            self._data[i] = molecule
        else:
            raise TypeError('Only Molecule acceptable')

class Reaction(ReactionABC):
    def __init__(self):
        self._reactants = MoleculeList()
        self._products = MoleculeList()

    @property
    def reactants(self):
        return self._reactants

    @property
    def products(self):
        return self._products

    def __repr__(self):
        return f"({list(self.reactants)}, {list(self.products)})"

    def __str__(self):
        return f"Reactants: {list(self.reactants)}\nProducts: {list(self.products)}"


__all__ = ['Reaction']
