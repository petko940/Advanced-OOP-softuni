class TheSquirrel:
    def __init__(self, size: int, moves: str):
        self.size = size
        self.moves = moves.split(', ')
        self.collected_hazelnuts = 0
        self.squirrel_position = None
        self.matrix = None

    def get_the_matrix(self):
        self.matrix = [[x for x in input()] for _ in range(self.size)]
        for x in range(self.size):
            if 's' in self.matrix[x]:
                self.squirrel_position = [x, self.matrix[x].index("s")]
                self.matrix[x][self.squirrel_position[1]] = '*'

    def movements(self, move_command):
        move = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1),
        }
        if not 0 <= self.squirrel_position[0] + move[move_command][0] < self.size:
            self.out_field()

        elif not 0 <= self.squirrel_position[1] + move[move_command][1] < self.size:
            self.out_field()

        self.squirrel_position[0] += move[move_command][0]
        self.squirrel_position[1] += move[move_command][1]
        return self.squirrel_position

    def start_move(self):
        for x in range(len(self.moves)):
            self.squirrel_position = self.movements(self.moves[x])

            if self.matrix[self.squirrel_position[0]][self.squirrel_position[1]] == 't':
                self.step_on_trap()
                self.end()
                break
            elif self.matrix[self.squirrel_position[0]][self.squirrel_position[1]] == 'h':
                self.collected_hazelnuts += 1
                self.matrix[self.squirrel_position[0]][self.squirrel_position[1]] = '*'
                if self.collected_hazelnuts == 3:
                    self.collected_all_hazelnuts()
                    self.end()
                    break
        else:
            self.there_are_more_hazelnuts()

    def out_field(self):
        print(f"The squirrel is out of the field.")
        self.end()
        quit()

    @staticmethod
    def step_on_trap():
        print(f"Unfortunately, the squirrel stepped on a trap...")

    @staticmethod
    def collected_all_hazelnuts():
        print(f"Good job! You have collected all hazelnuts!")

    def end(self):
        print(f'Hazelnuts collected: {self.collected_hazelnuts}')

    def there_are_more_hazelnuts(self):
        print("There are more hazelnuts to collect.")
        self.end()


squirrel = TheSquirrel(int(input()), input())
squirrel.get_the_matrix()
squirrel.start_move()
