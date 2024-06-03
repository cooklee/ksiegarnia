from datetime import datetime


def timee(request):
    return {'time':datetime.now() }