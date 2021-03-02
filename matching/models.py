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
    num_rounds = 3
    MPCR=0.7

    read_timeout = 180
    decision_timeout = 500


class Subsession(BaseSubsession):
	def creating_session(self):

		if self.round_number == 1:
			players = self.get_players()
			turn = itertools.cycle(['subsidizer','subsidized'])
			for p in players:
				p.participant.vars['type'] = next(turn)
			global c
			c=random.choice([0.25,0.25,0.25,-0.75,0.25,0.25,0.25,-0.75,0.25,0.25,0.25,-0.75,0.25,0.25,0.25,-0.75,0.25,0.25,0.25])
			global d	
			d=random.choice([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5])#15 zu 12
			global e
			e=random.choice([-0.25,-0.25,-0.25,0.75,-0.25,-0.25,-0.25,0.75,-0.25,-0.25,-0.25,0.75,-0.25,-0.25,0.75,0.75,0.75])
			global g
			g=random.choice([1,1,1])
			players = self.get_players()
			num_groups = int(len(players)/2)
			b=num_groups/2
			if str(b-int(b))[2]=="7":
		#			c=numpy.random.choice((0.25,-0.75),1,p=(0.75,0.25))	
#					c=random.choice([0.25,0.25,0.25,-0.75])		
					basis=int(b+c)
			elif str(b-int(b))[2]=="5":
#					c=random.choice([0.5,-0.5])
					basis=int(b+d)
			elif str(b-int(b))[2]=="2":
#					c=random.choice([-0.25,-0.25,-0.25,0.75])
					basis=int(b+e)
			else:
					if g==1:
						basis=int(round(b))
					else:
						basis=int(round(b))+1
#			basis=0
			pbase=players[:2*basis]
			for p in pbase:
				p.treatment='base'
			rest=players[2*basis:]
			subsidizer_players = [p for p in rest if p.participant.vars['type'] == 'subsidizer']
			subsidized_players = [p for p in rest if p.participant.vars['type'] == 'subsidized']
			subsidizer_players_basis = [p for p in pbase if p.participant.vars['type'] == 'subsidizer']
			subsidized_players_basis = [p for p in pbase if p.participant.vars['type'] == 'subsidized']
			group_matrix = []
			num_groups1 = int(len(rest)/2)

			for i in range(num_groups1):
				new_group = [
					subsidizer_players.pop(),
					subsidized_players.pop(),
				]
				group_matrix.append(new_group)
			for i in range(basis):
				new_group = [
					subsidizer_players_basis.pop(),
					subsidized_players_basis.pop(),
				]
				group_matrix.append(new_group)

			self.set_groups(group_matrix)

			
			


		if self.round_number == 2:
			players = self.get_players()
			num_groups = int(len(players)/2)
			b=num_groups/2
			if str(b-int(b))[2]=="7":
		#			c=numpy.random.choice((0.25,-0.75),1,p=(0.75,0.25))	
#					c=random.choice([0.25,0.25,0.25,-0.75])		
					basis=int(b+c)
			elif str(b-int(b))[2]=="5":
#					c=random.choice([0.5,-0.5])
					basis=int(b+d)
			elif str(b-int(b))[2]=="2":
#					c=random.choice([-0.25,-0.25,-0.25,0.75])
					basis=int(b+e)
			else:
					if g==1:
						basis=int(round(b))
					else:
						basis=int(round(b))+1
#			basis=0
			pbase=players[:2*basis]
			
			for p in pbase:
				p.treatment='base'
			rest=players[2*basis:]

			random.shuffle(rest)
			random.shuffle(pbase)
			subsidizer_players = [p for p in rest if p.participant.vars['type'] == 'subsidizer']
			subsidized_players = [p for p in rest if p.participant.vars['type'] == 'subsidized']
			subsidizer_players_basis = [p for p in pbase if p.participant.vars['type'] == 'subsidizer']
			subsidized_players_basis = [p for p in pbase if p.participant.vars['type'] == 'subsidized']
			group_matrix = []
			num_groups1 = int(len(rest)/2)

			for i in range(num_groups1):
				new_group = [
					subsidizer_players.pop(),
					subsidized_players.pop(),
				]
				group_matrix.append(new_group)
			for i in range(basis):
				new_group = [
					subsidizer_players_basis.pop(),
					subsidized_players_basis.pop(),
				]
				group_matrix.append(new_group)

			self.set_groups(group_matrix)

		

			matrix=self.get_groups()
			if basis!=0:
				matrix=matrix[:-basis]
			baseline = []
			lowthres = []
			highthres = []
			for i in matrix:
				j=random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3])
				if j==1:
					baseline.append(i)
				if j==2:
					lowthres.append(i)
				if j==3:
					highthres.append(i)

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

		if self.round_number==3:
			self.group_like_round(2)
			players = self.get_players()
			num_groups = int(len(players)/2)
			b=num_groups/2
			if str(b-int(b))[2]=="7":
		#			c=numpy.random.choice((0.25,-0.75),1,p=(0.75,0.25))	
#					c=random.choice([0.25,0.25,0.25,-0.75])		
					basis=int(b+c)
			elif str(b-int(b))[2]=="5":
#					c=random.choice([0.5,-0.5])
					basis=int(b+d)
			elif str(b-int(b))[2]=="2":
#					c=random.choice([-0.25,-0.25,-0.25,0.75])
					basis=int(b+e)
			else:
					if g==1:
						basis=int(round(b))
					else:
						basis=int(round(b))+1
			pbase=players[:2*basis]
			for p in pbase:
				p.treatment='base'
			rest=players[2*basis:]


class Group(BaseGroup):

	project = models.FloatField()
	pay_proj = models.FloatField()
	outcome = models.StringField(choices=['heads', 'tails'])
	amount_subsidy = models.FloatField(initial=0)
	sub_base_subsidizer = models.FloatField(initial=0)
	sub_base_subsidized = models.FloatField(initial=0)
	


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

  
	def rand_dec(self):
		self.outcome=random.choice(["heads","tails"])

	def calc_payoff1(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		if self.outcome=="tails":
			self.amount_subsidy = round((subsidizer.t/100)*subsidized.cond,2)
			self.project = subsidized.cond+self.amount_subsidy
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
			subsidizer.payoff=subsidizer.endowment-self.amount_subsidy+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project
		if self.outcome=="heads":
			self.amount_subsidy = round((subsidizer.condt/100)*subsidized.contri,2)
			self.project = subsidized.contri+self.amount_subsidy
			self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
			subsidizer.payoff=subsidizer.endowment-self.amount_subsidy+Constants.MPCR*self.project
			subsidized.payoff=subsidized.endowment-subsidized.contri+Constants.MPCR*self.project

	def calc_payoff2(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		if self.outcome=="tails":
			if subsidized.cond < 4:
				self.project = subsidized.cond
				self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
				subsidizer.payoff=subsidizer.endowment+Constants.MPCR*self.project
				subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project
			if subsidized.cond >= 4:
				self.amount_subsidy = round((subsidizer.t/100)*subsidized.cond,2)
				self.project = subsidized.cond+self.amount_subsidy
				self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
				subsidizer.payoff=subsidizer.endowment-self.amount_subsidy+Constants.MPCR*self.project
				subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project
		if self.outcome=="heads":
			if subsidized.contri < 4:
				self.project = subsidized.contri
				self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
				subsidizer.payoff=subsidizer.endowment+Constants.MPCR*self.project
				subsidized.payoff=subsidized.endowment-subsidized.contri+Constants.MPCR*self.project
			if subsidized.contri >= 4:
				self.amount_subsidy = round((subsidizer.condt/100)*subsidized.contri,2)
				self.project = subsidized.contri+self.amount_subsidy
				self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
				subsidizer.payoff=subsidizer.endowment-self.amount_subsidy+Constants.MPCR*self.project
				subsidized.payoff=subsidized.endowment-subsidized.contri+Constants.MPCR*self.project

	def calc_payoff3(self):
		subsidizer = self.get_player_by_role('subsidizer')
		subsidized = self.get_player_by_role('subsidized')
		if self.outcome=="tails":
			if subsidized.cond < 12:
				self.project = subsidized.cond
				self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
				subsidizer.payoff=subsidizer.endowment+Constants.MPCR*self.project
				subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project
			if subsidized.cond >= 12:
				self.amount_subsidy = round((subsidizer.t/100)*subsidized.cond,2)
				self.project = subsidized.cond+self.amount_subsidy
				self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
				subsidizer.payoff=subsidizer.endowment-self.amount_subsidy+Constants.MPCR*self.project
				subsidized.payoff=subsidized.endowment-subsidized.cond+Constants.MPCR*self.project
		if self.outcome=="heads":
			if subsidized.contri < 12:
				self.project = subsidized.contri
				self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
				subsidizer.payoff=subsidizer.endowment+Constants.MPCR*self.project
				subsidized.payoff=subsidized.endowment-subsidized.contri+Constants.MPCR*self.project
			if subsidized.contri >= 12:
				self.amount_subsidy = round((subsidizer.condt/100)*subsidized.contri,2)
				self.project = subsidized.contri+self.amount_subsidy
				self.pay_proj=math.floor(Constants.MPCR*self.project*100)/100
				subsidizer.payoff=subsidizer.endowment-self.amount_subsidy+Constants.MPCR*self.project
				subsidized.payoff=subsidized.endowment-subsidized.contri+Constants.MPCR*self.project
	
	def out(self):
		self.outcome=self.in_round(2).outcome


class Player(BasePlayer):
	treatment = models.StringField()

	endowment = models.PositiveIntegerField()


	def define_end(self):
		if self.treatment != 'base':
			if self.id_in_group == 1:
				self.endowment=40
			else:
				self.endowment=20
		if self.treatment=='base':
			self.endowment=30


	def role(self): 
			if self.id_in_group == 1:
				return "subsidizer"
			else:
				return "subsidized"


	contri = models.PositiveIntegerField(
    	min=0,
    	verbose_name="Ihr unbedingter Beitrag zum Projekt")


	fourty=models.PositiveIntegerField()
	thirtynine=models.PositiveIntegerField()
	thirtyeight=models.PositiveIntegerField()
	thirtyseven=models.PositiveIntegerField()
	thirtysix=models.PositiveIntegerField()
	thirtyfive=models.PositiveIntegerField()
	thirtyfour=models.PositiveIntegerField()
	thirtythree=models.PositiveIntegerField()
	thirtytwo=models.PositiveIntegerField()
	thirtyone=models.PositiveIntegerField()
	thirty=models.PositiveIntegerField()
	twentynine=models.PositiveIntegerField()
	twentyeight=models.PositiveIntegerField()
	twentyseven=models.PositiveIntegerField()
	twentysix=models.PositiveIntegerField()
	twentyfive=models.PositiveIntegerField()
	twentyfour=models.PositiveIntegerField()
	twentythree=models.PositiveIntegerField()
	twentytwo=models.PositiveIntegerField()
	twentyone=models.PositiveIntegerField()
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

	cond = models.IntegerField(initial=0)
	condt = models.IntegerField(initial=0)
	others_contri=models.IntegerField()


	def calc_others_contri(self):
		self.others_contri = self.get_others_in_group()[0].contri

	def calc_cond(self):
		con_lists = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve,self.thirteen,self.fourteen,self.fifteen,self.sixteen,self.seventeen,self.eighteen,self.nineteen,self.twenty,self.twentyone,self.twentytwo,self.twentythree,self.twentyfour,self.twentyfive,self.twentysix,self.twentyseven,self.twentyeight,self.twentynine,self.thirty,self.thirtyone,self.thirtytwo,self.thirtythree,self.thirtyfour,self.thirtyfive,self.thirtysix,self.thirtyseven,self.thirtyeight,self.thirtynine,self.fourty]
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
		'deci':'unbedingte'}

	sum_payoff=models.CurrencyField(initial=0)
	sum_pay_euro=models.FloatField()

	def total_payoff(self):
		self.sum_payoff=round(self.in_round(1).payoff+self.in_round(2).payoff+self.payoff,1)
		self.sum_pay_euro=self.sum_payoff.to_real_world_currency(self.session)





# MATCHPOINT EXPERIMENT START--------------------------------------------------

	t = models.PositiveIntegerField(
#		choices=[[0,"0%"],[10,"10%"],[20,"20%"],[30,"30%"],[40,"40%"],[50,"50%"],[60,"60%"],[70,"70%"],[80,"80%"],[90,"90%"],[100,"100%"],[110,"110%"],[120,"120%"]],
		)
	

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
	t130=models.PositiveIntegerField()
	t140=models.PositiveIntegerField()
	t150=models.PositiveIntegerField()
	t160=models.PositiveIntegerField()
	t170=models.PositiveIntegerField()
	t180=models.PositiveIntegerField()
	t190=models.PositiveIntegerField()
	t200=models.PositiveIntegerField()
	t210=models.PositiveIntegerField()
	t220=models.PositiveIntegerField()
	t230=models.PositiveIntegerField()
	t240=models.PositiveIntegerField()
	t250=models.PositiveIntegerField()
	t260=models.PositiveIntegerField()
	t270=models.PositiveIntegerField()
	t280=models.PositiveIntegerField()
	t290=models.PositiveIntegerField()
	t300=models.PositiveIntegerField()
	

	def vars_for_template1(self):
		return {
		'others_t' : self.get_others_in_group()[0].t}


	other_t=models.IntegerField()

	def calc_cond1(self):
		self.other_t = self.get_others_in_group()[0].t
		
		cond_lists = {0:self.t0,10:self.t10,20:self.t20,30:self.t30,40:self.t40,50:self.t50,60:self.t60,70:self.t70,80:self.t80,90:self.t90,100:self.t100,110:self.t110,120:self.t120,130:self.t130,140:self.t140,150:self.t150,160:self.t160,170:self.t170,180:self.t180,190:self.t190,200:self.t200,210:self.t210,220:self.t220,230:self.t230,240:self.t240,250:self.t250,260:self.t260,270:self.t270,280:self.t280,290:self.t290,300:self.t300}
		for key in cond_lists:
			if key==self.other_t:
				self.cond=cond_lists[key]

	def calc_cond2(self):
		self.others_contri = self.get_others_in_group()[0].contri
		condt_lists = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve,self.thirteen,self.fourteen,self.fifteen,self.sixteen,self.seventeen,self.eighteen,self.nineteen,self.twenty,self.twentyone,self.twentytwo,self.twentythree,self.twentyfour,self.twentyfive,self.twentysix,self.twentyseven,self.twentyeight,self.twentynine,self.thirty]
		self.condt=condt_lists[self.others_contri]

	guess=models.IntegerField()
	def fun_guess(self):
		if self.id_in_group==1:
				if (self.guess-self.in_round(2).others_contri)<=1:
					self.payoff=9
				if (self.guess-self.in_round(2).others_contri)>1:
					self.payoff=6/(self.guess-self.in_round(2).others_contri)
		if self.id_in_group==2:
				if (self.guess-self.in_round(2).other_t)<=10:
					self.payoff=9
				if (self.guess-self.in_round(2).other_t)>10:
					self.payoff=6/((self.guess-self.in_round(2).other_t)/10)


	def treat(self):
		self.treatment=self.in_round(2).treatment

	def vars_for_result(self):
		return {
		'own_cont':self.condt,
		'un':'unbedingte',
		'be':'bedingte',
		'own_contri': self.in_round(2).contri,
		'others_payoff1' : self.in_round(2).get_others_in_group()[0].payoff,
		'others_contri1': self.in_round(2).others_contri,
		'cond' : self.in_round(2).cond,
		'others_condt' : self.get_others_in_group()[0].condt,
		'others_cond':self.in_round(2).get_others_in_group()[0].cond,
		'round1_payoff': self.in_round(1).payoff,
		'total_payoff': self.in_round(1).payoff+self.in_round(2).payoff+self.payoff,
		'real_payoff':(self.in_round(1).payoff+self.in_round(2).payoff+self.payoff).to_real_world_currency(self.session),
		'payoff2':self.in_round(2).payoff,
		'amount_subsidy':self.in_round(2).group.amount_subsidy,
		'pay_proj':self.in_round(2).group.pay_proj}

#------------------Questionnaire--------------------------------
	equity1 = models.IntegerField(
#		choices=[
#			[1, 'A: 1.500	B: 1.500		C: 1.500'], 
#			[2, 'A: 1.250	B: 1.500		C: 1.750'],
#			[3, 'A: 1.125	B: 1.500		C: 1.875'],
#			[4, "A: 1.050	B: 1.500		C: 1.950"],
#			[5, "A: 1.000	B: 1.500		C: 2.000"],
#			[6, "A:x	B: x		C: x"]			
#		 ],
#		 verbose_name="Die Personen A, B und C besitzen gemeinsam ein Unternehmen. Da A, B und C in verschiedenem Maße zum Unternehmen beitragen, haben sie unterschiedliche Vergütungen vereinbart. Dementsprechend beziehen Sie monatlich jeweils 1.500 €, 2.000 € und 2.500 €. Alle drei Personen haben noch andere Einkommensquellen. Durch eine unerwartete Verschlechterung der wirtschaftlichen Lage beträgt der ihnen zustehende Anteil am Ertrag ihres Betriebes für einen bestimmten Monat lediglich 4.500 €, zu wenig also, um die drei Unternehmensleiter zu vergüten. Welches ist Ihrer Meinung nach die gerechteste Aufteilung der Summe von 4.500 € auf die Personen A, B und C?",
#		 widget=widgets.RadioSelect
	)
	equity1_A=models.CharField(blank=True)
	equity1_B=models.CharField(blank=True)
	equity1_C=models.CharField(blank=True)
	equity2_A=models.CharField(blank=True)
	equity2_B=models.CharField(blank=True)
	equity2_C=models.CharField(blank=True)
	equity3_A=models.CharField(blank=True)
	equity3_B=models.CharField(blank=True)
	equity3_C=models.CharField(blank=True)

	equity2 = models.IntegerField(
		choices=[
			[1, 'A: 1.000	B: 1.750		C: 1.750'], 
			[2, 'A: 1.000	B: 1.500		C: 2.000'],
			[3, 'A:   750	B: 1.500		C: 2.250'],
			[4, "A:   666	B: 1.416		C: 2.416"],
			[5, "A:   500	B: 1.500		C: 2.500"],
			[6, "A:x	B: x		C: x"]			
		 ],
#		 verbose_name="Stellen Sie sich nun bitte vor, dass die monatlichen Vergütungen, die A, B und C vereinbart haben, 1.000 €, 2.000 € beziehungsweise 3.000 € betragen. Welches ist Ihrer Meinung nach die gerechteste Aufteilung der Summe von 4.500 € auf die Personen A, B und C?",
		 widget=widgets.RadioSelect
		)

	equity3 = models.IntegerField(
		choices=[
			[1, 'A:   500	B: 2.000		C: 2.000'], 
			[2, 'A:   500	B: 1.625		C: 2.375'],
			[3, 'A:   450	B: 1.600		C: 2.450'],
			[4, 'A:   400	B: 1.500		C: 2.600'],
			[5, "A:   375	B: 1.500		C: 2.625"],
			[6, "A:   333	B: 1.333		C: 2.833"],
			[7, "A:   250	B: 1.375		C: 2.875"],
			[8, "A:   166	B: 1.416		C: 2.916"],
			[9, "A:     0	B: 1.500		C: 3.000"],
			[10, "A:x	B: x		C: x"]			
		 ],
#		 verbose_name="3.	Stellen Sie sich nun bitte vor, dass die monatlichen Vergütungen, die A, B und C vereinbart haben, 500 €, 2.000 € beziehungsweise 3.500 € betragen. Welches ist Ihrer Meinung nach die gerechteste Aufteilung der Summe von 4.500 € auf die Personen A, B und C? ",
		 widget=widgets.RadioSelect)


	risk = models.IntegerField(
#		choices=[
#			[1, '0 gar nicht risikobereit'], 
#			[2, '1'],
#			[3, '2'],
#			[4, "3"],
#			[5, "4"],
#			[6, "5"],
#			[7, "6"],
#			[8, "7"],
#			[9, "8"],
#			[10, "9"],
#			[11, "10 sehr risikobereit"]
#		 ],
#		 verbose_name="Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden? Bitte kruezen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: 'gar nicht risikobereit' und der Wert 10: 'sehr risikobereit'. Mit den Werten dazwischen können Sie Ihre Einschätzung abstufen.",
#		 widget=widgets.RadioSelectHorizontal
		 )
	
	trust1 = models.PositiveIntegerField(
		choices=[
			[1, 'Stimme voll zu'], 
			[2, 'Stimme eher zu'],
			[3, 'Lehne eher ab'],
			[4, "Lehne voll ab"],
			[5, "Keine Angabe"]			
		 ],
#		 verbose_name="Wie ist Ihre Meinung zu den folgenden Aussagen? Im Allgemeinen kann den meisten Menschen vertraut werden.",
		 widget=widgets.RadioSelect)

	trust2 = models.PositiveIntegerField(
		choices=[
			[1, 'Stimme voll zu'], 
			[2, 'Stimme eher zu'],
			[3, 'Lehne eher ab'],
			[4, "Lehne voll ab"],
			[5, "Keine Angabe"]			
		 ],
#		 verbose_name="Wenn man mit Fremden zu tun hat, ist es besser, vorsichtig zu sein, bevor man ihnen vertraut.",
		 widget=widgets.RadioSelect)

	trust3 = models.PositiveIntegerField(
		choices=[
			[5, 'Stimme voll zu'], 
			[4, 'Stimme eher zu'],
			[3, 'Lehne eher ab'],
			[2, "Lehne voll ab"],
			[1, "Keine Angabe"]			
		 ],
#		 verbose_name="Heutzutage kann man sich auf niemanden mehr verlassen.",
		 widget=widgets.RadioSelect)


	graphs = models.PositiveIntegerField(
		choices=[
			[1, 'Sehr hilfreich'], 
			[2, 'Hilfreich'],
			[3, 'Wenig hilfreich'],
			[4, "Überhaupt nicht hilfreich"],
			[5, "Keine Angabe"]			
		 ],
#		 verbose_name="Wie hilfreich finden Sie Tabellen und Diagramme beim Lesen von Nachrichten?",
		 widget=widgets.RadioSelect)

	percent = models.PositiveIntegerField(
		choices=[
			[1, 'Sehr sicher'], 
			[2, 'Sicher'],
			[3, 'Unsicher'],
			[4, "Sehr unsicher"],
			[5, "Keine Angabe"]			
		 ],
#		 verbose_name="Wie sicher sind Sie im Umgang mit Prozentzahlen?",
		 widget=widgets.RadioSelect)

	tipp = models.PositiveIntegerField(
		choices=[
			[1, 'Sehr leicht'], 
			[2, 'Leicht'],
			[3, 'Schwer'],
			[4, "Sehr schwer"],
			[5, "Keine Angabe"]			
		 ],
#		 verbose_name="Wie schwer fällt es Ihnen ein Trinkgeld von 15% zu berechnen?",
		 widget=widgets.RadioSelect)

	supermarket = models.PositiveIntegerField(
		choices=[
			[1, 'Supermarkt 1'], 
			[2, 'Supermarkt 2'],
			[3, 'Der Preis pro Kilogramm Mehl ist bei beiden Supermärkten gleich']			
		 ],
#		 verbose_name="Stellen Sie sich vor, Sie benötigen Mehl. Es gibt in Ihrer Nähe zwei Supermärkte, diese verlangen ursprünglich für ein Kilogramm Mehl derselben Qualität den gleichen Preis. Aufgrund eines aktuellen Angebots bietet Supermarkt 1 einen Rabatt von 20% auf ein Kilogramm Mehl an. In Supermarkt 2 wird 20% mehr Verpackungsinhalt zum ursprünglichen Preis aktuelle angeboten. In welchem Supermarkt ist der Preis pro Kilogramm Mehl geringer?",
		 widget=widgets.RadioSelect)

	gender = models.StringField(
		choices=['weiblich', 'männlich', 'weitere', 'keine Angabe'],
		verbose_name="Bitte geben Sie ihr Geschlecht an.",
		widget=widgets.RadioSelectHorizontal)

	age = models.PositiveIntegerField(verbose_name="Wie alt sind Sie?")

	religion = models.StringField(
		choices=['Ja', 'Nein', 'keine Angabe'],
#		verbose_name="Fühlen Sie sich einer Religionsgemeinschaft zugehörig?",
		widget=widgets.RadioSelectHorizontal)

	nationality = models.StringField(verbose_name="Was ist Ihre Staatsangehörigkeit?")

	language = models.StringField(verbose_name="Welche Muttersprache(n) sprechen Sie?")

	party = models.PositiveIntegerField(
		choices=[
			[1, 'CDU/CSU'], 
			[2, 'SPD'],
			[3, 'AfD'],
			[4, "FDP"],
			[5, "Bündnis 90/Die Grünen"],
			[6, "Die Linke"],
			[7, "andere"],
			[8, "Keine Angabe"]
		 ],
#		 verbose_name="Welche Partei würden Sie wählen, wenn am nächsten Sonntag Bundestagswahl wäre?",
		 widget=widgets.RadioSelect)

	name = models.StringField()
	seat = models.PositiveIntegerField()
	
	
#------------------------------Verständnisfragen--------------------------------------------

#Fragen Teil 1
	Q1_1 = models.IntegerField()
	Q1_2 = models.IntegerField()
	Q2_1 = models.IntegerField()
	Q2_2 = models.IntegerField()
	Q3_1 = models.IntegerField()
	Q4_1 = models.IntegerField()
	Q5_1 = models.IntegerField()
	Q6_1 = models.IntegerField()

#Fragen Teil 2
	Q1_1 = models.IntegerField()
	Q1_2 = models.IntegerField()
	Q2_1 = models.IntegerField()
	Q3_1 = models.IntegerField()
	Q4_1 = models.IntegerField()
	Q5_1 = models.IntegerField()
	Q6_1 = models.IntegerField()
	Q7_1 = models.IntegerField()	
	
	
	