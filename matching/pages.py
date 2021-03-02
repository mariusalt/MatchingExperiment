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
class A_Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1

class B_Procedure(Page):
    def is_displayed(self):
        return self.round_number == 1 

class C_Rules(Page):
    def is_displayed(self):
        return self.round_number == 1 

class D_DescDecisionI(Page):
    def is_displayed(self):
        return self.round_number == 1 

class E_DescPaymentI(Page):
    def is_displayed(self):
        return self.round_number == 1 

class EG_Control(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model=models.Player
    form_fields=["Q1_1","Q1_2","Q2_1","Q2_2","Q3_1","Q4_1","Q5_1","Q6_1"]

    
    def Q1_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==36):
               return 'Vergütung Teil I für Spieler 1 = (30 - 15) + 0,7·(15 + 15)'
        if self.player.treatment != 'base':
            if not (value==46):
                return 'Vergütung Teil I für Spieler 1  = (40 - 15) + 0,7·(15 + 15)'

    def Q1_2_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==36):
                return 'Vergütung Teil I für Spieler 2  = (30 - 15) + 0,7·(15 + 15)'
        if self.player.treatment != 'base':
            if not (value==26):
                return 'Vergütung Teil I für Spieler 2 = (20 - 15) + 0,7·(15 + 15)'

    def Q2_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==30):
                return 'Vergütung Teil I für Spieler 2  = (30 - 0) + 0,7·(0 + 0)'
        if self.player.treatment != 'base':
            if not (value==20):
                return 'Vergütung Teil I für Spieler 2  = (20 - 0) + 0,7·(0 + 0)'
    
    def Q2_2_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==30):
                return 'Vergütung Teil I für Spieler 1 = (30 - 0) + 0,7·(0 + 0)'
        if self.player.treatment != 'base':
            if not (value==40):
                return 'Vergütung Teil I für Spieler 1  = (40 - 0) + 0,7·(0 + 0)'
    
    def Q3_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==0):
                A='niedrigster Beitrag: Vergütung Teil I für Spieler 1  = (30 - 0) + 0,7·(0 + 20).'
                B='höchster Beitrag: Vergütung Teil I für Spieler 1  = (30 - 30) + 0,7·(30 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]

        if self.player.treatment != 'base':
            if not (value==0):
                A='niedrigster Beitrag: Vergütung Teil I für Spieler 1  = (40 - 0) + 0,7·(0 + 20).'
                B='höchster Beitrag: Vergütung Teil I für Spieler 1  = (40 - 40) + 0,7·(40 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]
                
    def Q4_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==30):
                A='niedrigster Beitrag: Vergütung Teil I für Spieler 1  = (30 - 0) + 0,7·(0 + 20) addiert mit Vergütung Teil I Spieler 2 = (30 - 20) + 0,7·(0 + 20).'
                B='höchster Beitrag: Vergütung Teil I für Spieler 1  = (30 - 30) + 0,7·(30 + 20) addiert mit Vergütung Teil I Spieler 2 = (30 - 20) + 0,7·(30 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]
                
        if self.player.treatment != 'base':
            if not (value==40):
                A='niedrigster Beitrag: Vergütung Teil I für Spieler 1  = (40 - 0) + 0,7·(0 + 20) addiert mit Vergütung Teil I Spieler 2 = (20 - 20) + 0,7·(0 + 20).'
                B='höchster Beitrag: Vergütung Teil I für Spieler 1  = (40 - 40) + 0,7·(40 + 20) addiert mit Vergütung Teil I Spieler 2 = (20 - 20) + 0,7·(40 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]
    
    def Q5_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==0):
                A='niedrigster Beitrag: Vergütung Teil I für Spieler 1  = (30 - 0) + 0,7·(0 + 0).'
                B='höchster Beitrag: Vergütung Teil I für Spieler 1  = (30 - 30) + 0,7·(30 + 0).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]
        if self.player.treatment != 'base':
            if not (value==0):
                A='niedrigster Beitrag: Vergütung Teil I für Spieler 1  = (40 - 0) + 0,7·(0 + 0).'
                B='höchster Beitrag: Vergütung Teil I für Spieler 1  = (40 - 40) + 0,7·(40 + 0).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]
    
    def Q6_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==30):
                A='niedrigster Beitrag: Vergütung Teil I für Spieler 1  = (30 - 0) + 0,7·(0 + 0) addiert mit Vergütung Teil I Spieler 2 = (30 - 0) + 0,7·(0 + 0).'
                B='höchster Beitrag: Vergütung Teil I für Spieler 1  = (30 - 30) + 0,7·(30 + 0) addiert mit Vergütung Teil I Spieler 2 = (30 - 0) + 0,7·(30 + 0).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]
        if self.player.treatment != 'base':
            if not (value==40):
                A='niedrigster Beitrag: Vergütung Teil I für Spieler 1  = (40 - 0) + 0,7·(0 + 0) addiert mit Vergütung Teil I Spieler 2 = (20 - 0) + 0,7·(0 + 0).'
                B='höchster Beitrag: Vergütung Teil I für Spieler 1  = (40 - 40) + 0,7·(40 + 0) addiert mit Vergütung Teil I Spieler 2 = (20 - 0) + 0,7·(40 + 0).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]
    
    

class G_Player(Page):
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        self.player.define_end()

class WaitToGroup(WaitPage):
    wait_for_all_groups=True
    def after_all_players_arrive(self):
        pass

class H_FischUncondi(Page):
    def is_displayed(self):
        return  self.round_number == 1
    

    form_model=models.Player
    form_fields=["contri"]
    
    def contri_max(self):
        return self.player.endowment


    def before_next_page(self):
        if self.timeout_happened:
            self.player.contri=random.randrange(0,self.player.endowment,1)





class WaitPlayer(WaitPage):
    def after_all_players_arrive(self):
        pass

class I_FischCondiRichTable(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidizer' and self.round_number == 1 and self.player.treatment != 'base'

    form_model=models.Player
    form_fields=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]

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
    def eleven_max(self):
        return self.player.endowment
    def twelve_max(self):
        return self.player.endowment
    def thirteen_max(self):
        return self.player.endowment
    def fourteen_max(self):
        return self.player.endowment
    def fifteen_max(self):
        return self.player.endowment
    def sixteen_max(self):
        return self.player.endowment
    def seventeen_max(self):
        return self.player.endowment
    def eighteen_max(self):
        return self.player.endowment
    def nineteen_max(self):
        return self.player.endowment      
    def twenty_max(self):
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
            self.player.elven=random.randrange(0,self.player.endowment,1)
            self.player.twelve=random.randrange(0,self.player.endowment,1)
            self.player.thirteen=random.randrange(0,self.player.endowment,1)
            self.player.fourteen=random.randrange(0,self.player.endowment,1)
            self.player.fifteen=random.randrange(0,self.player.endowment,1)
            self.player.sixteen=random.randrange(0,self.player.endowment,1)
            self.player.seventeen=random.randrange(0,self.player.endowment,1)
            self.player.eighteen=random.randrange(0,self.player.endowment,1)
            self.player.nineteen=random.randrange(0,self.player.endowment,1)
            self.player.twenty=random.randrange(0,self.player.endowment,1)
        self.player.calc_others_contri()
        self.player.calc_cond()






class I_FischCondiPoorTable(Page):
    def is_displayed(self):
        return self.participant.vars['type'] == 'subsidized' and self.round_number == 1 and self.player.treatment != 'base'
        

    form_model=models.Player
    form_fields=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen", "seventeen","eighteen","nineteen","twenty", "twentyone","twentytwo","twentythree","twentyfour","twentyfive","twentysix","twentyseven","twentyeight","twentynine","thirty","thirtyone","thirtytwo","thirtythree","thirtyfour","thirtyfive","thirtysix","thirtyseven","thirtyeight","thirtynine","fourty"]

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
    def eleven_max(self):
        return self.player.endowment
    def twelve_max(self):
        return self.player.endowment
    def thirteen_max(self):
        return self.player.endowment
    def fourteen_max(self):
        return self.player.endowment
    def fifteen_max(self):
        return self.player.endowment
    def sixteen_max(self):
        return self.player.endowment
    def seventeen_max(self):
        return self.player.endowment
    def eighteen_max(self):
        return self.player.endowment
    def nineteen_max(self):
        return self.player.endowment      
    def twenty_max(self):
        return self.player.endowment
    def twentyone_max(self):
        return self.player.endowment
    def twentytwo_max(self):
        return self.player.endowment
    def twentythree_max(self):
        return self.player.endowment
    def twentyfour_max(self):
        return self.player.endowment
    def twentyfive_max(self):
        return self.player.endowment
    def twentysix_max(self):
        return self.player.endowment
    def twentyseven_max(self):
        return self.player.endowment
    def twentyeight_max(self):
        return self.player.endowment
    def twentynine_max(self):
        return self.player.endowment
    def thirty_max(self):
        return self.player.endowment
    def thirtyone_max(self):
        return self.player.endowment
    def thirtytwo_max(self):
        return self.player.endowment
    def thirtythree_max(self):
        return self.player.endowment
    def thirtyfour_max(self):
        return self.player.endowment
    def thirtyfive_max(self):
        return self.player.endowment
    def thirtysix_max(self):
        return self.player.endowment
    def thirtyseven_max(self):
        return self.player.endowment
    def thirtyeight_max(self):
        return self.player.endowment
    def thirtynine_max(self):
        return self.player.endowment
    def fourty_max(self):
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
            self.player.elven=random.randrange(0,self.player.endowment,1)
            self.player.twelve=random.randrange(0,self.player.endowment,1)
            self.player.thirteen=random.randrange(0,self.player.endowment,1)
            self.player.fourteen=random.randrange(0,self.player.endowment,1)
            self.player.fifteen=random.randrange(0,self.player.endowment,1)
            self.player.sixteen=random.randrange(0,self.player.endowment,1)
            self.player.seventeen=random.randrange(0,self.player.endowment,1)
            self.player.eighteen=random.randrange(0,self.player.endowment,1)
            self.player.nineteen=random.randrange(0,self.player.endowment,1)
            self.player.twenty=random.randrange(0,self.player.endowment,1)
            self.player.twentyone=random.randrange(0,self.player.endowment,1)
            self.player.twentytwo=random.randrange(0,self.player.endowment,1)
            self.player.twentythree=random.randrange(0,self.player.endowment,1)
            self.player.twentyfour=random.randrange(0,self.player.endowment,1)
            self.player.twentyfive=random.randrange(0,self.player.endowment,1)
            self.player.twentysix=random.randrange(0,self.player.endowment,1)
            self.player.twentyseven=random.randrange(0,self.player.endowment,1)
            self.player.twentyeight=random.randrange(0,self.player.endowment,1)
            self.player.twentynine=random.randrange(0,self.player.endowment,1)
            self.player.thirty=random.randrange(0,self.player.endowment,1)
            self.player.thirtyone=random.randrange(0,self.player.endowment,1)
            self.player.thirtytwo=random.randrange(0,self.player.endowment,1)
            self.player.thirtythree=random.randrange(0,self.player.endowment,1)
            self.player.thirtyfour=random.randrange(0,self.player.endowment,1)
            self.player.thirtyfive=random.randrange(0,self.player.endowment,1)
            self.player.thirtysix=random.randrange(0,self.player.endowment,1)
            self.player.thirtyseven=random.randrange(0,self.player.endowment,1)
            self.player.thirtyeight=random.randrange(0,self.player.endowment,1)
            self.player.thirtynine=random.randrange(0,self.player.endowment,1)
            self.player.fourty=random.randrange(0,self.player.endowment,1)
        self.player.calc_others_contri()
        self.player.calc_cond()



class I_FischCondiBaselineTable(Page):
    def is_displayed(self):
        return self.player.treatment == 'base' and self.round_number == 1

    form_model=models.Player
    form_fields=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen", "sixteen", "seventeen","eighteen","nineteen","twenty", "twentyone","twentytwo","twentythree","twentyfour","twentyfive","twentysix","twentyseven","twentyeight","twentynine","thirty"]

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
    def eleven_max(self):
        return self.player.endowment
    def twelve_max(self):
        return self.player.endowment
    def thirteen_max(self):
        return self.player.endowment
    def fourteen_max(self):
        return self.player.endowment
    def fifteen_max(self):
        return self.player.endowment
    def sixteen_max(self):
        return self.player.endowment
    def seventeen_max(self):
        return self.player.endowment
    def eighteen_max(self):
        return self.player.endowment
    def nineteen_max(self):
        return self.player.endowment      
    def twenty_max(self):
        return self.player.endowment
    def twentyone_max(self):
        return self.player.endowment
    def twentytwo_max(self):
        return self.player.endowment
    def twentythree_max(self):
        return self.player.endowment
    def twentyfour_max(self):
        return self.player.endowment
    def twentyfive_max(self):
        return self.player.endowment
    def twentysix_max(self):
        return self.player.endowment
    def twentyseven_max(self):
        return self.player.endowment
    def twentyeight_max(self):
        return self.player.endowment
    def twentynine_max(self):
        return self.player.endowment
    def thirty_max(self):
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
            self.player.elven=random.randrange(0,self.player.endowment,1)
            self.player.twelve=random.randrange(0,self.player.endowment,1)
            self.player.thirteen=random.randrange(0,self.player.endowment,1)
            self.player.fourteen=random.randrange(0,self.player.endowment,1)
            self.player.fifteen=random.randrange(0,self.player.endowment,1)
            self.player.sixteen=random.randrange(0,self.player.endowment,1)
            self.player.seventeen=random.randrange(0,self.player.endowment,1)
            self.player.eighteen=random.randrange(0,self.player.endowment,1)
            self.player.nineteen=random.randrange(0,self.player.endowment,1)
            self.player.twenty=random.randrange(0,self.player.endowment,1)
            self.player.twentyone=random.randrange(0,self.player.endowment,1)
            self.player.twentytwo=random.randrange(0,self.player.endowment,1)
            self.player.twentythree=random.randrange(0,self.player.endowment,1)
            self.player.twentyfour=random.randrange(0,self.player.endowment,1)
            self.player.twentyfive=random.randrange(0,self.player.endowment,1)
            self.player.twentysix=random.randrange(0,self.player.endowment,1)
            self.player.twentyseven=random.randrange(0,self.player.endowment,1)
            self.player.twentyeight=random.randrange(0,self.player.endowment,1)
            self.player.twentynine=random.randrange(0,self.player.endowment,1)
            self.player.thirty=random.randrange(0,self.player.endowment,1)
        self.player.calc_others_contri()
        self.player.calc_cond()





class Result2WaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        self.group.calc_payoff()




class J_Result1(Page):
    def is_displayed(self):
        return self.round_number == 1
    timeout_seconds=Constants.read_timeout

    def before_next_page(self):
        self.player.condi()


    def vars_for_template(self):
        context = self.player.vars_for_template()
        if self.participant.vars['type'] == 'subsidizer' and self.group.outcome == "heads":
            context.update({'own_contri':self.player.cond,'others_contri_template':self.player.others_contri,'deci':'bedingte'})

        if self.participant.vars['type'] == 'subsidized' and self.group.outcome == "tails":
            context.update({'own_contri':self.player.cond,'others_contri_template':self.player.others_contri,'deci':'bedingte'})
        return context


        
class WaitToGroup(WaitPage):
    wait_for_all_groups=True
    def after_all_players_arrive(self):
        pass


        

#MATCHPOINT EXPERIMENT STARTS-----------------------------------------------------------------------
class K_WelcomeII(Page):
    def is_displayed(self):
        return self.round_number == 2

class L_RulesII(Page):
    def is_displayed(self):
        return self.round_number == 2 

class M_DescDecisionIIPlayer1(Page):
    def is_displayed(self):
        return self.round_number == 2 

class M_DescDecisionIIPlayer2(Page):
    def is_displayed(self):
        return self.round_number == 2 

class M_DescPaymentII(Page):
    def is_displayed(self):
        return self.round_number == 2

class O_MatchPlayer(Page):
    def is_displayed(self):
        return self.round_number == 2
    def before_next_page(self):
        self.player.define_end()


class N_Control(Page):
    def is_displayed(self):
        return self.round_number == 2

    form_model=models.Player
    form_fields=["Q1_1","Q1_2","Q2_1","Q3_1","Q4_1","Q5_1","Q6_1","Q7_1"]

    def Q1_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==38):
                A= 'Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (30 - 20) + 0,7·(20 + 20).'
                return [A,B]
        if self.player.treatment == 'baseline':
            if not (value==48):
                A= 'Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 20) + 0,7·(20 + 20).'
                return [A,B]
        if self.player.treatment == 'lowthres':
            if not (value==48):
                A= 'Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 20) + 0,7·(20 + 20).'
                return [A,B]
        if self.player.treatment == 'highthres':
            if not (value==48):
                A= 'Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 20) + 0,7·(20 + 20).'
                return [A,B]

    def Q1_2_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==38):
                A= 'Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20.'
                B= 'Berechnung der Vergütung Teil II für Spieler 2  = (30 - 20) + 0,7·(20 + 20).'
                return [A,B]
        if self.player.treatment == 'baseline':
            if not (value==28):
                A= 'Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20.'
                B= 'Berechnung der Vergütung Teil II für Spieler 2  = (20 - 20) + 0,7·(20 + 20).'
                return [A,B]
        if self.player.treatment == 'lowthres':
            if not (value==28):
                A= 'Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20.'
                B= 'Berechnung der Vergütung Teil II für Spieler 2  = (20 - 20) + 0,7·(20 + 20).'
                return [A,B]
        if self.player.treatment == 'highthres':
            if not (value==28):
                A= 'Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20.'
                B= 'Berechnung der Vergütung Teil II für Spieler 2  = (20 - 20) + 0,7·(20 + 20).'
                return [A,B]
    
    def Q2_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==0):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (0 % · 20) = 0 einsetzen in Vergütung Teil II für Spieler 1  = (30 - 0) + 0,7·(0 + 20).'
                B='Beitrag in Höhe Ihrer Anfangsausstattung: Berechnung des Beitrags von Spieler 1 = (150 % · 20) = 30 einsetzen in Vergütung Teil II für Spieler 1  = (30 - 30) + 0,7·(30 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Faktor in % Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]           

        if self.player.treatment == 'baseline':
            if not (value==0):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (0 % · 20) = 0 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 0) + 0,7·(0 + 20).'
                B='Beitrag in Höhe Ihrer Anfangsausstattung: Berechnung des Beitrags von Spieler 1 = (200 % · 20) = 40 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 40) + 0,7·(40 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Faktor in % Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]

        if self.player.treatment == 'lowthres':
            if not (value==0):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (0 % · 20) = 0 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 0) + 0,7·(0 + 20).'
                B='Beitrag in Höhe Ihrer Anfangsausstattung: Berechnung des Beitrags von Spieler 1 = (200 % · 20) = 40 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 40) + 0,7·(40 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Faktor in % Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]

        if self.player.treatment == 'highthres':
            if not (value==0):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (0 % · 20) = 0 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 0) + 0,7·(0 + 20).'
                B='Beitrag in Höhe Ihrer Anfangsausstattung: Berechnung des Beitrags von Spieler 1 = (200 % · 20) = 40 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 40) + 0,7·(40 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Faktor in % Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]

   
    def Q3_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==300):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (0 % · 20) = 0 einsetzen in Vergütung Teil II für Spieler 1  = (30 - 0) + 0,7·(0 + 20) und addiert mit Vergütung Teil II Spieler 2 = (30 - 20) + 0,7·(0 + 20).'
                B='höchster Beitrag: Berechnung des Beitrags von Spieler 1 = (300 % · 20) = 60 einsetzen in Vergütung Teil II für Spieler 1  = (30 - 60) + 0,7·(60 + 20) und addiert mit Vergütung Teil II Spieler 2 = (30 - 20) + 0,7·(60 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Faktor in % Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]           

        if self.player.treatment == 'baseline':
            if not (value==300):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (0 % · 20) = 0 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 0) + 0,7·(0 + 20) und addiert mit Vergütung Teil II Spieler 2 = (20 - 20) + 0,7·(0 + 20).'
                B='höchster Beitrag: Berechnung des Beitrags von Spieler 1 = (300 % · 20) = 60 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 60) + 0,7·(60 + 20) und addiert mit Vergütung Teil II Spieler 2 = (20 - 20) + 0,7·(60 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Faktor in % Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]

        if self.player.treatment == 'lowthres':
            if not (value==300):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (0 % · 20) = 0 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 0) + 0,7·(0 + 20) und addiert mit Vergütung Teil II Spieler 2 = (20 - 20) + 0,7·(0 + 20).'
                B='höchster Beitrag: Berechnung des Beitrags von Spieler 1 = (300 % · 20) = 60 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 60) + 0,7·(60 + 20) und addiert mit Vergütung Teil II Spieler 2 = (20 - 20) + 0,7·(60 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Faktor in % Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]
        if self.player.treatment == 'highthres':
            if not (value==300):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (0 % · 20) = 0 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 0) + 0,7·(0 + 20) und addiert mit Vergütung Teil II Spieler 2 = (20 - 20) + 0,7·(0 + 20).'
                B='höchster Beitrag: Berechnung des Beitrags von Spieler 1 = (300 % · 20) = 60 einsetzen in Vergütung Teil II für Spieler 1  = (40 - 60) + 0,7·(60 + 20) und addiert mit Vergütung Teil II Spieler 2 = (20 - 20) + 0,7·(60 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Faktor in % Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]

    def Q4_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==30):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (100 % · 0) = 0 einsetzen in Vergütung Teil II für Spieler 2  = (30 - 0) + 0,7·(0 + 0).'
                B='höchster Beitrag: Berechnung des Beitrags von Spieler 1 = (100 % · 30) = 30 einsetzen in Vergütung Teil II für Spieler 2  = (30 - 30) + 0,7·(30 + 30).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]

        if self.player.treatment != 'base':
            if not (value==20):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (100 % · 0) = 0 einsetzen in Vergütung Teil II für Spieler 2  = (20 - 0) + 0,7·(0 + 0).'
                B='höchster Beitrag: Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20 einsetzen in Vergütung Teil II für Spieler 2  = (20 - 20) + 0,7·(20 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste individuelle Vergütung erzielen.'
                return [A,B,C]        

    def Q5_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==30):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (100 % · 0) = 0 einsetzen in Vergütung Teil II für Spieler 2  = (30 - 0) + 0,7·(0 + 0) und addiert mit Vergütung Teil II Spieler 1 = (30 - 0) + 0,7·(0 + 0).'
                B='höchster Beitrag: Berechnung des Beitrags von Spieler 1 = (100 % · 30) = 30 einsetzen in Vergütung Teil II für Spieler 2  = (30 - 30) + 0,7·(30 + 30) und addiert mit Vergütung Teil II Spieler 1 = (30 - 0) + 0,7·(30 + 30).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]

        if self.player.treatment != 'base':
            if not (value==20):
                A='niedrigster Beitrag: Berechnung des Beitrags von Spieler 1 = (100 % · 0) = 0 einsetzen in Vergütung Teil II für Spieler 2  = (20 - 0) + 0,7·(0 + 0) und addiert mit Vergütung Teil II Spieler 1 = (40 - 0) + 0,7·(0 + 0).'
                B='höchster Beitrag: Berechnung des Beitrags von Spieler 1 = (100 % · 20) = 20 einsetzen in Vergütung Teil II für Spieler 2  = (20 - 20) + 0,7·(20 + 20) und addiert mit Vergütung Teil II Spieler 1 = (40 - 20) + 0,7·(20 + 20).'
                C='Vergleichen Sie die beiden Ergebnisse und entscheiden Sie mit welchem Beitrag in LD Sie die höchste Vergütung für die Gruppe erzielen.'
                return [A,B,C]

    def Q6_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==24):
                A= 'Berechnung des Beitrags von Spieler 1 = (300% · 30) = 90.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (30 - 90) + 0,7·(90 + 30).'                
                return [A,B]
        if self.player.treatment == 'baseline':
            if not (value==36):                
                A= 'Berechnung des Beitrags von Spieler 1 = (300% · 20) = 60.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 60) + 0,7·(60 + 20).'                
                return [A,B]
        if self.player.treatment == 'lowthres':
            if not (value==36):
                A= 'Berechnung des Beitrags von Spieler 1 = (300% · 20) = 60.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 60) + 0,7·(60 + 20).'                
                return [A,B]
        if self.player.treatment == 'highthres':
            if not (value==36):            
                A= 'Berechnung des Beitrags von Spieler 1 = (300% · 20) = 60.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 60) + 0,7·(60 + 20).'                
                return [A,B]
    
    def Q7_1_error_message(self,value):
        if self.player.treatment == 'base':
            if not (value==31):
                A= 'Berechnung des Beitrags von Spieler 1 = (50% · 2) = 1.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (30 - 1) + 0,7·(1 + 2).'
                return [A,B]
        if self.player.treatment == 'baseline':
            if not (value==41):
                A= 'Berechnung des Beitrags von Spieler 1 = (50% · 2) = 1.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 1) + 0,7·(1 + 2).'
                return [A,B]
        if self.player.treatment == 'lowthres':
            if not (value==41):
                A= 'Berechnung des Beitrags von Spieler 1 = (50% · 2) = 0, da weniger als 4 LD von Spieler 2 beigetragen wurde.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 0) + 0,7·(0 + 2).'
                return [A,B]
        if self.player.treatment == 'highthres':
            if not (value==41):
                A= 'Berechnung des Beitrags von Spieler 1 = (50% · 2) = 0, da weniger als 12 LD von Spieler 2 beigetragen wurde.'
                B= 'Berechnung der Vergütung Teil II für Spieler 1  = (40 - 0) + 0,7·(0 + 2).'
                return [A,B]
     

    def before_next_page(self):
        self.player.define_end()

class O_MatchUncondiRich(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['type'] == 'subsidizer' 


    form_model=models.Player
    form_fields=["t"]

    def t_max(self):
        return 300

    def t_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'


    def before_next_page(self):
        pass

class O_MatchUncondiPoor(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['type'] == 'subsidized' 


    form_model=models.Player
    form_fields=["contri"]
    def contri_max(self):
        return self.player.endowment

    def before_next_page(self):
        pass


class TWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 2
    def after_all_players_arrive(self):
        self.group.rand_dec()

class P_MatchCondiRichNoTable(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['type'] == 'subsidizer' and self.player.treatment=='baseline'


    form_model=models.Player
    form_fields=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen", "sixteen", "seventeen","eighteen","nineteen","twenty"]

    def zero_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def one_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def two_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def three_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def four_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def five_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def six_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def seven_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eight_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def nine_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def ten_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eleven_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twelve_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def thirteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def fourteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def fifteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def sixteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def seventeen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eighteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def nineteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twenty_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'


    def zero_max(self):
        return 300
    def one_max(self):
        return 300
    def two_max(self):
        return 300
    def three_max(self):
        return 300
    def four_max(self):
        return 300
    def five_max(self):
        return 300
    def six_max(self):
        return 300
    def seven_max(self):
        return 300
    def eight_max(self):
        return 300
    def nine_max(self):
        return 300
    def ten_max(self):
        return 300
    def eleven_max(self):
        return 300
    def twelve_max(self):
        return 300
    def thirteen_max(self):
        return 300
    def fourteen_max(self):
        return 300
    def fifteen_max(self):
        return 300
    def sixteen_max(self):
        return 300
    def seventeen_max(self):
        return 300
    def eighteen_max(self):
        return 300
    def nineteen_max(self):
        return 300
    def twenty_max(self):
        return 300


    def vars_for_template(self):
        return self.player.vars_for_template1()

    def before_next_page(self):
        if self.timeout_happened:
            self.player.zero=10#random.randrange(0,self.player.endowment,1)
            self.player.one=10#random.randrange(0,self.player.endowment,1)
            self.player.two=10#random.randrange(0,self.player.endowment,1)
            self.player.three=10#random.randrange(0,self.player.endowment,1)
            self.player.four=10#random.randrange(0,self.player.endowment,1)
            self.player.five=10#random.randrange(0,self.player.endowment,1)
        self.player.calc_cond2()
        self.player.condi()

class P_MatchCondiRichLowTable(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['type'] == 'subsidizer' and self.player.treatment=='lowthres'


    form_model=models.Player
    form_fields=["four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen", "seventeen","eighteen","nineteen","twenty"]

    def zero_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def one_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def two_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def three_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def four_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def five_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def six_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def seven_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eight_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def nine_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def ten_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eleven_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twelve_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def thirteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def fourteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def fifteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def sixteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def seventeen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eighteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def nineteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twenty_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
   
    
    def four_max(self):
        return 300
    def five_max(self):
        return 300
    def six_max(self):
        return 300
    def seven_max(self):
        return 300
    def eight_max(self):
        return 300
    def nine_max(self):
        return 300
    def ten_max(self):
        return 300
    def eleven_max(self):
        return 300
    def twelve_max(self):
        return 300
    def thirteen_max(self):
        return 300
    def fourteen_max(self):
        return 300
    def fifteen_max(self):
        return 300
    def sixteen_max(self):
        return 300
    def seventeen_max(self):
        return 300
    def eighteen_max(self):
        return 300
    def nineteen_max(self):
        return 300
    def twenty_max(self):
        return 300


    def vars_for_template(self):
        return self.player.vars_for_template1()

    def before_next_page(self):
        if self.timeout_happened:
            self.player.three=10#random.randrange(0,self.player.endowment,1)
            self.player.four=10#random.randrange(0,self.player.endowment,1)
            self.player.five=10#random.randrange(0,self.player.endowment,1)
        self.player.calc_cond2()
        self.player.condi()

class P_MatchCondiRichHighTable(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['type'] == 'subsidizer' and self.player.treatment=='highthres'


    form_model=models.Player
    form_fields=["twelve","thirteen","fourteen","fifteen", "sixteen","seventeen","eighteen","nineteen","twenty"]

    def twelve_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def thirteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def fourteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def fifteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def sixteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def seventeen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eighteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def nineteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twenty_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'

    
  
    def twelve_max(self):
        return 300
    def thirteen_max(self):
        return 300
    def fourteen_max(self):
        return 300
    def fifteen_max(self):
        return 300
    def sixteen_max(self):
        return 300
    def seventeen_max(self):
        return 300
    def eighteen_max(self):
        return 300
    def nineteen_max(self):
        return 300
    def twenty_max(self):
        return 300


    def vars_for_template(self):
        return self.player.vars_for_template1()

    def before_next_page(self):
        if self.timeout_happened:
            self.player.four=10#random.randrange(0,self.player.endowment,1)
            self.player.five=10#random.randrange(0,self.player.endowment,1)
        self.player.calc_cond2()
        self.player.condi()

class P_MatchCondiRichBaseTable(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['type'] == 'subsidizer' and self.player.treatment=='base'


    form_model=models.Player
    form_fields=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen", "sixteen", "seventeen","eighteen","nineteen","twenty","twentyone","twentytwo","twentythree","twentyfour","twentyfive","twentysix","twentyseven","twentyeight","twentynine","thirty"]

#    def error_message(self, values):
 #       if  str(values["zero"])[-1]!="0": 
  #          return 'Please choose one of these numbers: 0,10,20,30,40,50,60,70,80,90,100,110,120'
   # def error_message1(self, values):
    #    if  str(values["one"])[-1]!="0": 
     #       return 'Please choose one of these numbers: 0,10,20,30,40,50,60,70,80,90,100,110,120'
    def zero_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def one_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def two_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def three_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def four_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def five_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def six_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def seven_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eight_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def nine_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def ten_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eleven_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twelve_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def thirteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def fourteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def fifteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def sixteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def seventeen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def eighteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def nineteen_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twenty_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentyone_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentytwo_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentythree_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentyfour_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentyfive_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentysix_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentyseven_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentyeight_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def twentynine_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'
    def thirty_error_message(self,value):
        if not str(value)[-1]=="0":
            return 'Der Prozentsatz muss zwischen 0 und 300 liegen in Werten von [0%, 10%, 20%,&hellip;, 300%]'


    
    def zero_max(self):
        return 300
    def one_max(self):
        return 300
    def two_max(self):
        return 300
    def three_max(self):
        return 300
    def four_max(self):
        return 300
    def five_max(self):
        return 300
    def six_max(self):
        return 300
    def seven_max(self):
        return 300
    def eight_max(self):
        return 300
    def nine_max(self):
        return 300
    def ten_max(self):
        return 300
    def eleven_max(self):
        return 300
    def twelve_max(self):
        return 300
    def thirteen_max(self):
        return 300
    def fourteen_max(self):
        return 300
    def fifteen_max(self):
        return 300
    def sixteen_max(self):
        return 300
    def seventeen_max(self):
        return 300
    def eighteen_max(self):
        return 300
    def nineteen_max(self):
        return 300
    def twenty_max(self):
        return 300
    def twentyone_max(self):
        return 300
    def twentytwo_max(self):
        return 300
    def twentythree_max(self):
        return 300
    def twentyfour_max(self):
        return 300
    def twentyfive_max(self):
        return 300
    def twentysix_max(self):
        return 300
    def twentyseven_max(self):
        return 300
    def twentyeight_max(self):
        return 300
    def twentynine_max(self):
        return 300
    def thirty_max(self):
        return 300


    def vars_for_template(self):
        return self.player.vars_for_template1()

    def before_next_page(self):
        if self.timeout_happened:
            self.player.zero=10#random.randrange(0,self.player.endowment,1)
            self.player.one=10#random.randrange(0,self.player.endowment,1)
            self.player.two=10#random.randrange(0,self.player.endowment,1)
            self.player.three=10#random.randrange(0,self.player.endowment,1)
            self.player.four=10#random.randrange(0,self.player.endowment,1)
            self.player.five=10#random.randrange(0,self.player.endowment,1)
            self.player.six=10#random.randrange(0,self.player.endowment,1)
            self.player.seven=10#random.randrange(0,self.player.endowment,1)
            self.player.eight=10#random.randrange(0,self.player.endowment,1)
        self.player.calc_cond2()
        self.player.condi()




class P_MatchCondiPoorTable(Page):
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['type'] == 'subsidized' 


    form_model=models.Player
    form_fields=["t0","t10","t20","t30","t40","t50","t60","t70","t80","t90","t100","t110","t120","t130","t140","t150","t160","t170","t180","t190","t200","t210","t220","t230","t240","t250","t260","t270","t280","t290","t300"]

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
    def t130_max(self):
        return self.player.endowment
    def t140_max(self):
        return self.player.endowment
    def t150_max(self):
        return self.player.endowment
    def t160_max(self):
        return self.player.endowment
    def t170_max(self):
        return self.player.endowment
    def t180_max(self):
        return self.player.endowment
    def t190_max(self):
        return self.player.endowment
    def t200_max(self):
        return self.player.endowment
    def t210_max(self):
        return self.player.endowment
    def t220_max(self):
        return self.player.endowment
    def t230_max(self):
        return self.player.endowment
    def t240_max(self):
        return self.player.endowment
    def t250_max(self):
        return self.player.endowment
    def t260_max(self):
        return self.player.endowment
    def t270_max(self):
        return self.player.endowment
    def t280_max(self):
        return self.player.endowment
    def t290_max(self):
        return self.player.endowment
    def t300_max(self):
        return self.player.endowment





    def vars_for_template(self):
        return self.player.vars_for_template1()

    def before_next_page(self):
        self.player.calc_cond1()
        self.player.condi()

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
            self.player.t130=1#random.randrange(0,self.player.endowment,1)
            self.player.t140=1#random.randrange(0,self.player.endowment,1)
            self.player.t150=1#random.randrange(0,self.player.endowment,1)
            self.player.t160=1#random.randrange(0,self.player.endowment,1)
            self.player.t170=1#random.randrange(0,self.player.endowment,1)
            self.player.t180=1#random.randrange(0,self.player.endowment,1)
            self.player.t190=1#random.randrange(0,self.player.endowment,1)
            self.player.t200=1#random.randrange(0,self.player.endowment,1)
            self.player.t210=1#random.randrange(0,self.player.endowment,1)
            self.player.t220=1#random.randrange(0,self.player.endowment,1)
            self.player.t230=1#random.randrange(0,self.player.endowment,1)
            self.player.t240=1#random.randrange(0,self.player.endowment,1)
            self.player.t250=1#random.randrange(0,self.player.endowment,1)
            self.player.t260=1#random.randrange(0,self.player.endowment,1)
            self.player.t270=1#random.randrange(0,self.player.endowment,1)
            self.player.t280=1#random.randrange(0,self.player.endowment,1)
            self.player.t290=1#random.randrange(0,self.player.endowment,1)
            self.player.t300=1#random.randrange(0,self.player.endowment,1)




class Result3WaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 2 and self.player.treatment=='baseline' or self.round_number == 2 and self.player.treatment=='base'
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


class X_guesstimate(Page):
    def is_displayed(self):
        return self.round_number == 3

    form_model=models.Player
    form_fields=["guess"]

    def guess_max(self):
        if self.participant.vars['type'] == 'subsidized':
            return 300
        if self.participant.vars['type'] == 'subsidizer' and self.player.treatment=="base":
            return 30
        if self.participant.vars['type'] == 'subsidizer' and self.player.treatment!="base":
            return 20

    def guess_error_message(self, value):
        if self.participant.vars['type'] == 'subsidized':
            if not str(value)[-1]=="0":
                return 'Bitte beschränken Sie sich in ihren Angaben auf Zehnerwerte'


    def before_next_page(self):
        self.player.fun_guess()
        self.group.out()
        self.player.total_payoff()


class Result2(Page):
    def is_displayed(self):
        return self.round_number == 3

    timeout_seconds=Constants.read_timeout

 
        

class QuesWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == 3

    wait_for_all_groups=True

class Questionnaire(Page):
    def is_displayed(self):
        return self.round_number == 3

    form_model = 'player'
    form_fields = ['equity1','equity1_A','equity1_B','equity1_C','equity2','equity2_A','equity2_B','equity2_C','equity3','equity3_A','equity3_B','equity3_C','risk', 'trust1', 'trust2', 'trust3', 'graphs', 'percent', 'tipp', 'supermarket',  'gender','age', 'religion', 'nationality', 'language', 'party']

#    timeout_seconds = Constants.read_timeout

    def age_error_message(self, value):
        if (value<=14):
            return 'Hier scheint ein Fehler aufgetreten zu sein.'
        if (value>=100):
            return 'Hier scheint ein Fehler aufgetreten zu sein.'

class QZ_Name(Page):
    def is_displayed(self):
        return self.round_number == 3

    form_model = 'player'
    form_fields = ['seat']

class Thanks(Page):
    def is_displayed(self):
        return self.round_number == 3



page_sequence = [
    Arrival,
    A_Welcome,
    B_Procedure,
    C_Rules,
    D_DescDecisionI,
    E_DescPaymentI, 
    EG_Control,
    G_Player,
    WaitToGroup,
    H_FischUncondi,
    WaitPlayer,
    I_FischCondiBaselineTable,
    I_FischCondiPoorTable,
    I_FischCondiRichTable,
    Result2WaitPage,
    WaitToGroup,
    J_Result1,
    WaitToGroup,
    K_WelcomeII,
    L_RulesII,
    M_DescDecisionIIPlayer1,
    M_DescDecisionIIPlayer2,
    M_DescPaymentII,
    N_Control,
    O_MatchPlayer,
    WaitToGroup,
    O_MatchUncondiPoor,
    O_MatchUncondiRich,
    TWaitPage,
    P_MatchCondiPoorTable,
    P_MatchCondiRichBaseTable,
    P_MatchCondiRichHighTable,
    P_MatchCondiRichLowTable,
    P_MatchCondiRichNoTable,
    Result3WaitPage,
    Result4WaitPage,
    Result5WaitPage,
    WaitToGroup, 
    X_guesstimate,
    WaitToGroup,    
    Result2,
    QuesWaitPage,
    Questionnaire,
    QZ_Name,
    Thanks
]