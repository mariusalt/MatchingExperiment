from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Marius'

doc = """
Ultimatum
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 2
    num_rounds = 2
    pot_size=c(100)


class Subsession(BaseSubsession):
	def creating_seesion(self):
		self.group_randomly(fixed_id_in_group=True)
    


class Group(BaseGroup):
    offer = models.PositiveIntegerField(
    	max=Constants.pot_size,
    	min=0,
    	widget=widgets.Slider(attrs={'step':'1'}),
    	verbose_name="Please decide about the quantity to share with the other player")
    accepted = models.BooleanField(
    	choices=[(True, 'Yes'),(False,'No')],
    	verbose_name="Please decide about the other player's offer",
    	doc="response choice")

    def calc_payoff(self):
    	proposer = self.get_player_by_role('proposer')
    	responder = self.get_player_by_role('responder')
    	if self.accepted:
    		proposer.payoff=Constants.pot_size-self.offer
    		responder.payoff=self.offer
    	else:
    		proposer.payoff=c(0)
    		responder.payoff=c(0)


class Player(BasePlayer):
    def role(self):
    	if self.id_in_group ==1:
    		return "proposer"
    	else:
    		return "responder"

 #   pay = models.PositiveIntegerField()


