class Phone(object):
    def __init__(self, phone_number):
        # TODO: all of this could probably be a regex
        clean = phone_number.replace('+', '').replace('(', '').replace(')', '').replace('.', '').replace('-', '').replace(' ', '')

        if len(clean) == 11 and not clean[0:1] == '1':
            raise ValueError('Invalid area code.')

        # remove american international code if present
        if len(clean) == 11:
            clean = clean[1:11]

        if len(clean) > 10 or len(clean) < 7:
            raise ValueError('Incorrect amount of digits.')

        self.area_code = clean[0:3]

        if self.area_code[0:1] == '0' or self.area_code[0:1] == '1':
            raise ValueError('Invalid area code.')

        self.exchange_code = clean[3:6]

        if self.exchange_code[0:1] == '0' or self.exchange_code[0:1] == '1':
            raise ValueError('Invalid exchange code.')

        self.subscriber_number = clean[6:10]

        if self.subscriber_number[0:1] == '0' or self.subscriber_number == '1':
            raise ValueError('Invlaid subscriber number.')

        self.number = "{}{}{}".format(self.area_code, self.exchange_code, self.subscriber_number)

    def pretty(self):
        return "({}) {}-{}".format(self.area_code, self.exchange_code, self.subscriber_number)
