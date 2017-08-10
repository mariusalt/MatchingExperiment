from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model=models.Player
    form_fields=["invest"]

    def invest_max(self):
        return self.player.endowment

    def before_next_page(self):
    	self.player.calc_payoff()





class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results
]
