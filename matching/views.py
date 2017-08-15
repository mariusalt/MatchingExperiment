from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class StartWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class FischHigh(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model=models.Player
    form_fields=["contri"]
    
    def contri_max(self):
        return 20

    def before_next_page(self):
        self.player.other_player()


class FischLow(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model=models.Player
    form_fields=["contri"]

    def contri_max(self):
        return 15

    def before_next_page(self):
        self.player.other_player()


class FischHighTable(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model=models.Player
    form_fields=["twenty","nineteen","eighteen","seventeen","sixteen","fifteen","fourteen","thirteen","twelve","eleven","ten","nine","eight","seven","six","five","four","three","two","one","zero"]
    def before_next_page(self):
        self.player.calc_con()


class FischLowTable(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model=models.Player
    form_fields=["twenty","nineteen","eighteen","seventeen","sixteen","fifteen","fourteen","thirteen","twelve","eleven","ten","nine","eight","seven","six","five","four","three","two","one","zero"]



class Result2WaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.calc_payoff()


class Result1(Page):
	pass


page_sequence = [
    Intro,
    StartWaitPage,
    FischHigh,
    FischLow,
    FischHighTable,
    FischLowTable,
    Result2WaitPage,
    Result1
]
