# https://oauth.vk.com/blank.html#access_token=vk1.a.Xt0yi8W72Wb2Y7lsG5MYs7tWx2F5rppTdqdPTWh0ZabXgrCitn5vHkqPAm3WxSIHJpPnIyqMbvQTXU_l3wVXTNJS6DoPHLPqNMuskFcEAkm41d5dsbrU9kDzbThkAJ9ePJ-Ug4ek5Prp6ZnYmJl8OQ3I39V9YOMyeDDPNTxnObJoQshovY18E4J5-iQtDSHi&expires_in=86400&user_id=188251237&state=123456


TOKEN='vk1.a.Xt0yi8W72Wb2Y7lsG5MYs7tWx2F5rppTdqdPTWh0ZabXgrCitn5vHkqPAm3WxSIHJpPnIyqMbvQTXU_l3wVXTNJS6DoPHLPqNMuskFcEAkm41d5dsbrU9kDzbThkAJ9ePJ-Ug4ek5Prp6ZnYmJl8OQ3I39V9YOMyeDDPNTxnObJoQshovY18E4J5-iQtDSHi'
u_id='188251237'

import requests

class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'users_id': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()
    
access_token = TOKEN
user_id = u_id
vk = VK(access_token, user_id)
print(vk.users_info())