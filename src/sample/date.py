from datetime import datetime
def format_date():
    print(datetime.now())
    unformatted_time =datetime.now()
    formatted_time= unformatted_time.strftime("%Y%m%d%H%M%S")
    print(formatted_time, "this is formatted time")
    return formatted_time
