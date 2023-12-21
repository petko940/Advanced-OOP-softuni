from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=200)

    def can_climb(self):
        if self.strength >= 100:
            return True
        return False

    def climb(self, peak: BasePeak):
        difficulty_multiplier = 2.0 if peak.difficulty_level == "Extreme" else 1.5
        self.strength -= 20.0 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)
