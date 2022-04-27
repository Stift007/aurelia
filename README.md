# Aurelia
Python Web Framework for creating awesome websites

## Quickstart

```python3
from aurelia.config import Aurelia
from aurelia import run
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

run("127.0.0.1",80,config=app)
```
