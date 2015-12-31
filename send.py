import socket

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
    '*2\r\n$3\r\nINCR\r\n$16\r\nWatch this space\r\n'
    """
    strings = ['INCR', key]
    l = [ make_string(s) for s in strings ]
    return make_array(l)

def send_command(host, key):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 6379))
    msg = craft_string(key)
    s.send(msg)
    s.close()

if __name__ == '__main__':
    send_command('127.0.0.1', 'To advertise here, call 1-800 RED SPAM')
