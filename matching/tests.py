from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Bot, SubmissionMustFail
import random


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number ==1:
            yield (pages.Intro)

        if self.participant.vars['type'] == 'subsidizer' and self.round_number == 1:
        	yield (pages.FischHigh, {'contri':random.randrange(0,self.player.endowment,1)})
#        	yield SubmissionMustFail(pages.FischHigh,{'contri':-27})
        if self.participant.vars['type'] == 'subsidized' and self.round_number == 1:
        	yield (pages.FischLow, {'contri':random.randrange(0,self.player.endowment,1)})
#        	yield SubmissionMustFail(pages.FischLow,{'contri':-27})

        if self.participant.vars['type'] == 'subsidizer' and self.round_number == 1:
        	yield (pages.FischHighTable, {'zero':random.randrange(0,self.player.endowment,1),'one':random.randrange(0,self.player.endowment,1),'two':random.randrange(0,self.player.endowment,1),'three':random.randrange(0,self.player.endowment,1),'four':random.randrange(0,self.player.endowment,1),'five':random.randrange(0,self.player.endowment,1)})
        if self.participant.vars['type'] == 'subsidized' and self.round_number == 1:
        	yield (pages.FischLowTable, {'zero':random.randrange(0,self.player.endowment,1),'one':random.randrange(0,self.player.endowment,1),'two':random.randrange(0,self.player.endowment,1),'three':random.randrange(0,self.player.endowment,1),'four':random.randrange(0,self.player.endowment,1),'five':random.randrange(0,self.player.endowment,1),'six':random.randrange(0,self.player.endowment,1),'seven':random.randrange(0,self.player.endowment,1),'eight':random.randrange(0,self.player.endowment,1),'nine':random.randrange(0,self.player.endowment,1),'ten':random.randrange(0,self.player.endowment,1)})
       		
        if self.group.outcome == 'tails':
        	if self.participant.vars['type'] == 'subsidizer':
        		assert self.player.payoff == self.player.endowment-self.player.contri+self.group.pay_proj
        	else:
        		assert self.player.payoff == self.player.endowment-self.player.cond+self.group.pay_proj

            
        if self.group.outcome == 'heads':
            if self.participant.vars['type'] == 'subsidizer':
                assert self.player.payoff == self.player.endowment-self.player.cond+self.group.pay_proj
            else:
                assert self.player.payoff == self.player.endowment-self.player.contri+self.group.pay_proj

        if self.round_number ==1:
            yield (pages.Result1)

        if self.player.treatment=='lowthres' and self.round_number == 2:
            yield (pages.Intro2)
        elif self.player.treatment=='highthres' and self.round_number == 2:
            yield (pages.Intro3)
        elif self.player.treatment=='baseline' and self.round_number == 2:
            yield (pages.Intro1)

        if self.participant.vars['type'] == 'subsidizer' and self.round_number == 2:
            yield (pages.DecisionHigh, {'contri':random.randrange(0,self.player.endowment,1),'t':random.randrange(0,120,10)})

        if self.participant.vars['type'] == 'subsidized' and self.round_number == 2:
            yield (pages.DecisionLow, {"t0":random.randrange(0,self.player.endowment,1),"t10":random.randrange(0,self.player.endowment,1),"t20":random.randrange(0,self.player.endowment,1),"t30":random.randrange(0,self.player.endowment,1),"t40":random.randrange(0,self.player.endowment,1),"t50":random.randrange(0,self.player.endowment,1),"t60":random.randrange(0,self.player.endowment,1),"t70":random.randrange(0,self.player.endowment,1),"t80":random.randrange(0,self.player.endowment,1),"t90":random.randrange(0,self.player.endowment,1),"t100":random.randrange(0,self.player.endowment,1),"t110":random.randrange(0,self.player.endowment,1),"t120":random.randrange(0,self.player.endowment,1)})
 
        if self.player.treatment=='baseline' and self.round_number == 2:
            if self.participant.vars['type'] == 'subsidizer':
                assert self.player.payoff == self.player.endowment-self.player.contri-self.group.amount_subsidy+self.group.pay_proj
            if self.participant.vars['type'] == 'subsidized':
                assert self.player.payoff == self.player.endowment-self.player.cond+self.group.pay_proj
            
        if self.player.treatment=='lowthres' and self.round_number == 2:
            if self.participant.vars['type'] == 'subsidizer':
                assert self.player.payoff == self.player.endowment-self.player.contri-self.group.amount_subsidy+self.group.pay_proj
            if self.participant.vars['type'] == 'subsidized':
                assert self.player.payoff == self.player.endowment-self.player.cond+self.group.pay_proj

        if self.player.treatment=='highthres' and self.round_number == 2:
            if self.participant.vars['type'] == 'subsidizer':
                assert self.player.payoff == self.player.endowment-self.player.contri-self.group.amount_subsidy+self.group.pay_proj
            if self.participant.vars['type'] == 'subsidized':
                assert self.player.payoff == self.player.endowment-self.player.cond+self.group.pay_proj

        if self.round_number ==2:
            yield (pages.Result2)

        if self.player.treatment=='baseline' and self.round_number == 2:
            if self.participant.vars['type'] == 'subsidizer' and self.group.outcome == 'tails':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidized' and self.group.outcome == 'tails':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidizer' and self.group.outcome == 'heads':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidized' and self.group.outcome == 'heads':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

        if self.player.treatment=='lowthres' and self.round_number == 2:
            if self.participant.vars['type'] == 'subsidizer' and self.group.outcome == 'tails':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidized' and self.group.outcome == 'tails':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidizer' and self.group.outcome == 'heads':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidized' and self.group.outcome == 'heads':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

        if self.player.treatment=='highthres' and self.round_number == 2:
            if self.participant.vars['type'] == 'subsidizer' and self.group.outcome == 'tails':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidized' and self.group.outcome == 'tails':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidizer' and self.group.outcome == 'heads':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])

            if self.participant.vars['type'] == 'subsidized' and self.group.outcome == 'heads':
                assert self.player.sum_payoff == sum([p.payoff for p in self.player.in_all_rounds()])
            

        if self.round_number == 2:
            yield (pages.Questionnaire, {'gender':'männlich','age':40,'education':3,'studies':'VWL','occupation':'Researcher'})

