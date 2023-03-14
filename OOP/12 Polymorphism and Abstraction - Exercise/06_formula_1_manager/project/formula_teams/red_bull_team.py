from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES = 250_000

    @property
    def sponsors(self):
        return {
            'Oracle': {1: 1_500_000, 2: 800_000},
            'Honda': {8: 20_000, 10: 10_000}
        }

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for key, value in self.sponsors.items():
            for pos, price in value.items():
                if race_pos <= pos:
                    revenue += price
                    break

        revenue -= RedBullTeam.EXPENSES
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
