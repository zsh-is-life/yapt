#!/usr/bin/python3
import sys

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '?', '/']
numerical_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def checkArguments():
    if(len(sys.argv == 1)):
        raise Exception("Missing parameters: <password> [wordlists(s)]")
        
def checkSpecialChars(password):
    successFlag = 0
    for char in special_chars:
        if char in password:
            successFlag = 1
    if(not successFlag):
        raise Exception("Your password does not have any special characters")
    return True

def checkNumericalchars(password):
    successFlag = 0
    for char in numerical_chars:
        if char in password:
            successFlag = 1
    if(not successFlag):
        raise Exception("Your password does not have any numbers")
    return True

def checkPasswordLength(password):
    if(len(password) < 8):
        raise Exception("Your password is too short")
    return True

def testPassword(password):
    try:
        if(checkPasswordLength(password) and checkSpecialChars(password) and checkNumericalchars(password) and openWordlistFiles(password)):
            print("Your password looks good")
            sys.exit(0)
    except Exception as e:
        print(e)

def openWordlistFiles(password):
    for fileIndex in range(2, len(sys.argv)):
        print(f"Opening file {sys.argv[fileIndex]}")
        with open(str(sys.argv[fileIndex]), "r") as fHandler:
            for line in fHandler:
                line = line.strip()
                if(line == password):
                    raise Exception("Your password failed wordlist test")
        #File will auto close.
    return True

testPassword(sys.argv[1])