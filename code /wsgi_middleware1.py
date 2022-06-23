from wsgiref.simple_server import make_server


def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    # HTTP Headers
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"Hello World"]


def log_environ(handler):
    """print the envrionment dictionary to the console"""
    from pprint import pprint

    def _inner(environ, start_function):
        pprint(environ)
        return handler(environ, start_function)

    return _inner


# this will show "Hello World!" in your browser,
# and the environment in the console
app = log_environ(hello_world_app)


httpd = make_server('', 8001, app)
print("Serving on port 8001...")
# Serve until process is killed
httpd.serve_forever()
