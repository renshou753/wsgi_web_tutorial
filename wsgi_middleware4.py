from wsgiref.simple_server import make_server


def reverse_return(handler):
    """reverse return"""

    def _inner(environ, start_function):
        response = handler(environ, start_function)
        reverse = [x[::-1] for x in response]
        return reverse

    return _inner


@reverse_return
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    # HTTP Headers
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"Hello World"]


# this will show "Hello World!" in your browser,
# and use middleware to reverse return response


httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")
# Serve until process is killed
httpd.serve_forever()
