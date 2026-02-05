"""Tests for data models."""
import pytest
from akira99.models import Scenario, Bet, Outcome, BetStatus


def test_scenario_creation():
    """Test creating scenario."""
    s = Scenario(
        id="s1",
        narrative="Test story",
        options=["A", "B", "C"],
        narrative_odds={0: 3.2, 1: 4.8, 2: 12.1}
    )
    assert s.id == "s1"
    assert len(s.options) == 3


def test_bet_creation():
    """Test creating bet."""
    b = Bet("p1", "s1", 0, 5.0)
    assert b.player_id == "p1"
    assert b.status == BetStatus.PENDING


def test_outcome_creation():
    """Test creating outcome."""
    o = Outcome(
        scenario_id="s1",
        winning_option=1,
        reasoning="Test",
        winners=["p1", "p2"]
    )
    assert o.winning_option == 1
    assert len(o.winners) == 2
