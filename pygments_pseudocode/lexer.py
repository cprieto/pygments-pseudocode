import re
from pygments.lexer import RegexLexer, words, default
from pygments.token import Text, String, Number, Keyword, Operator, Name, Punctuation


class PseudocodeLexer(RegexLexer):
    name = 'Pseudocode'
    aliases = ['pseudo', 'pseudocode', 'algorithm', 'algo']
    filenames = ['*.algo', '*.pseudo']
    mimetypes = ['text/x-algo']

    flags = re.MULTILINE | re.IGNORECASE

    name_variable = r'[a-z_]\w*'
    name_function = r'[A-Z]\w*'
    name_constant = r'[A-Z_][A-Z0-9_]*'

    tokens = {
       'root': [
            # Text
            (r'[ \t]+', Text),
            (r'\.\.\n', Text),
            # Data
            ('"', String.Double),
            # Numbers
            (r'[0-9]+\.[0-9]*(?!\.)', Number.Float),
            (r'\.[0-9]*(?!\.)', Number.Float),
            (r'[0-9]+', Number.Integer),
            (r'(?:(?:(:)?([ \t]*)(:?%s|([+\-*/&|~]))|or|and|not|[=<>^]))', Operator),
            (r'[(){}!#,.:\[\]]', Punctuation),
            (r'(?i)\b(?:null|true|false)\b', Name.Builtin),
            # keywords
            (words(('function', 'while', 'for', 'end', 'do', 'if', 'then', 'return', 'new'), prefix=r'\b', suffix=r'\b'), Keyword.Reserved),
            (r'%s\b' % name_constant, Name.Constant),
            (r'%s\b' % name_function, Name.Function),
            (r'%s\b' % name_variable, Name.Variable),
       ],
       'funcname': [
            (r'(?i)%s\b' % name_function, Name.Function),
            (r'\s+', Text),
            (r'\(', Punctuation, 'variables'),
            (r'\)', Punctuation, '#pop')
        ],
       'variables': [
            (r'%s\b' % name_constant, Name.Constant),
            (r'%s\b' % name_variable, Name.Variable),
            (r'\s+', Text),
            (r',', Punctuation, '#push'),
            default('#pop')
        ],
    }
