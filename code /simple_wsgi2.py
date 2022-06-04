from wsgiref.simple_server import make_server


class HelloWSGI:

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        self.start('200 OK', [('Content-Type', 'text/plain')])
        yield b"Hello World!\n"


httpd = make_server('', 8000, HelloWSGI)
print("Serving on port 8000...")
# Serve until process is killed
httpd.serve_forever()
