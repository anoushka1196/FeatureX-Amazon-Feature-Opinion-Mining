import urllib
import urllib.parse
import requests
import re

def img(asin):
    try:
        url = 'https://www.amazon.com/dp/'+asin

        # now, with the below headers, we defined ourselves as a simpleton who is
        # still using internet explorer.
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        print(str(respData))

        para = re.findall(r'data-old-hires="https://(.*?)jpg',str(respData))

        for eachp in para:
            eachp="https://"+eachp+"jpg"
            with open('images/'+asin+'.jpg', 'wb') as handle:
                response = requests.get(eachp, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)

            print(eachp)



        saveFile = open('withHeaders.txt','w')
        saveFile.write(str(respData))
        saveFile.close()
    except Exception as e:
         print(str(e))