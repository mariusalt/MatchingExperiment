from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math
import random
import pprint

author = 'Marius'

doc = """
Matching experiment, different endowment, subsidizer and subsidized
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
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		self.project=sum([p.contri for p in self.get_players()])
		outcome=random.choice(["unc","con"])
		if outcome=="unc":
			subsidizer.payoff=subsidizer.endowment-subsidizer.cond+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.contri+math.floor(Constants.MPCR*self.project*100)/100
		else:
			subsidizer.payoff=subsidizer.endowment-subsidizer.contri+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.cond+math.floor(Constants.MPCR*self.project*100)/100




class Player(BasePlayer):

	endowment = models.PositiveIntegerField()
	cond = models.PositiveIntegerField()

#	treatment = models.CharField()

	def role(self):
		if self.id_in_group ==1:
			self.endowment=20
			return "subsidizer"
		else:
			self.endowment=15
			return "subsidized"


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

	cond = models.PositiveIntegerField()
	others_contri=models.PositiveIntegerField()

	def other_player(self):
		others_contri = self.get_others_in_group()[0].contri


	def calc_con(self):
		con_lists = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve,self.thirteen,self.fourteen,self.fifteen,self.sixteen,self.seventeen,self.eighteen,self.nineteen,self.twenty]
		for i in con_lists:
			if i == self.others_contri:
				self.cond=i

#		def calc_cond(self):
	#	subsidizer = self.get_player_by_role('subsidizer')
#		subsidized = self.get_player_by_role('subsidized')
#		con_lists_high = [subsidizer.zero,subsidizer.one,subsidizer.two,subsidizer.three,subsidizer.four,subsidizer.five,subsidizer.six,subsidizer.seven,subsidizer.eight,subsidizer.nine,subsidizer.ten,subsidizer.eleven,subsidizer.twelve,subsidizer.thirteen,subsidizer.fourteen,subsidizer.fifteen,subsidizer.sixteen,subsidizer.seventeen,subsidizer.eighteen,subsidizer.nineteen,subsidizer.twenty]
#		con_lists_low = [subsidized.zero,subsidized.one,subsidized.two,subsidized.three,subsidized.four,subsidized.five,subsidized.six,subsidized.seven,subsidized.eight,subsidized.nine,subsidized.ten,subsidized.eleven,subsidized.twelve,subsidized.thirteen,subsidized.fourteen,subsidized.fifteen,subsidized.sixteen,subsidized.seventeen,subsidized.eighteen,subsidized.nineteen,subsidized.twenty]
#		for i in con_lists_high:
#			if i == subsidized.contri:
#				self.cond=i
#		for i in con_lists_low:
#			if i == subsidizer.contri:
#				self.cond=i




  