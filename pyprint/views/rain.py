#coding: utf-8
from pyprint.handler import BaseHandler


class RainHandler(BaseHandler):
    def get(self):
        return self.render('rain.html')
