from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

from otree.api import SubmissionMustFail

class PlayerBot(Bot):
	pass

#    def play_round(self):
 #       yield SubmissionMustFail(views.MyPage,{'invest':-27})
  #      yield (views.MyPage, {'invest':20})
   #     if self.player.decision== 'win':
    #    	assert self.player.payoff == 120
     #   else:
      #  	assert self.player.payoff == 80
