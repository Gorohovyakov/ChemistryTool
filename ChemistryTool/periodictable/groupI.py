from .element import Element


class H(Element):
    _element = "H"

    def __repr__(self):
        return f"{H._element}"


__all__ = ['H']
