#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

class read_html():
    def __init__(self, path):
        self.path = path
        self.html = self.open_url()
        self.bsObj = None
        
    def open_url(self):
        ''' Create Ins urllib (self.path
            return ins / None
        '''
        try:
            self.html = urlopen(self.path)
        except HTTPError as e:            
            print(e)            
        except URLError as e:
            print("The server could not be found!")            
        else:
            print("It Worked->", self.path)
            return self.html

        return None
    
    def soup_read(self):
        ''' Create Ins Beautifulsoup4
            return ins / None
        '''

        self.bsObj = BeautifulSoup(self.html.read(), "html5lib")
        return self.bsObj

    def read_title(self):
        if soup_read is None:
            self.bsObj = self.soup_read()
        
        try:
            title = self.bsObj.head.title
        except AttributeError as e:
            return None
        return title
            



if __name__ == '__main__':
    test = read_html('http://himado.in/')
    a = test.soup_read()
    print(test.read_title())
        
