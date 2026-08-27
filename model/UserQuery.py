class UserQuery:
    def __init__(self, query: str):
        self._query = query

    @property
    def value(self) -> str:
        return self._value