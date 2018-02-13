import re


class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    def __repr__(self):
        'Improves the dfault rep in stack traces.'
        return "Money({},{})".format(self.dollars, self.cents)

def money_from_string(amount):
    match = re.search(r'^\$(P<dollars>\d+).(?P<cents>\d\d)$', amount)
    if match is None:
        raise ValueError("Invalid amount: " + repr(amount))
    dollars = int(match.group('dollars'))
    cents = int(match.group('cents'))
    return Money(dollars, cents)
