import base64
import json
import os
from tenacity import *
import requests
import logging
import time
from urllib3.exceptions import MaxRetryError

logger = logging.getLogger(__name__)
getUrlDomain = lambda url: urlparse(url).netloc

class GetDataFromUrl():

    def __init__(self):
        self._proxies = self._createProxy()


    def _createProxy(self):
        username = "smartuser101"
        password = "smartuser101"
        proxyLst = [
            f"http://{username}:{password}@gate.dc.smartproxy.com:20000",
        ]

        proxies = {
        'http': proxyLst[0], "https": proxyLst[0]
        }    
        return proxies

    def _getResponse(self, url):
        _res = {}
        for idx in range(1,5):
            try:
                r = requests.get(url, proxies=self._proxies)
                if r.status_code == 200:
                    _res['status_code'] = r.status_code
                    _res['data'] = r
                else:
                    _res['status_code'] = r.status_code
                    _res['data'] = None
                break
            except MaxRetryError:
                logger.info("Exception raised while trying to retrieve data.")
                time.sleep(5)

        _res['data'] = None
        return _res
            

    def _makeSoup(self, response):
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        return soup, html


    def process(self, url):
        r = self._getResponse(url)
        if r['data']:
            soup, html = self._makeSoup(r['data'])
            title = soup.title.text.split("|")[0].strip()
            url_domain = getUrlDomain(url)

            data = {
                "url": url,
                "url_domain": url_domain,
                "title": title,
                "relevance": 1,
                "html": bytes(html, 'utf-8') # NOTE the html is saved as bytes !!!
            } 

            return data
        else:
            logger.info("Could not Process Data")

if __name__ == "__main__":
    get_data = GetDataFromUrl()

    