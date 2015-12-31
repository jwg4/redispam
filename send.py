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
    strings = []
    l = [ make_string(s) for s in strings ]
    return make_array(l)
