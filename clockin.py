from datetime import datetime


def start_work():
    print('Starting work...')
    start_time = datetime.now()
    input('Press enter to end work... ')

    end_time = datetime.now()
    work_duration = end_time - start_time
    raw_seconds = work_duration.seconds
    hours = raw_seconds//3600
    minutes = (raw_seconds//60) % 60

    if hours == 0 and minutes == 0:
        formatted_length = None
    elif hours == 0:
        if minutes == 1:
            formatted_length = str(minutes) + ' minute'
        else:
            formatted_length = str(minutes) + ' minutes'
    elif minutes == 0:
        if hours == 1:
            formatted_length = str(hours) + ' hour'
        else:
            formatted_length = str(hours) + ' hours'
    else:
        if hours == 1 and minutes == 1:
            formatted_length = str(hours) + ' hour ' + str(minutes) + ' minute'
        elif hours == 1:
            formatted_length = str(hours) + ' hour ' + str(minutes) + ' minutes'
        elif minutes == 1:
            formatted_length = str(hours) + ' hours ' + str(minutes) + ' minute'
        else:
            formatted_length = str(hours) + ' hours ' + str(minutes) + ' minutes'

    if formatted_length is not None:
        print('Length of work: ' + formatted_length)
    else:
        print('Length of work less than 1 minute...')


if __name__ == "__main__":
    start_work()
