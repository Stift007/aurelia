from typing import List
import mimetypes

class Response:
    def __init__(self,*body,mimetype="text/plain",status:int=200,headers=[]) -> None:
        self.body = " ".join(body) if isinstance(body[0], str) else body
        self.mimetype = mimetype
        self.status = status
        self.headers = headers

def _endpoint(blueprint):
    if hasattr(blueprint,"__endpoint__"):
        return blueprint.__endpoint__
    return blueprint

def redirect(blueprint,status):
    return Response("",status=status,headers=[("refresh",_endpoint(blueprint))])


class FileResponse(Response):
    def __init__(self, fp, status: int = 200, headers=[]) -> None:
        super().__init__(open(fp,"rb").read(),mimetype=mimetypes.guess_type(fp),status=status, headers=headers)
