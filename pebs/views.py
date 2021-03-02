from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random


class A_Start(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        self.participant.vars['expiry'] = time.time()+120

class B_Effort(Page):
	form_model=models.Player
	def get_form_fields(self):
#		Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#		Numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#		random.shuffle(Letters)
#		random.shuffle(Numbers)
#		Codes={}		
#		for i in range(8):
#			Codes[Letters[i]]=Numbers[i]
#		Eins=list(Codes.keys())[0]
#		Zwei=list(Codes.keys())[1]
#		Drei=list(Codes.keys())[2]
#		Vier=list(Codes.keys())[3]
#		Funf=list(Codes.keys())[4]
#		Sechs=list(Codes.keys())[5]
#		Sieben=list(Codes.keys())[6]
#		Acht=list(Codes.keys())[7]


		return [""+self.player.Eins+"",""+self.player.Zwei+"",""+self.player.Drei+"",""+self.player.Vier+"",""+self.player.Funf+"",""+self.player.Sechs+"",""+self.player.Sieben+"",""+self.player.Acht+""]

	def A_error_message(self,value):
			if not (value==self.player.Numbers[0]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def B_error_message(self,value):
			if not (value==self.player.Numbers[1]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def C_error_message(self,value):
			if not (value==self.player.Numbers[2]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def D_error_message(self,value):
			if not (value==self.player.Numbers[3]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def E_error_message(self,value):
			if not (value==self.player.Numbers[4]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def F_error_message(self,value):
			if not (value==self.player.Numbers[5]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def G_error_message(self,value):
			if not (value==self.player.Numbers[6]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def H_error_message(self,value):
			if not (value==self.player.Numbers[7]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def I_error_message(self,value):
			if not (value==self.player.Numbers[8]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'
	def J_error_message(self,value):
			if not (value==self.player.Numbers[9]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def K_error_message(self,value):
			if not (value==self.player.Numbers[10]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def L_error_message(self,value):
			if not (value==self.player.Numbers[11]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def M_error_message(self,value):
			if not (value==self.player.Numbers[12]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def N_error_message(self,value):
			if not (value==self.player.Numbers[13]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def O_error_message(self,value):
			if not (value==self.player.Numbers[14]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def P_error_message(self,value):
			if not (value==self.player.Numbers[15]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def Q_error_message(self,value):
			if not (value==self.player.Numbers[16]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def R_error_message(self,value):
			if not (value==self.player.Numbers[17]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def S_error_message(self,value):
			if not (value==self.player.Numbers[18]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def T_error_message(self,value):
			if not (value==self.player.Numbers[19]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def U_error_message(self,value):
			if not (value==self.player.Numbers[20]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def V_error_message(self,value):
			if not (value==self.player.Numbers[21]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def W_error_message(self,value):
			if not (value==self.player.Numbers[22]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def X_error_message(self,value):
			if not (value==self.player.Numbers[23]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def Y_error_message(self,value):
			if not (value==self.player.Numbers[24]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'

	def Z_error_message(self,value):
			if not (value==self.player.Numbers[25]):
				return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'


















	timer_text = 'Time left to complete this task:'

	def get_timeout_seconds(self):
		return self.participant.vars['expiry'] - time.time()
	def is_displayed(self):
		return self.participant.vars['expiry'] - time.time() > 3


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
	def is_displayed(self):
		return self.participant.vars['expiry'] - time.time() < 3


page_sequence = [
	A_Start,
    B_Effort,
    ResultsWaitPage,
    Results
]
