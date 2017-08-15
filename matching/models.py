from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math
import random
import pprint

author = 'Marius'

doc = """
Fischbacher, different endowment
"""


class Constants(BaseConstants):
    name_in_url = 'matching'
    players_per_group = 2
    num_rounds = 1
    MPCR=0.8

 #   high_endowment=60
 #   low_endowment=40


class Subsession(BaseSubsession):
	pass
#	def before_session_starts(self):
#		for player in self.get_players():
#			player.treatment = "low" if player.id % 2 == 0 else "high"
#		half split by even / odd:

	


#	def creating_session(self):
#		endowment_urn = itertools.cycle([60, 40])
#		for p in self.get_player_by_role():
#			p.endowment = next(endowment_urn)

             
        


class Group(BaseGroup):



#	contri = models.PositiveIntegerField(
#    	min=0,
#    	verbose_name="Please decide how much you would like to invest in your common project")

	project = models.PositiveIntegerField()
	

	def calc_payoff(self):
		rich = self.get_player_by_role('rich')
		poor = self.get_player_by_role('poor')
		self.project=sum([p.contri for p in self.get_players()])
		outcome=random.choice(["unc","con"])
		if outcome=="unc":
			rich.payoff=rich.endowment-rich.cond+Constants.MPCR*self.project
			poor.payoff=poor.endowment-poor.contri+math.floor(Constants.MPCR*self.project*100)/100
		else:
			rich.payoff=rich.endowment-rich.contri+Constants.MPCR*self.project
			poor.payoff=poor.endowment-poor.cond+math.floor(Constants.MPCR*self.project*100)/100




class Player(BasePlayer):

	endowment = models.PositiveIntegerField()
	cond = models.PositiveIntegerField()

#	treatment = models.CharField()

	def role(self):
		if self.id_in_group ==1:
			self.endowment=20
			return "rich"
		else:
			self.endowment=15
			return "poor"


	contri = models.PositiveIntegerField(
    	min=0,
    	widget=widgets.SliderInput(attrs={'step':'1'}),
    	verbose_name="Please decide how much you would like to invest in your common project")


	twenty=models.PositiveIntegerField()
	nineteen=models.PositiveIntegerField()
	eighteen=models.PositiveIntegerField()
	seventeen=models.PositiveIntegerField()
	sixteen=models.PositiveIntegerField()
	fifteen=models.PositiveIntegerField()
	fourteen=models.PositiveIntegerField()
	thirteen=models.PositiveIntegerField()
	twelve=models.PositiveIntegerField()
	eleven=models.PositiveIntegerField()
	ten=models.PositiveIntegerField()
	nine=models.PositiveIntegerField()
	eight=models.PositiveIntegerField()
	seven=models.PositiveIntegerField()
	six=models.PositiveIntegerField()
	five=models.PositiveIntegerField()
	four=models.PositiveIntegerField()
	three=models.PositiveIntegerField()
	two=models.PositiveIntegerField()
	one=models.PositiveIntegerField()
	zero=models.PositiveIntegerField()

	cond = models.PositiveIntegerField(initial=0)
	others_contri=models.PositiveIntegerField()



	def calc_con(self):
		self.others_contri = self.get_others_in_group()[0].contri
		con_lists = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve,self.thirteen,self.fourteen,self.fifteen,self.sixteen,self.seventeen,self.eighteen,self.nineteen,self.twenty]
		for i in con_lists:
			if i == self.others_contri:
				self.cond=i

#		def calc_cond(self):
	#	rich = self.get_player_by_role('rich')
#		poor = self.get_player_by_role('poor')
#		con_lists_high = [rich.zero,rich.one,rich.two,rich.three,rich.four,rich.five,rich.six,rich.seven,rich.eight,rich.nine,rich.ten,rich.eleven,rich.twelve,rich.thirteen,rich.fourteen,rich.fifteen,rich.sixteen,rich.seventeen,rich.eighteen,rich.nineteen,rich.twenty]
#		con_lists_low = [poor.zero,poor.one,poor.two,poor.three,poor.four,poor.five,poor.six,poor.seven,poor.eight,poor.nine,poor.ten,poor.eleven,poor.twelve,poor.thirteen,poor.fourteen,poor.fifteen,poor.sixteen,poor.seventeen,poor.eighteen,poor.nineteen,poor.twenty]
#		for i in con_lists_high:
#			if i == poor.contri:
#				self.cond=i
#		for i in con_lists_low:
#			if i == rich.contri:
#				self.cond=i




  