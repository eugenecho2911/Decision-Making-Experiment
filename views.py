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
    form_fields = ['eval_p1', 'eval_p2', 'eval_p3']

    def vars_for_template(self):
        return {
            'p1_contrib':self.group.get_player_by_id(1).contribution,
            'p2_contrib':self.group.get_player_by_id(2).contribution,
            'p3_contrib':self.group.get_player_by_id(3).contribution,
        }

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
    body_text = "Waiting for other participants to evaluate."


class Results(Page):
    """Players payoff: How much each has earned"""
    def vars_for_template(self):
        return {
            'Your Contribution': p1_contrib,
            'Other Player 1 Contribution':None,
            'Other Player 2 Contribution':None,
            'Total Contribution':None,
            'Your Score':None,
            'Other Player 1 Score':None,
            'Other Player 2 Score':None,
            'Median Score':None,
            'Your Remaining Tokens':None,
            'Group Grade':None,
            'Your Individual Grade':None,
            'Your Final Grade':None,
            'diff_endow_contrib':Constants.endowment - self.player.units
        }

page_sequence = [
    Introduction,
    Contribute,
    ObserveWaitPage,
    Observe,
    ResultsWaitPage,
    Results
]

