from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from random import randint


author = 'Marius Alt'

doc = """
Pro-Environmental Behavioral Spillover Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'pebs'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
	pass

#	if self.round_number== 1|2|3|4|5|6|7|8|9|10
#	    Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#		Numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#	#	random.shuffle(Letters)
#	#	random.shuffle(Numbers)
#		Codes={}		
#		for i in range(8):
#			Codes[Letters[i]]=Numbers[i]
#		Letsub=[]
#		for i in range(8):
#			b=randint(0,(25-i))
#			k=Letters[b]
#			Letsub.append(k)
#			del Letters[b]
#
#
#		Eins=Letsub[0]
#		Zwei=Letsub[1]
#		Drei=Letsub[2]
#		Vier=Letsub[3]
#		Funf=Letsub[4]
#		Sechs=Letsub[5]
#		Sieben=Letsub[6]
#		Acht=Letsub[7]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	A=models.IntegerField()
	B=models.IntegerField()
	C=models.IntegerField()
	D=models.IntegerField()
	E=models.IntegerField()
	F=models.IntegerField()
	G=models.IntegerField()
	H=models.IntegerField()
	I=models.IntegerField()
	J=models.IntegerField()
	K=models.IntegerField()
	L=models.IntegerField()	
	M=models.IntegerField()
	N=models.IntegerField()
	O=models.IntegerField()
	P=models.IntegerField()
	Q=models.IntegerField()
	R=models.IntegerField()
	S=models.IntegerField()
	T=models.IntegerField()
	U=models.IntegerField()
	V=models.IntegerField()
	W=models.IntegerField()
	X=models.IntegerField()
	Y=models.IntegerField()
	Z=models.IntegerField()

	Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	Numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#	random.shuffle(Letters)
#	random.shuffle(Numbers)
	Codes={}		
	for i in range(8):
		Codes[Letters[i]]=Numbers[i]
	Letsub=[]
	for i in range(8):
		b=randint(0,(25-i))
		k=Letters[b]
		Letsub.append(k)
		del Letters[b]


	Eins=Letsub[0]
	Zwei=Letsub[1]
	Drei=Letsub[2]
	Vier=Letsub[3]
	Funf=Letsub[4]
	Sechs=Letsub[5]
	Sieben=Letsub[6]
	Acht=Letsub[7]