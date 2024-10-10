#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import optparse
import os
import sqlite3

# Function to print downloaded files from the downloads database
def printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)  # Connect to the downloads database
    c = conn.cursor()  # Create a cursor object
    c.execute('SELECT name, source, datetime(endTime/1000000, \'unixepoch\') FROM moz_downloads;')
    print('\n[*] --- Files Downloaded --- ')
    for row in c:
        print('[+] File: ' + str(row[0]) + ' from source: ' + str(row[1]) + ' at: ' + str(row[2]))

# Function to print cookies from the cookies database
def printCookies(cookiesDB, search_host):
    try:
        conn = sqlite3.connect(cookiesDB)  # Connect to the cookies database
        c = conn.cursor()  # Create a cursor object
        c.execute('SELECT host, name, value FROM moz_cookies')

        print('\n[*] -- Found Cookies --')
        found = False  # Flag to check if the cookie is found
        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])
            if search_host in host:
                print('[+] Host: ' + host + ', Cookie: ' + name + ', Value: ' + value)
                found = True
        if not found:
            print('Cookie not present')  # Print message if cookie is not found
    except Exception as e:
        if 'encrypted' in str(e):
            print('\n[*] Error reading your cookies database.')
            print('[*] Upgrade your Python-Sqlite3 Library')

# Function to print browsing history from the places database
def printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)  # Connect to the places database
        c = conn.cursor()  # Create a cursor object
        c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")

        print('\n[*] -- Found History --')
        for row in c:
            url = str(row[0])
            date = str(row[1])
            print('[+] ' + date + ' - Visited: ' + url)
    except Exception as e:
        if 'encrypted' in str(e):
            print('\n[*] Error reading your places database.')
            print('[*] Upgrade your Python-Sqlite3 Library')
            exit(0)

# Function to print Google search history from the places database
def printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)  # Connect to the places database
    c = conn.cursor()  # Create a cursor object
    c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")

    print('\n[*] -- Found Google --')
    for row in c:
        url = str(row[0])
        date = str(row[1])
        if 'google' in url.lower():
            r = re.findall(r'q=.*\&', url)
            if r:
                search = r[0].split('&')[0]
                search = search.replace('q=', '').replace('+', ' ')
                print('[+] ' + date + ' - Searched For: ' + search)

def main():
    parser = optparse.OptionParser("usage %prog -p <firefox profile path>")
    parser.add_option('-p', dest='pathName', type='string', help='specify firefox profile path')

    (options, args) = parser.parse_args()
    pathName = options.pathName
    if pathName is None:
        print(parser.usage)
        exit(0)
    elif not os.path.isdir(pathName):
        print('[!] Path Does Not Exist: ' + pathName)
        exit(0)
    else:
        search_host = input("Enter the cookie host you are looking for: ")

        cookiesDB = os.path.join(pathName, 'cookies.sqlite')
        if os.path.isfile(cookiesDB):
            printCookies(cookiesDB, search_host)
        else:
            print('[!] Cookies Db does not exist: ' + cookiesDB)

if __name__ == '__main__':
    main()
