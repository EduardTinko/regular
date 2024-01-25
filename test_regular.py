from regular import (
    validator_number,
    validator_date,
    get_email,
    split_email,
    sentence_split,
)


def test_find_email():
    text = (
        "Hello! Can you send an email to exemple-name23@exemple.com, exemple-name22@exemple.com. "
        "My email is exemple@exemple.ua!"
    )
    emails = get_email(text)
    assert emails == [
        "exemple-name23@exemple.com",
        "exemple-name22@exemple.com",
        "exemple@exemple.ua",
    ]


def test_find_email_not_found():
    text = "Hello! I don't have an email address."
    emails = get_email(text)
    assert emails == []


def test_valid_date1():
    date = "10/22/2012"
    val_date = validator_date(date)
    assert val_date == "Date 10/22/2012 is valid!"


def test_valid_date2():
    date = "01/31/1942"
    val_date = validator_date(date)
    assert val_date == "Date 01/31/1942 is valid!"


def test_valid_date3():
    date = "12/01/1984"
    val_date = validator_date(date)
    assert val_date == "Date 12/01/1984 is valid!"


def test_valid_date4():
    date = "01/31/1742"
    val_date = validator_date(date)
    assert val_date == "Date 01/31/1742 is valid!"


def test_not_valid_date1():
    date = "01/213/2022"
    val_date = validator_date(date)
    assert val_date == "Date 01/213/2022 is NOT valid"


def test_not_valid_date2():
    date = "1/23/2012"
    val_date = validator_date(date)
    assert val_date == "Date 1/23/2012 is NOT valid"


def test_split_email():
    email = "email_name@example.ua"
    s_email = split_email(email)
    assert s_email == "Name = email_name, Domain = example.ua"


def test_split_email_not_valid():
    email = "email_name@example./ua"
    s_email = split_email(email)
    assert s_email == "Email email_name@example./ua is NOT valid"


def test_valid_number():
    number = "+380984325432"
    val_number = validator_number(number)
    assert val_number == "Number +380984325432 is valid!"


def test_not_valid_number():
    number = "0984325432"
    val_number = validator_number(number)
    assert val_number == "Number 0984325432 is NOT valid!"


def test_sentence_split():
    text = (
        "The sun is setting behind the horizon. The forest whispers its secrets. "
        "Is a star watching us from afar? Clouds drift like memories. "
        "The river sings a song of the past. Our destiny is a moment. Now and forever, here and now."
    )

    sentences = sentence_split(text)
    assert sentences == [
        "The sun is setting behind the horizon.",
        "The forest whispers its secrets.",
        "Is a star watching us from afar?",
        "Clouds drift like memories.",
        "The river sings a song of the past.",
        "Our destiny is a moment.",
        "Now and forever, here and now.",
    ]
