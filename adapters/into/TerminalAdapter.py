from model import UserQuery
from ports.into.UserQuery import UserQueryPort


class TerminalAdapter(UserQueryPort):
    def ask(self, query: UserQuery):
        pass