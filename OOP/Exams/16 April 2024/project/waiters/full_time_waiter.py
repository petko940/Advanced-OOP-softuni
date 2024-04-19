from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    def calculate_earnings(self):
        return self.hours_worked * 15

    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."
