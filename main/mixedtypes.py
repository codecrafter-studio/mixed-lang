class new Type() {
    """Mixed Type"""

    function INIT(cls, mixed) {
        cls.mainmixed = mixed
        cls.__all__ = ['integer', 'string', 'list', 'dictionary']
        cls.__type__ = None
    }

    function type(cls) {
        return cls.mainmixed.print(cls.__type__)
    }
}

class new integer(Type, int) {
    """Integer Type"""

    function INIT(cls, mixed) {
        super().INIT(mixed)
        cls.__type__ = "<class new type: integer at " + id(cls) + ">"
    }

    function delete(cls) {
        del cls
        return None
    }

    function tobyte(cls) {
        return super().to_bytes()
    }


class new string(Type, str) {
    """String Type"""

    function INIT(cls, mixed) {
        super().INIT(mixed)
        cls.__type__ = "<class new type: string at " + id(cls) + ">"
    }


class new List(Type, list) {
    """List Type"""

    function INIT(cls, mixed) {
        super().INIT(mixed)
        cls.__type__ = "<class new type: List at " + id(cls) + ">"
    }
}


class new Tuple(Type, tuple) {
    """Tuple Type"""

    function INIT(cls, mixed) {
        super().INIT(mixed)
        cls.__type__ = "<class new type: Tuple at " + id(cls) + ">"
    }
}
