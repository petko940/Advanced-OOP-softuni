from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        return f"Player {player.name} is in another guild."
   
    def kick_player(self, player_name: str):
        for i, value in enumerate(self.players):
            if value.name == player_name:
                value.guild = "Unaffiliated"
                self.players.pop(i)
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        output = [f"Guild: {self.name}"]
        for ppl in self.players:
            output.append(ppl.player_info())
        return "\n".join(output)
