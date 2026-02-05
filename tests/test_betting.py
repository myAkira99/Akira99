"""Tests for betting engine."""
import pytest
from akira99.betting_engine import BettingEngine
from akira99.models import Scenario, Bet


@pytest.fixture
def engine():
    return BettingEngine()


@pytest.fixture
def scenario():
    return Scenario(
        id="s1",
        narrative="A figure enters the tavern",
        options=["Noble", "Thief", "Ghost"],
        narrative_odds={0: 3.2, 1: 4.8, 2: 12.1}
    )


def test_place_bet(engine, scenario):
    """Test placing a bet."""
    bet = engine.place_bet("player1", scenario, 1, 5.0)
    assert bet.player_id == "player1"
    assert bet.amount_sol == 5.0
    assert bet.option_index == 1


def test_calculate_payout(engine, scenario):
    """Test payout calculation."""
    bet = Bet("p1", "s1", 1, 5.0)
    payout = engine.calculate_payout(bet, scenario)
    assert payout == 5.0 * 4.8


def test_multiple_bets(engine, scenario):
    """Test multiple bets on same scenario."""
    engine.place_bet("p1", scenario, 0, 2.0)
    engine.place_bet("p2", scenario, 1, 3.0)
    engine.place_bet("p3", scenario, 2, 1.0)
    assert len(engine.pools[scenario.id]) == 3


def test_odds_adjustment(engine, scenario):
    """Test odds adjustment based on pool."""
    engine.place_bet("p1", scenario, 0, 10.0)
    adjusted = engine.get_current_odds(scenario)
    assert adjusted[0] < scenario.narrative_odds[0]
