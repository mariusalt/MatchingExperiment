from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Arrival(WaitPage):
#    group_by_arrival_time = True

    title_text = "Arrival Hall"
    body_text = "For this experiment, we need groups of two. \
    Please wait for another participant to log on."
#    wait_for_all_groups=True
#    def after_all_players_arrive(self):
#        self.subsession.group_randomly(fixed_id_in_group=True)

class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1

    timeout_seconds=Constants.read_timeout
    def before_next_page(self):
        self.player.define_end()



class StartWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
#    template_name = 'matching/MyWaitPage.html'
#    title_text = "Please Wait"


    def after_all_players_arrive(self):
        pass


class FischHigh(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidizer' and self.round_number == 1
    
    timeout_seconds=Constants.decision_timeout

    form_model=models.Player
    form_fields=["contri"]
    
    def contri_max(self):
        return self.player.endowment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri=1


class FischLow(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidized' and self.round_number == 1

    timeout_seconds=Constants.decision_timeout

    form_model=models.Player
    form_fields=["contri"]

    def contri_max(self):
        return self.player.endowment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri=random.randrange(0,self.player.endowment,1)

class WaitPlayer(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    def after_all_players_arrive(self):
        pass

class FischHighTable(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidizer' and self.round_number == 1

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
        if self.timeout_happened:
            self.player.zero=random.randrange(0,self.player.endowment,1)
            self.player.one=random.randrange(0,self.player.endowment,1)
            self.player.two=random.randrange(0,self.player.endowment,1)
            self.player.three=random.randrange(0,self.player.endowment,1)
            self.player.four=random.randrange(0,self.player.endowment,1)
            self.player.five=random.randrange(0,self.player.endowment,1)
        self.player.calc_cond()


    timeout_seconds=Constants.decision_timeout



class FischLowTable(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidized' and self.round_number == 1
        

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
        self.player.calc_cond()

    timeout_seconds=Constants.decision_timeout


class Result2WaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        self.group.calc_payoff()




class Result1(Page):
    def is_displayed(self):
        return self.round_number == 1
    timeout_seconds=Constants.read_timeout

    def before_next_page(self):
        self.player.condi()


    def vars_for_template(self):
        context = self.player.vars_for_template()
        if self.participant.vars['type'] == 'subsidizer' and self.group.outcome == "heads":
            context.update({'own_contri':self.player.cond,'others_contri_template':self.player.others_contri,'deci':'conditional'})

        if self.participant.vars['type'] == 'subsidized' and self.group.outcome == "tails":
            context.update({'own_contri':self.player.cond,'others_contri_template':self.player.others_contri,'deci':'conditional'})
        return context


        
class WaitToGroup(WaitPage):
    wait_for_all_groups=True
    def after_all_players_arrive(self):
        pass


        

#MATCHPOINT EXPERIMENT STARTS---------------

class Intro1(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.player.treatment=='baseline' 
    timeout_seconds=Constants.read_timeout
    def before_next_page(self):
        self.player.define_end()

class Intro2(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.player.treatment=='lowthres'
    timeout_seconds=Constants.read_timeout
    def before_next_page(self):
        self.player.define_end()

class Intro3(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.player.treatment=='highthres'
    timeout_seconds=Constants.read_timeout
    def before_next_page(self):
        self.player.define_end()

class StartWaitPage1(WaitPage):
    def is_displayed(self):
        return self.round_number == 2 

    def after_all_players_arrive(self):
        pass


class DecisionHigh(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidizer' and self.round_number == 2

    timeout_seconds=Constants.decision_timeout

    form_model=models.Player
    form_fields=["contri","t"]

    def contri_max(self):
        return self.player.endowment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri1=random.randrange(0,self.player.endowment,1)


class DecisionT(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidizer' and self.round_number == 2

    timeout_seconds=Constants.decision_timeout

    form_model=models.Player
    form_fields=["t"]

    def before_next_page(self):
        if self.timeout_happened:
            self.player.t=70#random.randrange(0,120,10)

class TWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 2
    def after_all_players_arrive(self):
        pass


class DecisionLow(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidized' and self.round_number == 2

    timeout_seconds=Constants.decision_timeout

    form_model=models.Player
    form_fields=["t0","t10","t20","t30","t40","t50","t60","t70","t80","t90","t100","t110","t120"]

    def t0_max(self):
        return self.player.endowment
    def t10_max(self):
        return self.player.endowment
    def t20_max(self):
        return self.player.endowment
    def t30_max(self):
        return self.player.endowment
    def t40_max(self):
        return self.player.endowment
    def t50_max(self):
        return self.player.endowment
    def t60_max(self):
        return self.player.endowment
    def t70_max(self):
        return self.player.endowment
    def t80_max(self):
        return self.player.endowment
    def t90_max(self):
        return self.player.endowment
    def t100_max(self):
        return self.player.endowment
    def t110_max(self):
        return self.player.endowment
    def t120_max(self):
        return self.player.endowment

    def vars_for_template(self):
        return self.player.vars_for_template1()

    def before_next_page(self):
        if self.timeout_happened:
            self.player.t0=1#random.randrange(0,self.player.endowment,1)
            self.player.t10=1#random.randrange(0,self.player.endowment,1)
            self.player.t20=1#random.randrange(0,self.player.endowment,1)
            self.player.t30=1#random.randrange(0,self.player.endowment,1)
            self.player.t40=1#random.randrange(0,self.player.endowment,1)
            self.player.t50=1#random.randrange(0,self.player.endowment,1)
            self.player.t60=1#random.randrange(0,self.player.endowment,1)
            self.player.t70=1#random.randrange(0,self.player.endowment,1)
            self.player.t80=1#random.randrange(0,self.player.endowment,1)
            self.player.t90=1#random.randrange(0,self.player.endowment,1)
            self.player.t100=1#random.randrange(0,self.player.endowment,1)
            self.player.t110=1#random.randrange(0,self.player.endowment,1)
            self.player.t120=1#random.randrange(0,self.player.endowment,1)
        self.player.calc_cond1()


class Result3WaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 2 and self.player.treatment=='baseline'
    def after_all_players_arrive(self):
        self.group.calc_payoff1()


class Result4WaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 2 and self.player.treatment=='lowthres'
    def after_all_players_arrive(self):
        self.group.calc_payoff2()


class Result5WaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 2 and self.player.treatment=='highthres'
    def after_all_players_arrive(self):
        self.group.calc_payoff3()


class Result2(Page):
    def is_displayed(self):
        return self.round_number == 2

    timeout_seconds=Constants.read_timeout

    def vars_for_template(self):
        return self.player.vars_for_result()
    def before_next_page(self):
        self.player.total_payoff()

class Questionnaire(Page):
    def is_displayed(self):
        return self.round_number == 2

    form_model = models.Player
    form_fields = ['age', 'gender', 'education', 'studies', 'occupation']

    timeout_seconds = Constants.read_timeout

    def error_message(self, values):
        if values['education'] >= 3 and not values['studies']:
            return 'Bitte teilen Sie uns ihr Studienfach mit.'

class Thanks(Page):
    def is_displayed(self):
        return self.round_number == 2



page_sequence = [
    Arrival,
    Intro,
    StartWaitPage,
    FischHigh,
    FischLow,
    WaitPlayer,
    FischHighTable,
    FischLowTable,
    Result2WaitPage,
    Result1,
    WaitToGroup,
    Intro1,
    Intro2,
    Intro3,
    StartWaitPage1,
    DecisionHigh,
    TWaitPage,
    DecisionLow,
    Result3WaitPage,
    Result4WaitPage,
    Result5WaitPage,
    Result2,
    Questionnaire,
    Thanks
]