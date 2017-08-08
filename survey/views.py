from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    form_model=models.Player
    form_fields=["age","gender","field_of_studies","height","weight"]

    def before_next_page(self):
    	self.player.calculate_bmi()
    	self.player.category()
        
    







class Page2(Page):
    pass

#    def vars_for_template(self):
 #   	return {
  #  	    'bmi': self.player.weight/(self.player.height**2)
   # 	}



page_sequence = [
    Page1,
    WaitPage,
    Page2
]
