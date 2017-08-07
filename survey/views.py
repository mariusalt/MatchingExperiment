from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    form_model=models.Player
    form_fields=["age","gender","field_of_studies","height","weight"]


class WaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Page2(Page):
    pass


page_sequence = [
    Page1,
    WaitPage,
    Page2
]
