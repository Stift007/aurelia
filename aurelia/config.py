import typing

class Aurelia:
    def __init__(self):
        self.routes = []
        self.views = {}
        self.methods = {}

    def register_route(self,rule,route_name,methods:typing.List[str]=["GET"]):
        self.routes.append((rule,route_name))
        self.methods[route_name] = methods

    def add_view(self,function,route_name):
        self.views[route_name] = function

    def view(self,path,**kwds):
        def predicate(function):
            route_name = function.__name__
            self.register_route(path,route_name)
            self.add_view(function,route_name)
            self.methods[route_name] = kwds.get("request_method",["GET"])

        return predicate
