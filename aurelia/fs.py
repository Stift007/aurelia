from response import Response


def send_file(filename):
    return Response(open(filename,"rb").read(),mimetype="application/x-www-urlformencoded")
