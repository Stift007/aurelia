# Aurelia
Aurelia is a lightweight Python web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications while being as lightweight as possible. 

Aurelia doesn't enforce any dependencies or project layout. it's based off Python's SocketServer and HTTP Module, which are built-in with Python.  

Using an easy Routing System, you can create epic Websites in Minutes and while this Framework might not be as advanced as Flask or Pyramid, it's lightweight,  
comes with no Dependencies and is simple to understand.  

## Installation
Installation via pip:

    $ pip install -U git+https://github.com/Stift007/aurelia
    
Or via Polyp:

    $ polyp i Stift007.aurelia


## Quickstart

```python3
from aurelia.config import Aurelia
from aurelia import run_server, HTML
from aurelia.response import Response
from aurelia.fs import send_file

def helloworld(request):
    return Response("Hello World!", mimetype="text/plain")

app = Aurelia()

app.register_route("/","ping")
app.add_view(helloworld,"ping")

@app.view("/file")
def sendmeafile(request):
    return send_file("fs.py")

@app.view("/2")
def second(request):
    return "Welcome to Aurelia!"

@app.view("/3")
def three(request):
    return HTML.render_file("index.html")
    
run_server("127.0.0.1",80,config=app)
```
