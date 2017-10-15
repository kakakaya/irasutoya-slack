#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

IRASUTOYA_DOMAIN = 'www.irasutoya.com'


class IrasutoyaEntry(object):
    def __init__(self, url):
        """Load irasutoya entry from given URL.
        """
        if url.find(IRASUTOYA_DOMAIN) == -1:
            raise ValueError("URL seems not to be valid.")
        self.url = url
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        post = soup.find("div", id='post')

        self.title = post.find("div", class_="title").h2.string.strip()
        ss = post.find_all("div", class_='separator')
        if not ss:
            self.is_special_page = True
            return
        else:
            self.is_special_page = False

        self.description = ss[-1].string.strip()

        imgs = post.find('div', class_="entry").find_all('img')
        self.illusts = list(
            filter(
                None,
                map(
                    lambda x: IrasutoyaIllust(title=x.attrs['alt'], url=x.attrs['src']) if x.attrs.get('alt') is not None else None,
                    imgs
                )
            )
        )


class IrasutoyaIllust(object):
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self._image = None

    @property
    def image(self):
        if not self._image:
            self._image = self.get_image()
        return self._image

    def get_image(self):
        return requests.get(self.url).raw
