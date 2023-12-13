from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    @property
    def valid_diver_types(self):
        return {
            "FreeDiver": FreeDiver,
            "ScubaDiver": ScubaDiver
        }

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.valid_diver_types:
            return f"{diver_type} is not allowed in our competition."

        for diver in self.divers:
            if diver.name == diver_name:
                return f"{diver_name} is already a participant."

        diver = self.valid_diver_types[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    @property
    def valid_fish_types(self):
        return {
            "PredatoryFish": PredatoryFish,
            "DeepSeaFish": DeepSeaFish
        }

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.valid_fish_types:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(x for x in self.fish_list if x.name == fish_name)
            return f"{fish_name} is already permitted."
        except StopIteration:
            fish = self.valid_fish_types[fish_type](fish_name, points)
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = [x for x in self.divers if x.name == diver_name]
        if not diver:
            return f"{diver_name} is not registered for the competition."
        diver = diver[0]

        fish = [x for x in self.fish_list if x.name == fish_name]
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        fish = fish[0]

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        else:
            if diver.oxygen_level == fish.time_to_catch:
                if is_lucky:
                    diver.hit(fish)
                    if diver.oxygen_level == 0:
                        diver.has_health_issue = True
                    return f"{diver_name} hits a {fish.points}pt. {fish_name}."
                else:
                    diver.miss(fish.time_to_catch)
                    return f"{diver_name} missed a good {fish_name}."
            else:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        output = [f"**{diver_name} Catch Report**"]
        diver = [x for x in self.divers if x.name == diver_name][0]

        for fish in diver.catch:
            output.append(fish.fish_details())

        return '\n'.join(output)

    def competition_statistics(self):
        output = ["**Nautical Catch Challenge Statistics**"]

        for diver in sorted(self.divers, key=lambda x: [-x.competition_points, -len(x.catch), x.name]):
            if diver.oxygen_level:
                output.append(diver.__str__())

        return '\n'.join(output)
