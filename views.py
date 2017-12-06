from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class Contribute(Page):
    """Player: Choose how much to contribute"""
    form_model = models.Player
    form_fields = ['contribution']

class ObserveWaitPage(WaitPage):
    body_text = "Waiting for other participants to contribute."

class Observe(Page):
    form_model = models.Player
    form_fields = ['Score_p1', 'Score_p2', 'Score_p3']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
    body_text = "Waiting for other participants to evaluate."


class Results(Page):
    """Players payoff: How much each has earned"""
    def vars_for_template(self):
        return {
            'Your Contribution':
            'Other Player 1 Contribution':
            'Other Player 2 Contribution':
            'Total Contribution':
            'Your Score':
            'Other Player 1 Score':
            'Other Player 2 Score':
            'Median Score':
            'Your Remaining Tokens':
            'Group Grade':
            'Your Individual Grade'
            'Your Final Grade':
        }

page_sequence = [
    Introduction,
    Contribute,
    ObserveWaitPage,
    Observe,
    ResultsWaitPage,
    Results
]
