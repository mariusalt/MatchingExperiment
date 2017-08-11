from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otreechat.models import ChatMessage


class MyPage(Page):
    pass




page_sequence = [
    MyPage
]
