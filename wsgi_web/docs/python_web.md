# Python web 框架

2000 年后 python web 应用框架逐渐涌现，当时比较流行的 web 应用框架有 twisted, Zope 等等。这些框架并没有统一的标准，导致 web 服务器要做不同的适配才能接入这些框架，繁琐的配置限制了 python web 开发的发展，通常情况下这些 web 框架只能在 CGI，FASTCGI，mod_python 之间做取舍。

### WSGI

WSGI (Web Server Gateway Interface) 是作为 Web 服务器与 Web 应用程序或应用框架之间的一种接口，以提升 python web 开发的可移植性。

WSGI 协议被定义在 [PEP333](https://peps.python.org/pep-0333) 当中，有兴趣的小伙伴可以详细阅读。
