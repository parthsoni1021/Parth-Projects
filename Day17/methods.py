class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0              # initializing a new user will have 0 followers
        self.following = 0

# Unlike function, a methods will always have the self parameter, so that it knows the object which called it
    def follow(self, user):   # user which we've decided to follow
        user.followers += 1
        self.following += 1

# self is a way to refer to object itself, inside the class blueprint

user_1 = User('001','Parth')
user_2 = User('002', 'Arsh')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

