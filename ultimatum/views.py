from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    timeout_seconds = 60

class Page2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    timeout_seconds = 60




class Page3(Page):
	def is_displayed(self):
		return self.player.id_in_group == 1

	form_model=models.Group
	form_fields=["offer"]
	timeout_seconds = 60
	timeout_submission = {'proposer_share':0}

#	def before_next_page(self):
#		if self.tiemout_happened:
#			self.player.fell_asleep = True
    		


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Page4(Page):
	def is_displayed(self):
		return self.player.id_in_group == 2

	form_model=models.Group
	form_fields=["accepted"]

class ResultsWaitPage1(WaitPage):
	def after_all_players_arrive(self):
		self.group.calc_payoff()

    

class Page5(Page):
    pass

page_sequence = [
    Page1,
    Page2,
    Page3,
    ResultsWaitPage,
    Page4,
    ResultsWaitPage1,
    Page5
]
