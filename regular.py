import re


def get_email(text_):
    items = re.findall(r"[\w.!#$%&'*+-/=?^_`{|}~]+@+\w+\.\w+", text_)
    return items


def validator_date(date_):
    date = re.search(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[0-1])/\d{4}$", date_)
    if date:
        return f"Date {date_} is valid!"
    else:
        return f"Date {date_} is NOT valid"


def split_email(email_):
    item = re.search(r"^([\w.!#$%&'*+-/=?^_`{|}~]+)+@+(\w+\.\w+)$", email_)
    if item:
        return f"Name = {item.group(1)}, Domain = {item.group(2)}"
    else:
        return f"Email {email_} is NOT valid"


def validator_number(number_):
    number_code = r"(39|50|63|66|67|68|73|91|92|93|94|95|96|97|98|99|)"
    item = re.search(r"^[+]380+" + number_code + r"\d{7}$", number_)
    if item:
        return f"Number {number_} is valid!"
    else:
        return f"Number {number_} is NOT valid!"


def sentence_split(sentence_):
    sentences = re.split(r"(?<=[.?!])\s+", sentence_)
    return sentences
