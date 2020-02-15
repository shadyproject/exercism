# new in Python 3.6 and really cool
import secrets
import string

class Robot(object):
    def new_name(self):
        return ''.join([
            # generate two random numbers in the ASCII range
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_uppercase),
            # generate three numbers between 0 and 9
            # we generate three numbers so we can get 000 inclusive
            # and not just 0 through 999
            str(secrets.choice(range(10))),
            str(secrets.choice(range(10))),
            str(secrets.choice(range(10)))
        ])

    def __init__(self):
        self.name = self.new_name()

    def reset(self):
        self.name = self.new_name()

