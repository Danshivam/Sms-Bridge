from datetime import datetime, date, timedelta


def format_timestamp(timestamp: int) -> str:

    dt = datetime.fromtimestamp(timestamp / 1000)

    return dt.strftime("%I:%M %p")



def get_date_group(timestamp: int) -> str:

    message_date = datetime.fromtimestamp(timestamp / 1000).date()

    today = date.today()
    yesterday = today - timedelta(days=1)

    if message_date == today:
        return "Today"

    if message_date == yesterday:
        return "Yesterday"

    return message_date.strftime("%B %d, %Y")