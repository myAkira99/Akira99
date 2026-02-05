"""Tests for Solana settlement."""
import pytest
from akira99.solana_settlement import SolanaSettler


@pytest.fixture
def settler():
    return SolanaSettler()


def test_settlement(settler):
    """Test settlement."""
    payout = {"p1": 25.0, "p2": 15.0}
    result = settler.settle(["p1", "p2"], payout)
    assert len(result.winners) == 2
    assert result.fee > 0


def test_settlement_fee_calculation(settler):
    """Test fee calculation."""
    payout = {"p1": 100.0}
    result = settler.settle(["p1"], payout)
    assert result.fee == 5.0  # 5% of 100
