from datetime import datetime


def get_data(request):
    return {'date': datetime.now()}
