class Profile:
    username: str
    followers: list[str]
    following: list[str]

    def __init__(self, usr):
        self.username = usr
        self.followers = []
        self.following = []

    # Method definitions
    def follow(self, username: str) -> None:
        self.following.append(username)

    def get_following(self) -> list[str]:
        return self.following


my_prof: Profile = Profile("comp110fan")  # calls __init__()
print(my_prof.following)
my_prof.follow(
    "unclatinosintech"
)  # method call <object>.<method>(<non-self parameters>)
print(my_prof.following)


# Class and Method Writing
# Class: Coordinate, attributes: x float and y float,
# constructor takes 3 parameters: self, x float, and y float
# method called get_dist that takes parameters self and other (another coordinate object)
# should return distance btw the 2 coordinate objects

class Coordinate:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = 
        self.y = 