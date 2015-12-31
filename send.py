import random
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
    try:
        s.connect((host, 6379))
    except socket.error:
        return False
    msg = craft_string(key)
    s.send(msg)
    s.close()
    return True

def get_random_ip():
    quad = [ str(random.randint(0, 255)) for i in [1, 2, 3, 4] ]
    return ".".join(quad)

def send_message(msg):
    addr = get_random_ip()
    r = send_command(addr, msg)
    status = 'Success' if r else 'Failure'
    print '%s : %s' % (addr, status)

if __name__ == '__main__':
    for x in range(1000):
        send_message('YOUR MESSAGE HERE. redispam@gmail.com')
