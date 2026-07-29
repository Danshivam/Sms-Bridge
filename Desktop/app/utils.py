from datetime import datetime


def format_timestamp(timestamp: int) -> str:

    dt = datetime.fromtimestamp(timestamp / 1000)

    return dt.strftime("%I:%M %p")