from InstagramAPI import InstagramAPI
from time import sleep

class instanalyzer:

    def __init__(self):
        self.following_users = []
        self.follower_users = []      
        self.api = ""

    def login(self, username, password):
        self.api = InstagramAPI(username, password)
        self.api.login()

    def unfollow_users(self):
        api = self.api
        api.getSelfUserFollowers()
        result = api.LastJson
        for user in result['users']:
            self.follower_users.append({'pk':user['pk'], 'username':user['username']})

        api.getSelfUsersFollowing()
        result = api.LastJson
        for user in result['users']:
            self.following_users.append({'pk':user['pk'],'username':user['username']})

        for user in self.following_users:
            if user not in self.follower_users:
                print('Unfollowing @' + user['username'])
                api.unfollow(user['pk'])
                #sleep(20) 

bot = instanalyzer()
bot.login("username", "password")
bot.unfollow_users()
