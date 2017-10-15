#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


class IrasutoyaEntry(object):
    def __init__(self, url):
        """Load irasutoya entry from given URL.
        """
        self.url = url
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        self.title = soup.find("div", class_="title").h2.string.strip()
        self.description = soup.find_all("div", class_='separator')[-1].string.strip()

        imgs = soup.find('div', class_="entry").find_all('img')
        self.illusts = list(filter(None, map(lambda x: x.attrs['src'] if x.attrs.get('alt') is not None else None, imgs)))


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


def main():
    pass


if __name__ == "__main__":
    main()
