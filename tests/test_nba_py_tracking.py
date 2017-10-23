from nba_py import league
from nba_py import constants
try:
    # python 2 compatability
    from future_builtins import filter
except ImportError:
    pass

class TestPlayerTrackingStats:

    def __init__(self):
        self.season = "2016-17"
        self.target_player = "Aaron Gordon"

    def testPassing(self):
        passing = league.PlayerTrackingStats(season=self.season, pt_measure_type=constants.PtMeasureType.Passing)
        assert passing
        overall = passing.overall()
        stats = overall.iloc[2]
        assert stats['PLAYER_NAME'] == self.target_player
        assert stats['GP'] == 80
        assert stats['AST_TO_PASS_PCT_ADJ'] == 0.102
        assert stats['AST_ADJ'] == 2.6

    def testDefense(self):
        defense = league.PlayerTrackingStats(season=self.season, pt_measure_type=constants.PtMeasureType.Defense)
        assert defense
        overall = defense.overall()
        stats = overall.iloc[2]
        assert stats['PLAYER_NAME'] == self.target_player
        assert stats['GP'] == 80
        assert stats['DREB'] == 3.6