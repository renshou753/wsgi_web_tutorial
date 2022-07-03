# 框架

成熟的 web 框架还需要下面几部分。

1 对 environ 做一些预处理，把 request 暴露出来供应用开发者调用。在一部分 wsgi 框架中 request 被直接注入到路由函数当中。

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
```

而像 flask 和 bottle 类似的框架，request 是一个线程安全的全局变量，需要主动引入。

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```

2 对 response 对象做一些封装以方便应用端返回结果，WSGI 服务端要求每次返回结果时一定要调用服务端发来的 start_response 对象。这很麻烦，框架可以实现一些封装，把这部分逻辑隐藏掉，比如 flaks 提供了一个 Response 对象。

```python
def index():
   response = Response("Unicorns are OK")
   response.headers['X-Parachutes'] = 'parachutes are cool'
   response.set_cookie('username', 'the username')
   return response
```

3 提供更方便的路由处理方法，框架需要处理浏览器发来的查询参数，比如 http://localhost:8080/orders?confirmed=true&processor=tony. 框架需要很方便地让应用开发者查询的到 confirmed 参数和 processor 参数是什么。

4 cookie，session 处理能力。

5 某些框架还提供了 html template 的功能，比如 flask 里集成的 jinja。在前后分离的 web 开发浪潮中 template 不是后端框架必须提供的。

6 还可以添加 orm 抽象层去处理数据库增删改查，比如 Django ORM。
