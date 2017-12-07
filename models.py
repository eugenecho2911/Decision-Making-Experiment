from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from statistics import median

author = 'Eugene Cho'

doc = """
This is an experiment in decision making.
"""


class Constants(BaseConstants):
    name_in_url = 'Decision_Making_Experiment'
    players_per_group = 3
    num_rounds = 30

    instructions_template ='Decision_Making_Experiment/Instructions.html'
    endowment = c(12)
    multiplier = 13


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    group_grade = models.FloatField()

    def set_preliminary_payoffs(self):
        self.contribution = [(p, p.contribution) for p in self.get_players()]
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        for p in self.get_players():
            p.individual_score = statistics.median(score_p1, score_p2, score_3)
            p.individual_grade = Constants.multiplier * (3 * individual_score) - 0.5 * (3 * individual_score)^2
            p.group_grade = Constants.multiplier * (self.total_contribution) - 0.5 * (self.total_contribution)^2

    def set_final_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        for p in self.get_players():
            p.final_grade =  0.25 * (p.group_grade) + 0.75 * (p.individual_grade)


class Player(BasePlayer):
    individual_grade = models.FloatField()
    final_grade = models.FloatField()
    score_median = models.FloatField()

    endowment = models.FloatField(
        min=0,
        max=Constants.endowment,
        doc="""player's tokens"""
    )

    contribution = models.FloatField(
        min=0, max=Constants.endowment,
        doc="""player's tokens""",
        widget=widgets.SliderInput(attrs={'step':'0.1'})
    )

    eval_p1 =  models.FloatField(
        min=0, max=Constants.endowment,
        doc="""This player's evaluation of player 1""",
        widget=widgets.SliderInput(attrs={'step':'0.1'})
    )
    eval_p2 =  models.FloatField(
        min=0, max=Constants.endowment,
        doc="""This player's evaluation of player 2""",
        widget=widgets.SliderInput(attrs={'step':'0.1'})
    )
    eval_p3 =  models.FloatField(
        min=0, max=Constants.endowment,
        doc="""This player's evaluation of player 3""",
        widget=widgets.SliderInput(attrs={'step':'0.1'})
    )


    contribution_p1 = models.FloatField(
        min=0, max=Constants.endowment,
        doc="""The amount of tokens contributed by Player 1.""",
    )

    contribution_p2 = models.FloatField(
        min=0, max=Constants.endowment,
        doc="""The amount of tokens contributed by Player 2.""",
    )

    contribution_p3 = models.FloatField(
        min=0, max=Constants.endowment,
        doc="""The amount of tokens contributed by Player 3.""",
    )

    score_p1 = models.FloatField(
        doc="""The median of all scores given to Player 1.""",
        min=0, max=Constants.endowment,
    )

    score_p2 = models.FloatField(
        doc="""The median of all scores given to Player 2.""",
        min=0, max=Constants.endowment,
    )

    score_p3 = models.FloatField(
        doc="""The median of all scores given to Player 3.""",
        min=0, max=Constants.endowment,
    )

    score_median = models.FloatField(
        doc="""The median of score_p1, score_p2, and score_p3""",
        min=0, max=Constants.endowment,
    )

    group_grade = models.FloatField(
        doc="""This is the group grade that contributes to all player's final grade.""",
    )

    individual_grade_p1 = models.FloatField(
        doc="""This is Player 1's individual grade.""",
    )

    individual_grade_p2 = models.FloatField(
        doc="""This is Player 2's individual grade.""",
    )

    individual_grade_p3 = models.FloatField(
        doc="""This is Player 3's individual grade.""",
    )

    final_grade_p1 = models.FloatField(
        doc="""This is Player 1's final grade.""",
    )

    final_grade_p2 = models.FloatField(
        doc="""This is Player 2's final grade.""",
    )

    final_grade_p3 = models.FloatField(
        doc="""This is Player 3's final grade.""",
    )

