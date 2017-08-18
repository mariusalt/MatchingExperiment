from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Arrival(WaitPage):
    group_by_arrival_time = True

    title_text = "Arrival Hall"
    body_text = "For this experiment, we need groups of two. \
    Please wait for another participant to log on."
    def after_all_players_arrive(self):
        pass

class Intro(Page):
    timeout_seconds=Constants.read_timeout
    def before_next_page(self):
        self.player.define_end()



class StartWaitPage(WaitPage):
#    template_name = 'matching/MyWaitPage.html'
#    title_text = "Please Wait"

    def after_all_players_arrive(self):
        pass


class FischHigh(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    timeout_seconds=Constants.read_timeout

    form_model=models.Player
    form_fields=["contri"]
    
    def contri_max(self):
        return self.player.endowment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri=1


class FischLow(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    timeout_seconds=Constants.read_timeout

    form_model=models.Player
    form_fields=["contri"]

    def contri_max(self):
        return self.player.endowment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri=random.randrange(0,self.player.endowment,1)


class FischHighTable(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
        pass

    form_model=models.Player
    form_fields=["five","four","three","two","one","zero"]

    def zero_max(self):
        return self.player.endowment
    def one_max(self):
        return self.player.endowment
    def two_max(self):
        return self.player.endowment
    def three_max(self):
        return self.player.endowment
    def four_max(self):
        return self.player.endowment
    def five_max(self):
        return self.player.endowment


    def before_next_page(self):
        self.player.calc_cond()
        self.group.rand()
        self.player.calc_payoff2()
        if self.timeout_happened:
            self.player.zero=random.randrange(0,self.player.endowment,1)
            self.player.one=random.randrange(0,self.player.endowment,1)
            self.player.two=random.randrange(0,self.player.endowment,1)
            self.player.three=random.randrange(0,self.player.endowment,1)
            self.player.four=random.randrange(0,self.player.endowment,1)
            self.player.five=random.randrange(0,self.player.endowment,1)


    timeout_seconds=Constants.decision_timeout



class FischLowTable(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2
        

    form_model=models.Player
    form_fields=["ten","nine","eight","seven","six","five","four","three","two","one","zero"]

    def zero_max(self):
        return self.player.endowment
    def one_max(self):
        return self.player.endowment
    def two_max(self):
        return self.player.endowment
    def three_max(self):
        return self.player.endowment
    def four_max(self):
        return self.player.endowment
    def five_max(self):
        return self.player.endowment
    def six_max(self):
        return self.player.endowment
    def seven_max(self):
        return self.player.endowment
    def eight_max(self):
        return self.player.endowment
    def nine_max(self):
        return self.player.endowment
    def ten_max(self):
        return self.player.endowment

    def before_next_page(self):
        self.player.calc_cond()
        self.group.rand()
        self.player.calc_payoff2()
        if self.timeout_happened:
            self.player.zero=random.randrange(0,self.player.endowment,1)
            self.player.one=random.randrange(0,self.player.endowment,1)
            self.player.two=random.randrange(0,self.player.endowment,1)
            self.player.three=random.randrange(0,self.player.endowment,1)
            self.player.four=random.randrange(0,self.player.endowment,1)
            self.player.five=random.randrange(0,self.player.endowment,1)
            self.player.six=random.randrange(0,self.player.endowment,1)
            self.player.seven=random.randrange(0,self.player.endowment,1)
            self.player.eight=random.randrange(0,self.player.endowment,1)
            self.player.nine=random.randrange(0,self.player.endowment,1)
            self.player.ten=random.randrange(0,self.player.endowment,1)

    timeout_seconds=Constants.decision_timeout


class Result2WaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Result1(Page):
    timeout_seconds=Constants.read_timeout

    def vars_for_template(self):
        if self.player.id_in_group == 1:
            if self.group.outcome == "heads":
                return {'deci':'conditional'}
            else:
                return {'deci':'unconditional'}
            return {'others_payoff': self.get_others_in_group()[0].payoffFisch}
        if self.player.id_in_group == 2:
            if self.group.outcome == "heads":
                return {'deci':'unconditional'}
            else:
                return {'deci':'conditional'}
            return {'others_payoff': self.get_others_in_group()[0].payoffFisch}

        

#MATCHPOINT EXPERIMENT STARTS---------------

class Intro1(Page):
    timeout_seconds=Constants.read_timeout

class StartWaitPage1(WaitPage):

    def after_all_players_arrive(self):
        pass

class DecisionHigh(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    timeout_seconds=Constants.decision_timeout

    form_model=models.Player
    form_fields=["contri1"]

    def contri1_max(self):
        return self.player.endowment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri1=random.randrange(0,self.player.endowment,1)


class DecisionLow(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    timeout_seconds=Constants.decision_timeout

    form_model=models.Player
    form_fields=["contri1"]

    def contri1_max(self):
        return self.player.endowment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri1=random.randrange(0,self.player.endowment,1)
    

class DecisionT(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    timeout_seconds=Constants.decision_timeout

    form_model=models.Player
    form_fields=["t"]

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri1=random.randrange(0,2.5,0.1)

 #   def before_next_page(self):
 #       self.group.calc_payoff1()
 #       self.player.calc_payoff2()



class Result3WaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.calc_payoff1()


class Result2(Page):
    def vars_for_template(self):
        return {'total_payoff': self.player.payoffFisch+self.player.payoff}






page_sequence = [
    Arrival,
    Intro,
    StartWaitPage,
    FischHigh,
    FischLow,
    FischHighTable,
    FischLowTable,
    Result2WaitPage,
    Result1,
    Intro1,
    StartWaitPage1,
    DecisionHigh,
    DecisionLow,
    DecisionT, 
    Result3WaitPage,
    Result2
]