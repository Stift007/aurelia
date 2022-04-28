import http
import http.server
import http.client
from math import inf
from _html import HTML
import response
from config import Aurelia

class Requesthandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            if self.aurel.on_before_request:
                self.aurel.on_before_request(self)
            rule, rname = self.find(lambda r:r[0] == self.path,self.aurel.routes)
            res = self.aurel.views[rname](self)
            if isinstance(res,HTML):
                res = res.__repr__()
                self.send_response(res.status)
                self.send_header("Content-Type", res.mimetype)
                for i in res.headers:
                    self.send_header(i[0],i[1])
                self.end_headers( )
                if isinstance(res.body,bytes):
                    self.wfile.write(res.body)
                else:
                    self.wfile.write(res.body.encode())
            elif isinstance(res,response.Response):
                self.send_response(res.status)
                self.send_header("Content-Type", res.mimetype)
                for i in res.headers:
                    self.send_header(i[0],i[1])
                self.end_headers( )
                if isinstance(res.body,bytes):
                    self.wfile.write(res.body)
                else:
                    self.wfile.write(res.body.encode())
            else:
                

                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers( )
                self.wfile.write(res.encode())
            
        except Exception as e:
            return self.wfile.write(str(e.with_traceback(e.__traceback__)).encode())

    def find(self,predicate,iterable):
        for i in iterable:
            if predicate(i): 
                return i
        return None

def run(host="127.0.0.1",port=5000,config:Aurelia=None):
    Handle = Requesthandler
    Handle.aurel = config
    with http.server.HTTPServer((host,port), Handle) as https:
        print(f"Running app '{__name__}' on http://{host}:{port}")        
        while True:
            https.handle_request()
