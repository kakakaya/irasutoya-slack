#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kakakaya, Date: Sun Oct 15 19:49:06 2017
from unittest import TestCase
from nose.tools import ok_, eq_, raises
import irasutoya


class TestIrasutoyaEntry(TestCase):
    def test_single_illust_entry(self):
        url = 'http://www.irasutoya.com/2017/10/blog-post_613.html'
        title = '中二病のイラスト（女性）'
        desc = '中二病（厨二病）の女の子が自分で考えたかっこいいポーズを取っているイラストです。'
        illust_length = 1
        ie = irasutoya.IrasutoyaEntry(url)
        eq_(ie.url, url)
        eq_(ie.title, title)
        eq_(ie.description, desc)
        eq_(len(ie.illusts), illust_length)

    def test_multiple_illust_entry(self):
        url = 'http://www.irasutoya.com/2013/10/blog-post_5077.html'
        title = '男の子の顔のアイコン'
        desc = 'ツイッターやフェイスブックなどのSNSなどで使える、いろいろな顔の少年のアイコンです。'
        illust_length = 12
        ie = irasutoya.IrasutoyaEntry(url)
        eq_(ie.url, url)
        eq_(ie.title, title)
        eq_(ie.description, desc)
        eq_(len(ie.illusts), illust_length)

    @raises(ValueError)
    def test_bad_url(self):
        url = 'https://kakakaya.xyz'
        irasutoya.IrasutoyaEntry(url)

    def test_special_entry(self):
        url = 'http://www.irasutoya.com/2013/08/kotsu.html'
        title = '検索のコツ'
        ie = irasutoya.IrasutoyaEntry(url)
        eq_(ie.url, url)
        eq_(ie.title, title)
        ok_(ie.is_special_page)
