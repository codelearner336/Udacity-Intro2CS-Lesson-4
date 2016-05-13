#crawl web https://www.udacity.com/cs101x/index.html

import urllib
import time
#1) get the urls of a web page

def geturls(url):              # get the first/next link in source code of variable "page"
    page = urllib.urlopen(url).read()
    linklist = []
    start_link = page.find('<a href=')

    while start_link != -1: 
            start_quote = page.find('"http', start_link) #start search for " from psoition "startling" 
            end_quote = page.find('"', start_quote + 1) 
            url = page[start_quote + 1:end_quote]  #+1 so as to not capture the " ie start at HTTP
            linklist.append(url)
            start_link= page.find('<a href=',end_quote)
    return linklist

  
def crawl_the_web(url,max_pages):    

    start_time = time.time()  # Check execution time of this program

    to_crawl = [url]            
    final_list_of_crawled_urls = []
    index = ["init",["init"]]
    while to_crawl:           # while this list is not empty  

         if len(final_list_of_crawled_urls) < max_pages:    
            url = to_crawl.pop()
            linklist = geturls(url)

            for link in linklist:
                if link not in final_list_of_crawled_urls :
                    final_list_of_crawled_urls.append(link)
                else:
                     linklist.remove(link)              # dont store duplicates

            for link in linklist:
                to_crawl.append(link)                   # any new links found, go and crawl them
         else:
             break

    while final_list_of_crawled_urls:
            
            for link in final_list_of_crawled_urls:

                 url = final_list_of_crawled_urls.pop()
              
                 try:                                       # some pages reject urlopen 
                     content = urllib.urlopen(url).read()
                 except:
                     print "exception" , url
                 
                 words = content.split()                    
                 less_words = words[5:6]                    
                 index.append([less_words,[url]] )          # slow and basic but works to prove the point. 

    
    print("--- %s seconds ---" % (time.time() - start_time)) # execution time
    print index        
   # return (final_list_of_crawled_urls)
    
print crawl_the_web("http://www.reddit.com",5)        



