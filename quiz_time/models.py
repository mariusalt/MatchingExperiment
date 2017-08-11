from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Marius'

doc = """
Play a loaded quiz
"""


class Constants(BaseConstants):
    name_in_url = 'quiz_time'
    players_per_group = None
    

    with open('quiz_time\quiz.csv') as f:
    	questions = list(csv.DictReader(f, delimiter=';'))

    num_rounds = len(questions)



class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions
            ## ALTERNATIVE DESIGN:
            ## to randomize the order of the questions, you could instead do:

            # import random
            # randomized_questions = random.sample(Constants.questions, len(Constants.questions))
            # self.session.vars['questions'] = randomized_questions

            ## and to randomize differently for each participant, you could use
            ## the random.sample technique, but assign into participant.vars
            ## instead of session.vars.

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']
            p.solution = question_data['solution']



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.PositiveIntegerField()
    question = models.CharField()
    solution = models.CharField()
    submitted_answer = models.CharField(widget=widgets.RadioSelect())
    is_correct = models.BooleanField()
 #   correct_answers=models.IntegerField(
  #  	default=0
   # 	)

    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]

    def check_correct(self):
    	self.is_correct = self.submitted_answer == self.solution

#    def count(self):
 #   	if self.submitted_answer == self.solution:
  #  		self.correct_answers=self.correct_answers.in_previous_rounds() + 1

