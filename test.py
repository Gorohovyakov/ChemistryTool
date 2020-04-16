from ChemistryTool import *


if __name__ == "__main__":
    m = Molecule()
    m.add_atom("C", 1)
    m.add_atom("C", 2)
    m.add_atom("C", 3)
    m.add_bond(1, 2, 1)
    m.add_bond(3, 1, 1)
    print(m)
    print(repr(m))

