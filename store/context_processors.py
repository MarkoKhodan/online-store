import datetime


def get_current_datetime_to_context(request):
    current_datetime = datetime.datetime.now()
    return {
        'current_date': current_datetime.date,
        'current_time': current_datetime.time

    }