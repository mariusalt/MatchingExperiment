from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math
import random
import itertools
import pprint
author = 'Marius'

doc = """
Fischbacher, different endowment
"""


class Constants(BaseConstants):
    name_in_url = 'matching'
    players_per_group = 2
    num_rounds = 2
    MPCR=0.8

    read_timeout = 3 
    decision_timeout = 40


class Subsession(BaseSubsession):
	def creating_session(self):
		if self.round_number == 1:
			players = self.get_players()
			turn = itertools.cycle(['subsidizer','subsidized'])
			for p in players:
				p.participant.vars['type'] = next(turn)

		players = self.get_players()
		if self.round_number == 2:
			random.shuffle(players)
		subsidizer_players = [p for p in players if p.participant.vars['type'] == 'subsidizer']
		subsidized_players = [p for p in players if p.participant.vars['type'] == 'subsidized']
		group_matrix = []
		num_groups = int(len(players)/2)

		for i in range(num_groups):
			new_group = [
				subsidizer_players.pop(),
				subsidized_players.pop(),
			]
			group_matrix.append(new_group)

		self.set_groups(group_matrix)

		if self.round_number==2:
			matrix=self.get_groups()
			third=int(round(len(matrix)/3))
			A=matrix[:third]
			B=matrix[-third:]
			C=matrix[third:-third]
			treaties=[A,B,C]
			random.shuffle(treaties)
			turn1 = itertools.cycle(treaties)
			baseline=next(turn1)
			lowthres=next(turn1)
			highthres=next(turn1)

			for group in baseline:
				playersb = group.get_players()
				for p in playersb:
					p.treatment='baseline'
			for group in lowthres:
				playersb = group.get_players()
				for p in playersb:
					p.treatment='lowthres'
			for group in highthres:
				playersb = group.get_players()
				for p in playersb:
					p.treatment='highthres'


class Group(BaseGroup):

	project = models.PositiveIntegerField()
	pay_proj = models.FloatField()
	outcome = models.CharField(choices=['heads', 'tails'])
	amount_subsidy = models.FloatField()
	


	def calc_payoff(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		outcome=random.choice(["heads","tails"])
		if outcome=="heads":
			self.project=subsidizer.cond+subsidized.contri
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
			subsidizer.payoff=subsidizer.endowment-subsidizer.cond+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.contri+math.floor(Constants.MPCR*self.project*100)/100
		if outcome=="tails":
			self.project=subsidized.cond+subsidizer.contri
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
			subsidizer.payoff=subsidizer.endowment-subsidizer.contri+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.cond+math.floor(Constants.MPCR*self.project*100)/100
		self.outcome=outcome	



#MatchPOINT EXPERIMENT START---------------------------------------------------------

  


	def calc_payoff1(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		self.amount_subsidy = round((subsidizer.t/100)*subsidized.cond,2)
		self.project = subsidizer.contri + subsidized.cond+self.amount_subsidy
		self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
		subsidizer.payoff=subsidizer.endowment-subsidizer.contri-self.amount_subsidy+Constants.MPCR*self.project
		subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project

	def calc_payoff2(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		if subsidizer.t <= 20:
			self.project = subsidizer.contri + subsidized.cond
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
			subsidizer.payoff=subsidizer.endowment-subsidizer.contri+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project
		if subsidizer.t > 20:
			self.amount_subsidy = round((subsidizer.t/100)*subsidized.cond,2)
			self.project = subsidizer.contri + subsidized.cond+self.amount_subsidy
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
			subsidizer.payoff=subsidizer.endowment-subsidizer.contri-self.amount_subsidy+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project

	def calc_payoff3(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		if subsidizer.t <= 50:
			self.project = subsidizer.contri + subsidized.cond
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
			subsidizer.payoff=subsidizer.endowment-subsidizer.contri+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project
		if subsidizer.t > 50:
			self.amount_subsidy = round((subsidizer.t/100)*subsidized.cond,2)
			self.project = subsidizer.contri + subsidized.cond+self.amount_subsidy
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
			subsidizer.payoff=subsidizer.endowment-subsidizer.contri-self.amount_subsidy+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project

	


class Player(BasePlayer):
	treatment = models.CharField()

	endowment = models.PositiveIntegerField()

	cond = models.PositiveIntegerField()

	def define_end(self):
			if self.id_in_group == 1:
				self.endowment=10
			else:
				self.endowment=5

	def role(self): 
			if self.id_in_group == 1:
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


		
	def calc_cond(self):

		self.others_contri = self.get_others_in_group()[0].contri
		con_lists = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten]
		self.cond=con_lists[self.others_contri]

	Rel_Dec=models.CharField(choices=['unconditional', 'conditional'])

	def condi(self):
		if self.id_in_group==1 and self.group.outcome=="heads":
			self.Rel_Dec="conditional"
		if self.id_in_group==2 and self.group.outcome=="heads":
			self.Rel_Dec="unconditional"
		if self.id_in_group==1 and self.group.outcome=="tails":
			self.Rel_Dec="unconditional"
		if self.id_in_group==2 and self.group.outcome=="tails":
			self.Rel_Dec="conditional"
		

	
	def vars_for_template(self):
		return {
		'own_contri': self.contri,
		'others_contri_template': self.get_others_in_group()[0].cond,
		'others_payoff' : self.get_others_in_group()[0].payoff,
		'deci':'unconditional'}

		



# MATCHPOINT EXPERIMENT START--------------------------------------------------

	t = models.PositiveIntegerField(
		choices=[0,10,20,30,40,50,60,70,80,90,100,110,120],
		widget=widgets.RadioSelect(),
		verbose_name="decide by how many percent you would like to support the other Player's contribution"
		)
	total_payoff=models.FloatField()

	t0 = models.PositiveIntegerField()
	t10 = models.PositiveIntegerField()
	t20=models.PositiveIntegerField()
	t30=models.PositiveIntegerField()
	t40=models.PositiveIntegerField()
	t50=models.PositiveIntegerField()
	t60=models.PositiveIntegerField()
	t70=models.PositiveIntegerField()
	t80=models.PositiveIntegerField()
	t90=models.PositiveIntegerField()
	t100=models.PositiveIntegerField()
	t110=models.PositiveIntegerField()
	t120=models.PositiveIntegerField()

	other_t=models.PositiveIntegerField()

	def calc_cond1(self):
		self.other_t = self.get_others_in_group()[0].t
		cond_lists = {0:self.t0,10:self.t10,20:self.t20,30:self.t30,40:self.t40,50:self.t50,60:self.t60,70:self.t70,80:self.t80,90:self.t90,100:self.t100,110:self.t110,120:self.t120}
		for key in cond_lists:
			if key==self.other_t:
				self.cond=cond_lists[key]

	def vars_for_template1(self):
		return {
		'others_t' : self.get_others_in_group()[0].t}



	def vars_for_result(self):
		return {'own_contri':self.contri,
		'own_cond':self.cond,
		'others_payoff1' : self.get_others_in_group()[0].payoff,
		'others_contri1': self.get_others_in_group()[0].contri,
		'others_cond':self.get_others_in_group()[0].cond,
		'total_payoff': self.in_round(1).payoff+self.payoff}
#		'real_payoff':self.payoffFisch.to_real_world_currency(self.session)+self.payoff.to_real_world_currency(self.session)}





	










