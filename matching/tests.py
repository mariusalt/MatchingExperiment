from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import Bot, SubmissionMustFail


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Intro)

        if self.participant.vars['type'] == 'subsidizer':
        	yield (views.FischHigh, {'contri':1})
#        	yield SubmissionMustFail(views.FischHigh,{'contri':-27})
        else:
        	yield (views.FischLow, {'contri':0})
#        	yield SubmissionMustFail(views.FischLow,{'contri':-27})

        if self.participant.vars['type'] == 'subsidizer':
        	yield (views.FischHighTable, {'zero':7,'one':2,'two':7,'three':6,'four':1,'five':0})
        else:
        	yield (views.FischLowTable, {'zero':3,'one':2,'two':4,'three':5,'four':2,'five':0,'six':5,'seven':4,'eight':5,'nine':2,'ten':2})
       		
        if self.group.outcome == 'tails':
        	if self.participant.vars['type'] == 'subsidizer':
        		assert self.player.payoff == 9
        	else:
        		assert self.player.payoff == 8
 #       if self.group.outcome == 'tails':
  #      	if self.participant.vars['type'] == 'subsidizer':
   #     		assert self.player.payoff == 9.6
    #    	else:
     #   		assert self.player.payoff == 12.6

