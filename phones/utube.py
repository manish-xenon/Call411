#!/usr/bin/python
import MySQLdb
import random
import re

import urllib2, urllib
import xml.etree.ElementTree as ET
from pprint import pprint as pp

def youtube_search(query):
    keyword = urllib.quote_plus(query + " review")
    url = "http://gdata.youtube.com/feeds/api/videos?orderby=viewCount&max_results=1&vq='%s'" % keyword 
    #pp(url)
    datafile = urllib2.urlopen(url)
    response = datafile.read()
    datafile.close()
    root = ET.fromstring(response)
    entry = root.find('{http://www.w3.org/2005/Atom}entry')

    try:
        result = {}
        result['model_number'] = query
        result['title'] = entry.find('{http://www.w3.org/2005/Atom}title').text
        result['description'] = entry.find('{http://www.w3.org/2005/Atom}content').text

        media = entry.find('{http://search.yahoo.com/mrss/}group')
        result['media_content'] = media.find('{http://search.yahoo.com/mrss/}content').get('url')
        result['media_player'] = media.find('{http://search.yahoo.com/mrss/}player').get('url')
        result['rating'] = entry.find('{http://schemas.google.com/g/2005}rating').get('average')
    except:
        return None

    return result
    
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user='call411', passwd='cs411', db='call411')
    cur = db.cursor()
    cur.execute('SELECT model_number FROM phones')

    queries = []
    for p in cur.fetchall():
        vi_review = youtube_search(p[0])
        #pp(vi_review)
        if vi_review is None:
            continue
        #"""
        query = 'INSERT INTO `video_reviews`(`model_number`, `title`, `description`, `media_content`, `media_player`, `rating`) VALUES (%s, %s, %s, %s, %s, %s)'
        data = (
            vi_review['model_number'],
            vi_review['title'],
            vi_review['description'],
            vi_review['media_content'],
            vi_review['media_player'],
            vi_review['rating'],
        )
        try:
            cur.execute(query, data)
        except:
            pass

    db.commit()
        #"""
    cur.close()
    db.close()
