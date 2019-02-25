#
# General utility functions
#

def tokenize(instr, delims):
    """
    Takes a string as input and splits into tokens using any character
    in delim to split.
    
    >>> tokenize('test,string', ',')
    ['test', 'string']
    >>> tokenize('test => string (1,2)', '=>(,)')
    ['test', 'string', '1', '2']
    """

    tokstr = instr
    for ch in delims:
        tokstr = tokstr.replace(ch, ' ')

    return tokstr.split()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
