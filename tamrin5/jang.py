class Soldier:
    soldier_ids = []

    def __init__(self, soldier_type, soldier_id, x, y):
        self.soldier_type = soldier_type
        self.soldier_id = soldier_id
        self.health = 100
        self.x = x
        self.y = y
        Soldier.soldier_ids.append(self.soldier_id)


class Archer(Soldier):
    def __init__(self, soldier_id, x, y):
        super().__init__("archer", soldier_id, x, y)


class Melee(Soldier):
    def __init__(self, soldier_id, x, y):
        super().__init__("melee", soldier_id, x, y)


class Game:
    def __init__(self, n):
        self.positions = {0: {}, 1: {}}
        self.players = {0: [], 1: []}
        self.current_turn = 0
        self.n = n

    def invalid_switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def create_soldier(self, soldier_type, soldier_id, x, y):
        player_ids = [i.soldier_id for i in self.players[self.current_turn]]
        if soldier_id in player_ids:
            print("duplicate tag")
            return

        if (x, y) not in self.positions[self.current_turn]:
            self.positions[self.current_turn][(x, y)] = []

        if soldier_type == "archer":
            soldier = Archer(soldier_id, x, y)
        elif soldier_type == "melee":
            soldier = Melee(soldier_id, x, y)
        else:
            print("Invalid soldier type")
            return

        self.positions[self.current_turn][(x, y)].append(soldier)
        self.players[self.current_turn].append(soldier)
        self.invalid_switch_turn()

    def move_soldier(self, soldier_id, direction):
        soldier = self.find_soldier(soldier_id)

        if soldier is not None:
            old_position = (soldier.x, soldier.y)
            new_x, new_y = self.calculate_new_position(soldier, direction)

            if not self.is_within_bounds(new_x, new_y):
                print("out of bounds")
                return

            self.positions[self.current_turn][old_position].remove(soldier)

            if (new_x, new_y) not in self.positions[self.current_turn]:
                self.positions[self.current_turn][(new_x, new_y)] = []
            self.positions[self.current_turn][(new_x, new_y)].append(soldier)

            soldier.x = new_x
            soldier.y = new_y

            self.invalid_switch_turn()
            return
        else:
            print("soldier does not exist")
            return

    def attack(self, attacker_id, target_id):
        attacker = self.find_soldier_for_attack(attacker_id, "attacker")
        target = self.find_soldier_for_attack(target_id, "defender")

        if attacker is None or target is None:
            return
        if isinstance(attacker, Archer):
            self.handle_archer_attack(attacker, target)
        elif isinstance(attacker, Melee):
            self.handle_melee_attack(attacker, target)

    def handle_archer_attack(self, archer, target):
        if self.calculate_distance(archer.x, archer.y, target.x, target.y) > 2:
            print("the target is too far")
            return
        target.health -= 10
        self.handle_health_after_attack(target)

    def handle_melee_attack(self, melee, target):
        if self.calculate_distance(melee.x, melee.y, target.x, target.y) > 1:
            print("the target is too far")
            return
        target.health -= 20
        self.handle_health_after_attack(target)

    def handle_health_after_attack(self, target):
        if target.health <= 0:
            print("target eliminated")
            target_position = (target.x, target.y)
            if target_position in self.positions[1 - self.current_turn]:
                if target in self.positions[1 - self.current_turn][target_position]:
                    self.positions[1 - self.current_turn][target_position].remove(target)
            if target in self.players[1 - self.current_turn]:
                self.players[1 - self.current_turn].remove(target)
        self.invalid_switch_turn()

    def get_info(self, soldier_id):
        soldier = self.find_soldier(soldier_id)
        if soldier is None:
            print("soldier does not exist")
            return

        print(f"health:  {soldier.health}")
        print(f"location:  {soldier.x}   {soldier.y}")
        self.invalid_switch_turn()

    def who_is_in_lead(self):
        score = {0: 0, 1: 0}
        for player, soldiers in self.players.items():
            for soldier in soldiers:
                score[player] += soldier.health

        if score[0] > score[1]:
            print("player  1")
        elif score[0] < score[1]:
            print("player  2")
        else:
            print("draw")

    def find_soldier(self, soldier_id):
        for soldiers_list in self.positions[self.current_turn].values():
            for soldier in soldiers_list:
                if soldier.soldier_id == soldier_id:
                    return soldier

    def find_soldier_for_attack(self, soldier_id, who_is):
        if who_is == "attacker":
            for soldiers_list in self.positions[self.current_turn].values():
                for soldier in soldiers_list:
                    if soldier.soldier_id == soldier_id:
                        return soldier
        else:
            for soldiers_list in self.positions[1 - self.current_turn].values():
                for soldier in soldiers_list:
                    if soldier.soldier_id == soldier_id:
                        return soldier
        print("soldier does not exist")
        return None

    def calculate_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def calculate_new_position(self, soldier, direction):
        if direction == "up":
            return soldier.x, soldier.y - 1
        elif direction == "down":
            return soldier.x, soldier.y + 1
        elif direction == "left":
            return soldier.x - 1, soldier.y
        elif direction == "right":
            return soldier.x + 1, soldier.y
        else:
            print("Invalid direction")
            return soldier.x, soldier.y

    def is_within_bounds(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n


def main():
    k = int(input())
    game = Game(k)
    commands = []

    while True:
        try:
            line = input().split(" ")
            if 'end' in line:
                break
            commands.append(line)
        except EOFError:
            break

    point = 0
    while True:
        if point == len(commands):
            break
        command = commands[point]
        if command[0] == "new":
            game.create_soldier(command[1], int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "move":
            game.move_soldier(int(command[1]), command[2])
        elif command[0] == "attack":
            game.attack(int(command[1]), int(command[2]))
        elif command[0] == "info":
            game.get_info(int(command[1]))
        elif command[0] == "who":
            game.who_is_in_lead()
        point += 1


if __name__ == "__main__":
    main()
