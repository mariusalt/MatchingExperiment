from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Marius'

doc = """
Game with possibility to chat
"""


class Constants(BaseConstants):
    name_in_url = 'chat'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'group1'
        else:
            return 'group2'

    def chat_nickname(self):
        return 'Group {} {}'.format(self.role())
