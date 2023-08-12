import random
from datetime import date, timedelta


def generate_weekend(n):
    today_pl = date.today() + timedelta(days=n)
    weekend = today_pl.strftime("%-d %B %Y")
    return weekend

def generate_password(n):
    # defining the list of choices of characters.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    num = "123456789"
    """
    The random.sample() method returns a list, so we need to convert it into a string before returning it.
    """
    chosen_pass = random.sample(characters, n) + random.sample(num, 3)
    # finally converting the list into a string
    password = "".join(chosen_pass)
    return password


def generate_email():
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    login_len = random.randint(4, 15)
    login = ''
    for i in range(login_len):
        pos = random.randint(0, len(valid_chars) - 1)
        login = login + valid_chars[pos]
    if login[0].isnumeric():
        pos = random.randint(0, len(valid_chars) - 10)
        login = valid_chars[pos] + login
    servers = ['@gmail', '@yahoo', '@redmail', '@bing']
    serv_pos = random.randint(0, len(servers) - 1)
    email = login + servers[serv_pos]
    tlds = ['.com', '.gov', '.net', '.org']
    tld_pos = random.randint(0, len(tlds) - 1)
    email = email + tlds[tld_pos]
    return email
