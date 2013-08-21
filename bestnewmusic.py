#!/usr/bin/python

# return name of lastest best new music on pitchfork

import urllib2
import re

def main():
  
  web_page = urllib2.urlopen('http://www.pitchfork.com/best')
  all_the_html = web_page.read()

  # this string surrounds the first row of Best New things
  demarcator = 'bnm-hub-features-1'

  # grab the first one, this is the first Best New Album
  relevant_block = re.findall(demarcator+'(.*?)'+demarcator, all_the_html)
  first_block = relevant_block[0]

  # grab just the artist of the first Best New album
  relevant_artist = re.findall('h1>'+'(.*?)'+'</h1', first_block)
  print relevant_artist[0]

if __name__ == '__main__':
    main()
