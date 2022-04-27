class Response:
    def __init__(self,*body,mimetype="text/plain",status:int=200,headers=[]) -> None:
        self.body = " ".join(body)
        self.mimetype = mimetype
        self.status = status
        self.headers = headers
