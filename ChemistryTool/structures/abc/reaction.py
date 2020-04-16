from abc import ABC, abstractmethod
from collections.abc import MutableSequence
from typing import Iterable, overload
from .molecule import MoleculeABC


class MoleculeListABC(MutableSequence):
    def __init__(self):
        self._data = []

    @abstractmethod
    def insert(self, i: int, molecule: MoleculeABC) -> None:
        pass

    @overload
    @abstractmethod
    def __getitem__(self, i: int) -> MoleculeABC: ...

    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> 'MoleculeListABC': ...

    @overload
    @abstractmethod
    def __setitem__(self, i: int, molecule: MoleculeABC) -> None: ...

    @overload
    @abstractmethod
    def __setitem__(self, s: slice, molecule: Iterable[MoleculeABC]) -> None: ...

    @overload
    @abstractmethod
    def __delitem__(self, i: int) -> None: ...

    @overload
    @abstractmethod
    def __delitem__(self, i: slice) -> None: ...

    def __delitem__(self, i):
        del self._data[i]

    def __len__(self) -> int:
        return len(self._data)


class ReactionABC(ABC):
    @abstractmethod
    def __init__(self):
        self._reactants: MoleculeListABC
        self._products: MoleculeListABC

    @property
    @abstractmethod
    def reactants(self) -> MoleculeListABC:
        """
        Reactants of reaction
        """

    @property
    @abstractmethod
    def products(self) -> MoleculeListABC:
        """
        Products of reaction
        """


__all__ = ['ReactionABC', 'MoleculeListABC']
