import calendar


class DVD:
    def __init__(self, name: str, id_num: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_num
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_num: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(x) for x in date.split('.')]
        return cls(name, id_num, year, calendar.month_name[month], age_restriction)

    def __repr__(self):
        if self.is_rented:
            rent = 'rented'
        else:
            rent = 'not rented'

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age " \
               f"restriction {self.age_restriction}. Status: {rent}"
