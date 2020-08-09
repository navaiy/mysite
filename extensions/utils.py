from . import jalali
from django.utils import timezone


def jalali_convert_dt(time):
    time = timezone.localtime(time)
    time_to_str = '{},{},{}'.format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    output = '{}/{}/{} ساعت {}:{}'.format(
        time_to_tuple[0],
        time_to_tuple[1],
        time_to_tuple[2],
        time.hour,
        time.minute,
    )
    return output


def jalali_convert_d(time):
    time = timezone.localtime(time)
    time_to_str = '{},{},{}'.format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    output = '{}/{}/{}'.format(
        time_to_tuple[0],
        time_to_tuple[1],
        time_to_tuple[2],
    )
    return output
