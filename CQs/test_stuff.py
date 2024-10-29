class Profile:
    username: str
    bio: str
    followers: list[str]
    following: list[str]
    private: bool

    def __init__(self):
        self.username = "usr9"
        self.bio = ""
        self.followers = []
        self.following = []
        self.private = False


my_prof: Profile = Profile()
my_prof.username = "comp110fan"
my_prof.following.append("unc.latinosintech")
print(my_prof.following)
