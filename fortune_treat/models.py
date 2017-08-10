from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools


author = 'Marius'

doc = """
Fortune with treat
"""


class Constants(BaseConstants):
    name_in_url = 'fortune_treat'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
	def creating_session(self):
		for p in self.get_players():
			if 'treatment' in self.session.config:
				p.endowment = self.session.config['treatment']  #demo mode
			else:
				p.endowment = random.choice([100,1000])  #live experiment

        	    
#     def before_session_starts(self):  #random assignment to treatments
#     	for player in self.get_players(): 
#            player.endowment = random.choice([100, 1000])

#        endowment_urn = itertools.cycle([100, 1000]) #equal number of participants in treatments
#        for p in self.get_players():
#            p.endowment = next(endowment_urn)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	# endow=Subsession.endowment
    endowment=models.IntegerField()

    invest = models.IntegerField(
    	min=0,
    	widget=widgets.SliderInput(attrs={'step':'1'}),
    	verbose_name="Choose how much you would like to invest",
    	doc="Investment choice"
    	)

    decision = models.CharField()

    def calc_payoff(self):
    	outcome=random.choice(["win","lose"])
    	if outcome=="win":
    		self.payoff=self.invest+self.endowment
    	if self.decision=="lose":
    		self.payoff=self.endowment-self.invest
    	self.decision=outcome

    

