from .element import Element


class C(Element):
    _element = "C"

    def __repr__(self):
        return f"{C._element}"


__all__ = ['C']
