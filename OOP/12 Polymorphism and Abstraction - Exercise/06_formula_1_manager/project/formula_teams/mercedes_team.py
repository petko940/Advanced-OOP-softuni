from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES = 200_000

    @property
    def sponsors(self):
        return {
            'Petronas': {1: 1_000_000, 3: 500_000},
            'TeamViewer': {5: 100_000, 7: 50_000}
        }

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for key, value in self.sponsors.items():
            for pos, price in value.items():
                if race_pos <= pos:
                    revenue += price
                    break

        revenue -= MercedesTeam.EXPENSES
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
