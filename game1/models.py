from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Marius'

doc = """
game1
"""


class Constants(BaseConstants):
    name_in_url = 'game1'
    players_per_group = None
    num_rounds = 1
    




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    endowment = models.CurrencyField(
    	default=c(100)
    	)

    invest = models.CurrencyField(
    	min=0,
    	max=100,
    	verbose_name="Choose how much you would like to invest",
    	doc="Investment choice"
    	)

    payoff = models.CurrencyField()
    decision = models.StringField()


    def calculate_payoff(self):
    	outcome=random.choice(["win","lose"])
    	if outcome=="win":
    		self.payoff=self.invest+self.endowment
    	if self.decision=="lose":
    		self.payoff=self.endowment-self.invest
    	self.decision=outcome

 


  


    	


