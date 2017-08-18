from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math
import random

author = 'Marius'

doc = """
Fischbacher, different endowment
"""


class Constants(BaseConstants):
    name_in_url = 'matching'
    players_per_group = 2
    num_rounds = 1
    MPCR=0.8

    read_timeout = 60 
    decision_timeout = 180


class Subsession(BaseSubsession):
	pass


             
        


class Group(BaseGroup):

	project = models.PositiveIntegerField()
	pay_proj = models.FloatField()
	outcome = models.CharField(choices=['heads', 'tails'])

	def rand(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		self.outcome=random.choice(["heads","tails"])
		#heads->the conditional contribution becomes payoff relevant for the subsidizer. Tails-> vice versa
		if self.outcome=="heads":
			self.project=subsidizer.cond+subsidized.contri
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
		else:
			self.project=subsidizer.cond+subsidized.contri
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100

#	def calc_payoff(self):
#		subsidizer = self.get_player_by_role('subsidizer')
#		subsidized = self.get_player_by_role('subsidized')
#		self.outcome=random.choice(["heads","tails"])
#		if self.outcome=="heads":
#			self.project=subsidizer.cond+subsidized.contri
#			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
#			subsidizer.payoff=subsidizer.endowment-subsidizer.cond+Constants.MPCR*self.project
#			subsidized.payoff=subsidized.endowment-subsidized.contri+math.floor(Constants.MPCR*self.project*100)/100
		
#		else:
#			self.project=subsidizer.cond+subsidized.contri
#			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
#			subsidizer.payoff=subsidizer.endowment-subsidizer.contri+Constants.MPCR*self.project
#			subsidized.payoff=subsidized.endowment-subsidized.cond+math.floor(Constants.MPCR*self.project*100)/100
			

#MatchPOINT EXPERIMENT START---------------------------------------------------------

   
	project1 = models.PositiveIntegerField()
	pay_proj1 = models.FloatField()


	def calc_payoff1(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		self.project1 = subsidizer.contri + subsidized.contri
		self.pay_proj1=math.floor(Constants.MPCR*self.project1*100)/100
		subsidizer.payoff=subsidizer.endowment-subsidizer.contri1-subsidizer.t*subsidized.contri1+Constants.MPCR*self.project1
		subsidized.payoff=subsidized.endowment-subsidized.contri1+subsidizer.t*subsidized.contri1+Constants.MPCR*self.project1


class Player(BasePlayer):

	endowment = models.PositiveIntegerField()

	def define_end(self):
		if self.id_in_group ==1:
			self.endowment=10
		else:
			self.endowment=5

	cond = models.PositiveIntegerField()


	def role(self):
		if self.id_in_group ==1:
			return "subsidizer"
		else:
			return "subsidized"


	contri = models.PositiveIntegerField(
    	min=0,
    	widget=widgets.SliderInput(attrs={'step':'1'}),
    	verbose_name="Please decide how much you would like to invest in your common project")



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
	payoffFisch = models.FloatField()


		
	def calc_cond(self):
		self.others_contri = self.get_others_in_group()[0].contri
		con_lists = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten]
		self.cond=con_lists[self.others_contri]

	def calc_payoff2(self):
		if self.group.outcome=="heads":
			if self.id_in_group ==1:
				self.payoffFisch=self.endowment-self.cond+Constants.MPCR*self.group.project
			if self.id_in_group ==2:
				self.payoffFisch=self.endowment-self.contri+Constants.MPCR*self.group.project
		else:
			if self.id_in_group ==1:
				self.payoffFisch=self.endowment-self.contri+Constants.MPCR*self.group.project
			if self.id_in_group ==2:
				self.payoffFisch=self.endowment-self.cond+Constants.MPCR*self.group.project
	
	def vars_for_template(self):
		return {
		'others_payoff' : self.get_others_in_group()[0].payoffFisch,
		'deci':'conditional'}

		



# MATCHPOINT EXPERIMENT START--------------------------------------------------

	contri1 = models.PositiveIntegerField(
    	min=0,
    	widget=widgets.SliderInput(attrs={'step':'1'}),
    	verbose_name="Please decide how much you would like to invest in your common project")


	t = models.FloatField(
		choices=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5],
		widget=widgets.RadioSelect(),
		verbose_name="decide by how many percent you would like to support the other Player's contribution"
		)
	total_payoff=models.FloatField()

	def calc_total_payoff(self):
		self.total_payoff = self.payoff+self.payoffFisch



#	payoff1 = models.FloatField()
#	others_contri1 = models.PositiveIntegerField()
#	others_t = models.FloatField()


#	def calc_payoff2(self):
#		self.others_contri1 = self.get_others_in_group()[0].contri1
#		self.others_t = self.get_others_in_group()[0].t
#		if self.id_in_group ==1:
##			self.payoff1 = self.endowment-self.contri1-self.t*self.others_contri1+Constants.MPCR*self.group.project1
#		else:
#			self.payoff1 = self.endowment-self.contri1+self.others_t*self.contri1+Constants.MPCR*self.group.project1




	










