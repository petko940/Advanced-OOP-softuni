import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNumberSymbolsError(Exception):
    pass


class IllegalSymbolInEmailError(Exception):
    pass


length_name_pattern = re.compile("(\w{4,})")
domain_name_pattern = re.compile("\.(com|bg|org|net)$")
illegal_symbols = re.compile("([^\w+\.*\@{1}]+)")

while True:
    emails = input()
    if emails.startswith("End"):
        break

    if illegal_symbols.findall(emails):
        raise IllegalSymbolInEmailError("Email must contain only letters, numbers, only one '@', '.' and '_'")

    if emails.count('@') > 1:
        raise InvalidNumberSymbolsError("Email must contain only one @")

    if not length_name_pattern.findall(emails):
        raise NameTooShortError("Name must be more than 4 characters")

    if emails.count("@") < 1:
        raise MustContainAtSymbolError("Email must contain @")

    if not domain_name_pattern.findall(emails):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')
