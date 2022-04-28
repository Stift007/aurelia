from response import FileResponse


def send_file(filename):
    return FileResponse(filename)
