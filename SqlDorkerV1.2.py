#Don't CHnage anything from here ;) DIBO237#
#my git link https://github.com/DIBO237
from multiprocessing.dummy import Pool
from bs4 import BeautifulSoup as bs
from sys import exit, argv
import requests, urllib.parse

header = {'user-agent': 'Moofzilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
url1 = "https://bing.com/search?q="
#count page and thread, dorks
class Dorker(object):

    urls = []

    def __init__(self, dorks, page_count, thread_count):
        self.dorks = dorks
        self.page_count = page_count
        self.thread_count = thread_count
#Loop to make bing search
    def makelist(self, dork):
        i = page = 1
        while i <= self.page_count:
            url = url1 + urllib.parse.quote(dork) + '&first=' + str(page)
            self.urls.append(url)
            i += 1
            page += 10
#All are stored after search is generated
    def load(self, url):
        html = requests.get(url, headers = header).text
        data = bs(html, 'html.parser')
        results = data.find('ol', {'id': 'b_results'})
        results = results.find_all('li', {'class': 'b_algo'})
        for result in results:
            link = result.find('a').attrs['href']
            print(link)
            f = open('result.txt', 'w')
            f.write(link)
            f.write("\n")
            f.close()

    def run(self):
        for dork in self.dorks:
            self.makelist(dork)
            with Pool(self.thread_count) as worker:
                worker.map(self.load, self.urls)
                worker.close()
                worker.join()
            self.urls = []
#It can also be used extarnaly in linux terminal like this python SqlDorkerv1.2.py dorklist.txt
def main():
   while True:
        print('''<=============== DORKER BY DIBO237# V 1.2 ================>

MAke YOUr SeleCtIonS:
              ''')
       
        
        dorks = thread_count = page_count = None
#it sarches for thelist if not found returns error not found
        if len(argv) > 1:
            if argv[1].lower() == 'file':
                try:
                    dorks = open(input("Enter dorklist file path: "), 'r').read().split('\n')
                except IOError:
                    exit("Dorklist not found")
            else:
                exit("Error, unknown option")
#this General runs on a terminal where u can manually type in dork                
        else:
            dorks = input("Enter your dorks: ").split(' ')

        page_count = int(input("Enter pages to look: "))
        thread_count = int(input("Threads: "))

        open('result.txt', 'a').close()

        dorker = Dorker(dorks, page_count, thread_count)
        dorker.run()
        
        print()
        print("Sarch Completed!! SAved to result.txt ;)!! keep hunting!!")

    

if __name__ == '__main__':
    main()
#Simple and effective dorker by DIBO237#    