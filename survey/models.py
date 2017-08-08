from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Marius'

doc = """
Our first aurvey
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
        max=120,
        verbose_name="How old are you?",
        doc="collect age data between 0 and 120"
    )

    gender = models.CharField(
    	choices=["female","male","other"],
    	widget=widgets.RadioSelect(),
    	verbose_name="Please choose your gender",
    	doc="gender selection"

    )

    field_of_studies = models.CharField(
    	blank=True,
    	verbose_name="What do you study if at all?",
    	doc="free text input of field of studies"
    )

    height = models.FloatField(
    	min=0,
    	verbose_name="Please insert your height (in meter)",
    	doc="insert height"
    )

    weight = models.FloatField(
    	min=0,
    	verbose_name="Please insert your weight (in kg)",
    	doc="height of participant"
    )

    bmi = models.FloatField()
    bmi_class = models.CharField()

    def calculate_bmi(self):
    	self.bmi=self.weight/(self.height**2)
    	self.bmi=round(self.bmi,2)

    def category(self):
    	if self.bmi<18.5:
    #		return 'underweight'
    		self.bmi_class="underweight"
    	elif self.bmi>=18.5 and self.bmi<=25:
    #		return 'normal'
    		self.bmi_class="normal"
    	else:
    #		return 'overweight'
    		self.bmi_class="overweight"
   