from .response import Response

class HTML:
    def __init__(self,*html) -> None:
        self.html = html

    def __repr__(self):
        return Response(self.html,mimetype="text/html")

    @classmethod
    def render_file(cls, filename):
        return cls(open(filename).read())
