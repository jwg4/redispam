def make_string(s):
    r"""
    >>> make_string('asdf')
    '$4\r\nasdf\r\n'
    """
    return '$%d\r\n%s\r\n' % (len(s), s)

def make_array(l):
    r"""
    >>> make_array(['+asdf\r\n'])
    '*1\r\n+asdf\r\n'
    """
    return ('*%d\r\n' % len(l)) + ''.join(l)

def craft_string(key):
    r"""
    >>> craft_string('Watch this space')
    '*2\r\n$3\r\nINC\r\n$16\r\nWatch this space\r\n'
    """
    strings = []
    l = [ make_string(s) for s in strings ]
    return make_array(l)
