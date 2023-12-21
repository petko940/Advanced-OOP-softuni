from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=150)

    def can_climb(self):
        if self.strength >= 75:
            return True
        return False

    def climb(self, peak: BasePeak):
        difficulty_multiplier = 1.3 if peak.difficulty_level == "Advanced" else 2.5
        self.strength -= 30.0 * difficulty_multiplier

        self.conquered_peaks.append(peak.name)
