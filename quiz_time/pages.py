from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model=models.Player
    form_fields=["question","submitted_answer"]

    def submitted_answer_choices(self):
        qd = self.player.current_question()
        return [
            qd['option1'],
            qd['option2'],
            qd['option3'],
        ]

    def before_next_page(self):
    	self.player.check_correct()




class Results(Page):
    def is_displayed(self):
    	return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }

#        inner_list[]
#        for p in player_in_all_rounds:
#        	inner_list.append(p.is_correct) 
        #player_in _all_rounds looks like this
        #[player_round1,player_round2,...]
        #->[True,False,False,...]
        #sum(inner-list)
        #True can be evaluated as a 1 and Flase as a 0


page_sequence = [
    MyPage,
    Results
]
