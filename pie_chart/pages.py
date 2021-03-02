from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'group'
    form_fields = ['p1_share']

    def before_next_page(self):
    	self.group.set_p2_share()




class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results
]
