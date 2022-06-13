# 你好 WSGI 应用

下面我们尝试创建一个最小化的 WSGI 应用。

一个 WSGI 应用是一个可以被 request 触发的 python 可调用对象(实现了\_\_call\_\_魔法函数，类、函数都可以)，该对象需接受两个参数， environ 和 start_response。

Environ 是一个 python 字典，包含了[CGI 环境变量](https://peps.python.org/pep-0333/#environ-variables)的信息。start_response 是一个回调函数，接受两个参数 status 和 headers，对应了 http 协议的状态码和 http headers。

Environ 和 start_response 回调函数都是由 WSGI 服务端传递到应用端的，WSGI 服务器决定环境变量该如何设置，start_response 该怎么实现。WSGI 应用端仅仅是接受它们，然后生成状态码和 headers，最后经由 start_response 函数返回结果。

```python
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    # HTTP Headers
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    return [b"Hello World"]
```

### 运行 WSGI 应用

为了运行上面这个迷你 WSGI 应用，我们需要一个 WSGI 服务器，当然 gunicorn，uwsgi 这些生产型服务器都是可以满足要求的，但我们这里为了简便，仅仅使用 python 标准库自带的一个简易 WSGI 测试服务器。

```python
from wsgiref.simple_server import make_server

def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    # HTTP Headers
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    return [b"Hello World"]

httpd = make_server('', 8000, app)
print("Serving on port 8000...")
# Serve until process is killed
httpd.serve_forever()
```
