"""Tests for outcome resolution."""
import pytest
from akira99.outcome_resolver import OutcomeResolver
from akira99.models import Scenario, Bet


@pytest.fixture
def resolver():
    return OutcomeResolver()


@pytest.fixture
def scenario():
    return Scenario(
        id="s1",
        narrative="A thief enters the tavern",
        options=["Noble", "Thief", "Ghost"],
        narrative_odds={0: 3.2, 1: 4.8, 2: 12.1}
    )


def test_resolve_outcome(resolver, scenario):
    """Test outcome resolution."""
    bets = [
        Bet("p1", "s1", 0, 5.0),
        Bet("p2", "s1", 1, 10.0),
        Bet("p3", "s1", 2, 2.0),
    ]
    outcome = resolver.resolve(scenario, bets)
    assert outcome.scenario_id == "s1"
    assert 0 <= outcome.winning_option <= 2


def test_winners_identified(resolver, scenario):
    """Test winners are correctly identified."""
    bets = [Bet("p1", "s1", 1, 5.0), Bet("p2", "s1", 1, 3.0)]
    outcome = resolver.resolve(scenario, bets)
    if outcome.winning_option == 1:
        assert "p1" in outcome.winners or "p2" in outcome.winners
