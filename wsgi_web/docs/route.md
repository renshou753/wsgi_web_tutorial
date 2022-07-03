# 路由

路由是 web 框架最核心的功能之一，另外一个是 request->response 处理，路由允许浏览器调用服务端代码中的不同部分。

### PATH_INFO

WSGI 服务端把浏览器索要的路径信息记录在了 PATH_INFO 这个变量中并听过 environ 传递给 WSGI 应用端。

下面的伪代码通过无限的 if else 嵌套把所有需要处理的逻辑返回给浏览器。

```python
def giant_wsgi_case_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    # HTTP Headers
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    # The returned object is going to be printed
    if environ['PATH_INFO'] == '/hello':
        return [b"Hello World"]
    elif environ['PATH_INFO'] == '/bye':
        return [b"Good bye"]
    elif ...
         ...
    else:
        start_response('404 Not Found', headers)
        return [b"Not found"]
```

这是最原始的路由处理方法，当然几乎没有任何 web 框架会真的这么处理路由。

### WSGI 框架路由

我们可以用一个 python 字典去代替繁琐的 if else，许多 wsgi 框架会有一个类似字典的 Mapping 类型。比如 django 可以把路由表放在 urls.py 中，并用正则表达式和可调用的 view 做匹配去响应浏览器的请求。

```python
from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    ...
    ]
```

另一个 wsgi 框架 pyramid 采用了类似的方法。

```python
with Configurator() as config:
     config.add_route('hello', '/hello/{name}')
     config.add_view(hello_world, route_name='hello')
     app = config.make_wsgi_app()
```

add_route 把 route_name 和路由的路径模式联系在一起，add_view 把业务处理函数(hello_world)和 route_name 联系在一起。这样当浏览器访问/hello/{name}路径是 hello_world 函数就会被触发。

flask 和 bottle 申明路由的方式相比就不大一样, flask 首先创造了通过装饰器申明路由的方式。下面的代码直接把路由路径“/”和处理函数 hello 联系在了一起，当浏览器访问“/”路径时 hello 函数会被直接调用。

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```
