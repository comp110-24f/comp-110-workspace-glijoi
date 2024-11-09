"""File to define River class."""

__author__ = "730667690"

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
        """checks ages of fish  and bear"""
        checked_fish: list[Fish] = []
        checked_bear: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                checked_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                checked_bear.append(bear)
        self.fish = checked_fish
        self.bears = checked_bear
        return None

    def bears_eating(self):
        """bears eat fish if enough fish per bear"""
        ate: int = 3
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(amount=ate)
                bear.eat(num_fish=ate)
        return None

    def check_hunger(self):
        """checks hunger of bears"""
        survived: list[Bear] = []
        idx: int = 0
        while idx < len(self.bears):
            if self.bears[idx].hunger_score >= 0:
                survived.append(self.bears[idx])
            idx += 1
        self.bears = survived
        return None

    def repopulate_fish(self):
        """fish reproduce in pairs"""
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
        """bears reproduce in pairs"""
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
        """river stats per day"""
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
        """river after one week of simulation"""
        count: int = 0
        while count < 7:
            self.one_river_day()
            count += 1

    def remove_fish(self, amount: int):
        """removes fish as they are eaten"""
        while amount > 0:
            self.fish.pop(0)
            amount -= 1
        return None
