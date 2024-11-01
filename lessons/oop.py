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
