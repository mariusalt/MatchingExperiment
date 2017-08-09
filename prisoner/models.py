from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def payoff(self):
    	players = self.get_players()
    	player1 = players[0]
    	player2 = players[1]
    	if player1.decision=="stay silent" and player2.decision=="stay silent":
    		player1.years=1
    		player2.years=1
    	elif player1.decision=="stay silent" and player2.decision=="betray":
    		player1.years=3
    		player2.years=0
    	elif player2.decision=="stay silent" and player1.decision=="betray":
    		player1.years=0
    		player2.years=3
    	else:
    		player1.years=2
    		player2.years=2


class Player(BasePlayer):
    decision = models.CharField(
    	choices=["stay silent","betray"],
    	widget=widgets.RadioSelect(),
    	verbose_name="Make a choice",
    	doc="Participants make a choice about cooperation"
    	)

    years = models.PositiveIntegerField()
