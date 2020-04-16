from ChemistryTool import *


if __name__ == "__main__":
    m1 = Molecule()
    m1.add_atom("C", 1)
    m1.add_atom("C", 2)
    m1.add_atom("C", 3)
    m1.add_bond(1, 2, 1)
    m1.add_bond(3, 1, 1)
    m1.add_bond(2, 3, 1)

    m2 = Molecule()
    m2.add_atom("C", 1)
    m2.add_atom("C", 2)
    m2.add_atom("C", 3)
    m2.add_bond(1, 2, 1)
    m2.add_bond(3, 1, 1)

    m3 = Molecule()
    m3.add_atom("C", 1)
    m3.add_atom("O", 2)
    m3.add_atom("C", 3)
    m3.add_bond(1, 2, 1)
    m3.add_bond(3, 1, 1)

    r = Reaction()
    r.products.append(m1)
    r.products.append(m2)
    r.products[:2] = m2, m3
    r.products[1] = m3
    # print(m1)
    print(repr(m1))
    print(repr(r))
    # repr(m3)
    # print(m3)
    # print(r)



#     a = [1, 2, 3, 4]
#     a[:2] = [6, 5]
# print("f", a)







