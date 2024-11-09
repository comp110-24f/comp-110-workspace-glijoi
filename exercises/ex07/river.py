"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        checked_fish: list[Fish] = []
        checked_bear: list[Bear] = []
        idx: int = 0
        while idx < len(self.fish):
            if Fish.age <= 3:
                checked_fish.append(self.fish[idx])
            idx += 1
        ind: int = 0
        while ind < len(self.bears):
            if Bear.age <= 5:
                checked_bear.append(self.bears[ind])
            ind += 1
        self.fish = checked_fish
        self.bears = checked_bear
        return None

    def bears_eating(self):
        if len(self.fish) / len(self.bears) >= 5:
            fish_eaten: int = len(self.bears) * 3
            self.remove_fish(amount=fish_eaten)
            for bear in self.bears:
                bear.eat(num_fish=fish_eaten)
        return None

    def check_hunger(self):
        survived: list[Bear] = []
        idx: int = 0
        while idx < len(self.bears):
            if self.bears[idx].hunger_score >= 0:
                survived.append(self.bears[idx])
            idx += 1
        self.bears = survived
        return None

    def repopulate_fish(self):
        new: float = 0
        if len(self.fish) % 2 == 0:
            new = (len(self.fish) / 2) * 4
        elif len(self.fish) % 2 != 0:
            new = ((len(self.fish) / 2) - 0.5) * 4
        while new > 0:
            self.fish.append(Fish())
            new -= 1
        return None

    def repopulate_bears(self):
        new: float = 0
        if len(self.bears) % 2 == 0:
            new = len(self.bears) / 2
        elif len(self.bears) % 2 != 0:
            new = (len(self.bears) / 2) - 0.5
        while new > 0:
            self.bears.append(Bear())
            new -= 1
        return None

    def view_river(self):
        x: int = self.day
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        count: int = 0
        while count < 7:
            self.one_river_day()
            count += 1

    def remove_fish(self, amount: int):
        idx: int = len(self.fish) - 1
        removed: list[Fish] = []
        while idx < len(self.fish):
            if idx < 0:
                return None
            elif idx > amount:
                removed.append(self.fish[idx])
            idx -= 1
        self.fish = removed
