import re
from pygments.lexer import RegexLexer, words
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
    name_class = r'[A-Z]\w*'
    name_module = r'[a-z0-9_]*'

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
            (r'\$[0-9a-f]+', Number.Hex),
            (r'(?:(?:(:)?([ \t]*)(:?%s|([+\-*/&|~]))|Or|And|Not|[=<>^]))', Operator),
            (r'[\[\]]', Punctuation),
            (r'\%[10]+', Number.Bin),
            (r'(?i)\b(?:null|true|false)\b', Name.Builtin),
            # keywords
            (words(('function', 'while', 'for', 'end', 'do', 'if', 'then', 'return', 'new'), prefix=r'\b', suffix=r'\b'), Keyword.Reserved),
            (r'%s\b' % name_constant, Name.Constant),
            (r'%s\b' % name_function, Name.Function),
            (r'%s\b' % name_variable, Name.Variable),
       ],
       'variables': [
            (r'%s\b' % name_constant, Name.Constant),
            (r'%s\b' % name_variable, Name.Variable),
            (r'\s+', Text),
       ]
    }
