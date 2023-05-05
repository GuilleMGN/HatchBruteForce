# Brute Force Attacks with Hatch

## What is a Brute Force attack?
Brute force attacks consist of attempting various amounts of passwords to a username, and hoping to eventually guess the right credentials. This is more of a trial-and-error approach, so there is no real strategy to this method of attack. After a few failed attempts, anyone can become exhausted. However, if an attacker does some research on their victim, it can maybe help narrow down some possible passwords that the victim may use, however it's still a lot of guess work. But what if… the guessing could be done for you instead…

## Introduction to Hatch - What is Hatch?
Hatch is a python script that can help automate brute force attacks within your chrome browser on any webpage with a login form. Automating brute force attacks with Hatch can give anyone a massive advantage because the script will attempt more passwords than a human could, and at a much faster rate. Hatch works in the command line, by being provided a Website and its HTML elements: the Username field, the Password field, and the Login button. Hatch will then ask for a username that we want to attack, and finally, Hatch will use a word list and start the brute forcing within your Chrome browser!

## Tools & Technologies
* Python 2.7
* Hatch
* Selenium
* Google Chrome Browser
* Chrome Web Driver
* Word List
* Webpage Login Form

## Goals & Objectives
The goal is to show how we can use python scripts to automate brute force attacks on vulnerable web page login forms with weak user credentials, all done by code instead of an actual user having to manually guess and input common credentials. We will know the objective is complete when the script has successfully guessed a user’s password on a website and we are now able to access the websites contents as that user that has signed in. 

## Installation Instructions
### How to get Hatch python script: 
* Install [Python version 2.7](https://www.python.org/downloads/windows)
* Install Python Libraries: Requests and Selenium
* Install the [Chrome Driver extension](https://chromedriver.chromium.org/downloads)
* Clone the [Hatch GitHub repository](https://github.com/nsgodshall/Hatch)

### How to run Hatch python script: 
* Navigate to Hatch directory and run 'hatch.py'
* Navigate to a webpage login form
* Enter prompted information in the command line
* Hatch will start brute forcing
* Hatch will let you know when it's completed its brute force attack

## Mitigation Strategies
There are plenty of ways to defend against brute force attacks, which is now a standard for almost every website. The most common being getting locked out after a certain number of failed login attempts. Web services have password requirements that the user must satisfy when creating their accounts in order to proceed. 
Hatch will not function properly on websites that have these protective measures against brute force attacks, or if the login page layout is different. 

## Sources and References
* https://github.com/nsgodshall/Hatch 
* https://null-byte.wonderhowto.com/how-to/brute-force-nearly-any-website-login-with-hatch-0192225/ 
* https://chromedriver.chromium.org/downloads 
* https://www.python.org/downloads/windows 

---
Coded my Metachar - project used for my BootCon presenation in Cybersecurity
