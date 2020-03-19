#! python3
# threadedDownloadXkcd.py - download XKCD comics using muliti threads

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)


def downloadXKcd(startComic, endComic):
  print('aaaaaaaaaaaa %s' %(startComic))
  for urlNumber in range(startComic, endComic):
    print('downloading pages htts://xkcd.com/%s..' %(urlNumber))
    res=requests.get('https://xkcd.com/%s' % (urlNumber))
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem=soup.select('#comic img')
    if comicElem == []:
      print('can not find comic img')
    else:
      comicUrl=comicElem[0].get('src')
      print('downloading img %s' % (comicUrl))
      res=requests.get('https:' + comicUrl)
      res.raise_for_status()

      imageFile=open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

      for chunk in res.iter_content(100000):
        imageFile.write(chunk)
      imageFile.close()

downloadThreads = []
for i in range(0,140,10):
  start = i
  end = i+9
  if start == 0:
    start = 1
  downloadThread = threading.Thread(target=downloadXKcd, args=(start,end))
  downloadThreads.append(downloadThread)
  downloadThread.start()

for downloadThread in downloadThreads:
  downloadThread.join()
print('done')
