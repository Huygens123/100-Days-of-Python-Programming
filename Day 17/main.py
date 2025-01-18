class User:

    def __int__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User()
user_2 = User()
user_1.id, user_1.username = "001", 'Corradi'
user_2.id, user_2.username = "002", 'Huygens'

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
