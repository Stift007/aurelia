class Blueprint:
    """
    Blueprints work like subclasses of an Aurelia-Instance.

    You can call a Blueprint by using
    >>> app.url_for("path")

    Using Blueprints:


    >>> def bp_route(request):
    >>>     return "Hello"
    >>> blueprint = make_blueprint(subindex="/sub")
    >>> blueprint.add_route("/",bp_route)
    >>> app.register_blueprint(blueprint)

    Here's a practical Example:

    >>> from second_app import app
    >>> blueprint = make_blueprint(subindex="/test")
    >>> blueprint.from_object(app)
    >>> app.register_blueprint(blueprint)
    """
    def __init__(self,**kwds):
        self.url_root = kwds.get("subindex","/blue")
        self.routes = []

    def add_route(self,rule,function,methods=["GET"]):
        self.routes.append((rule, function, methods))

    def from_object(self,aur: "Aurelia"):
        """
        Load an Aurelia Object's Routes into the Blueprint
        """
        for r in aur.routes:
            self.add_route(r[0],aur.views[r[1]])

class Aurelia:
    def __init__(self):
        self.routes = []
        self.views = {}
        self.on_before_request = None

    def register_route(self,rule,route_name):
        self.routes.append((rule,route_name))

    def add_view(self,function,route_name):
        self.views[route_name] = function

    def register_blueprint(self,bp:Blueprint):
        for r in bp.routes:
            route_rule = r[0]
            function = r[1]
            route_name = function.__name__
            print(route_rule)
            print(bp.url_root)
            self.register_route(bp.url_root+route_rule, route_name)
            self.add_view(function, route_name)

    def view(self,path):
        def predicate(function):
            route_name = function.__name__
            self.register_route(path,route_name)
            self.add_view(function,route_name)

        return predicate

    def set_before_request(self,requesthandle):
        self.on_before_request = requesthandle

def make_blueprint(**kwargs):
    
    """
    Blueprints work like subclasses of an Aurelia-Instance.

    You can call a Blueprint by using
    >>> app.url_for("path")

    Using Blueprints:


    >>> def bp_route(request):
    >>>     return "Hello"
    >>> blueprint = make_blueprint(subindex="/sub")
    >>> blueprint.add_route("/",bp_route)
    >>> app.register_blueprint(blueprint)

    Here's a practical Example:

    >>> from second_app import app
    >>> blueprint = make_blueprint(subindex="/test")
    >>> blueprint.from_object(app)
    >>> app.register_blueprint(blueprint)
    """
    return Blueprint(**kwargs)