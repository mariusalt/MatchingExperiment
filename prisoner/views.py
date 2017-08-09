from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
  

    form_model=models.Player
    form_fields=["decision"]




class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.payoff()


class Results(Page):
	def vars_for_template(self):
		player1 = self.group.get_player_by_id(1)
		player2 = self.group.get_player_by_id(2)

		if self.player.id == player1.id:
			return {'otherPlayerDec': self.group.player2.years}
		else:
			return {'otherPlayerDec': self.group.player1.years}

		if self.player.id == player1.id:
			return {'otherPlayerY': self.group.player2.years}
		else:
			return {'otherPlayerY': self.group.player1.years}


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
