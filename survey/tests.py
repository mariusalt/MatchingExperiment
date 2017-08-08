from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

from otree.api import SubmissionMustFail


class PlayerBot(Bot):

    def play_round(self):
    	yield SubmissionMustFail(views.Page1,{'age':27,'gender':"male",'field_of_studies':"econ",'height':1.80,'weight':-10})
    	yield (views.Page1, {'age':27,'gender':"male",'field_of_studies':"econ",'height':1.00,'weight':100})
    	assert self.player.bmi == 100
    	assert self.player.bmi_class == "overweight"
    	yield(views.Page2)
        
        
