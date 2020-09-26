__author__ = "Tom Paz"
__email__ = "tompazz16@gmail.com"
__date__ = "27/09/2020"

from InstagramAPI import InstagramAPI
from time import sleep

class instanalyzer:
""" This class defines an instagram program that uses instagram api to unfollow users that dont follow you back """ 

    def __init__(self):
    """ This function defines class variables """    
        self.following_users = []
        self.follower_users = []      
        self.api = ""

    def login(self, username, password):
    """ This function login to instagram account """
        self.api = InstagramAPI(username, password)
        self.api.login()

    def unfollow_users(self):
    """ This function stores the account followers and following in a list, then unfollow users that dont follow back """
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
