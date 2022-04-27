class Aurelia:
    def __init__(self):
        self.routes = []
        self.views = {}

    def register_route(self,rule,route_name):
        self.routes.append((rule,route_name))

    def add_view(self,function,route_name):
        self.views[route_name] = function

    def view(self,path):
        def predicate(function):
            route_name = function.__name__
            self.register_route(path,route_name)
            self.add_view(function,route_name)

        return predicate
