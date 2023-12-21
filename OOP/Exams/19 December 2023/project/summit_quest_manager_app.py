from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list[BasePeak] = []

    @property
    def climbers_types(self):
        return {
            "ArcticClimber": ArcticClimber,
            'SummitClimber': SummitClimber
        }

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.climbers_types:
            return f"{climber_type} doesn't exist in our register."

        for name in self.climbers:
            if climber_name == name.name:
                return f"{climber_name} has been already registered."

        new_climber = self.climbers_types[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    @property
    def peak_types(self):
        return {
            "ArcticPeak": ArcticPeak,
            "SummitPeak": SummitPeak
        }

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.peak_types:
            return f"{peak_type} is an unknown type of peak."

        if peak_name in [peak.name for peak in self.peaks]:
            return

        new_peak = self.peak_types[peak_type](peak_name, peak_elevation)
        new_peak.calculate_difficulty_level()
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = [climber for climber in self.climbers if climber.name == climber_name][0]
        peak = [peak for peak in self.peaks if peak.name == peak_name][0]

        peak_gear = set(peak.get_recommended_gear())
        gear = set(gear)

        if gear == peak_gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        missing_gear = peak_gear - gear
        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = next(x for x in self.climbers if x.name == climber_name)
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(x for x in self.peaks if x.name == peak_name)
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        result = [f"Total climbed peaks: {len(self.peaks)}",
                  f"**Climber's statistics:**"]

        for climber in sorted(self.climbers, key=lambda x: (-len(x.conquered_peaks), x.name)):
            if climber.conquered_peaks:
                result.append(climber.__str__())

        return '\n'.join(result)
