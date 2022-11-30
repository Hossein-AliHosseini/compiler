from enum import Enum


class TokenTypes(Enum):
    NUMBER = {
        'name': 'NUMBER'
    }
    ID = {
        'name': 'ID'
    }
    KEYWORD = {
        'name': 'KEYWORD'
    }
    SYMBOL = {
        'name': 'SYMBOL'
    }
    COMMENT = {
        'name': 'COMMENT'
    }
    WHITESPACE = {
        'name': 'WHITESPACE'
    }
