"""Data models for Akira99 Fate Casino."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class BetStatus(str, Enum):
    """Bet status."""
    PENDING = "pending"
    SETTLED = "settled"
    LOST = "lost"


@dataclass
class Scenario:
    """Story scenario for betting."""
    id: str
    narrative: str
    options: list[str]
    narrative_odds: dict[int, float]
    total_pool: float = 0.0
    bets: list = field(default_factory=list)


@dataclass
class Bet:
    """Placed bet on scenario outcome."""
    player_id: str
    scenario_id: str
    option_index: int
    amount_sol: float
    status: BetStatus = BetStatus.PENDING
    payout: Optional[float] = None


@dataclass
class Outcome:
    """Resolved scenario outcome."""
    scenario_id: str
    winning_option: int
    reasoning: str
    winners: list[str] = field(default_factory=list)
    payouts: dict[str, float] = field(default_factory=dict)


class ScenarioRequest(BaseModel):
    """Request for scenario generation."""
    difficulty: str = "medium"
    theme: Optional[str] = None


class BetRequest(BaseModel):
    """Request to place bet."""
    player_id: str
    scenario_id: str
    option_index: int
    amount_sol: float
