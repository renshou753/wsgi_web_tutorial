import re

from wsgiref.simple_server import make_server


def not_found(environ, start_response):
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return [b'404 Not Found']


def index(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Index!\n"]


def hello(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Hello World!\n"]


def greet_user(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    user = environ.get('USER')
    # response must contain bytes
    return ["Welcome {}!\n".format(user).encode()]


urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)/$', greet_user),
]


def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        print(path)
        if match:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)

    return not_found(environ, start_response)


httpd = make_server('', 8000, application)
print("Serving on port 8000...")
# Serve until process is killed
httpd.serve_forever()
