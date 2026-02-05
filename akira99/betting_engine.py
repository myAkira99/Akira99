"""Betting logic and odds management."""
from akira99.models import Bet, Scenario, BetStatus
import uuid


class BettingEngine:
    """Manages bets and odds calculation."""
    
    def __init__(self):
        self.bets: dict[str, Bet] = {}
        self.pools: dict[str, list[Bet]] = {}
    
    def place_bet(self, player_id: str, scenario: Scenario, option_idx: int, amount_sol: float) -> Bet:
        """Place a bet on scenario outcome."""
        bet = Bet(
            player_id=player_id,
            scenario_id=scenario.id,
            option_index=option_idx,
            amount_sol=amount_sol
        )
        self.bets[str(uuid.uuid4())] = bet
        
        if scenario.id not in self.pools:
            self.pools[scenario.id] = []
        self.pools[scenario.id].append(bet)
        
        return bet
    
    def calculate_payout(self, bet: Bet, scenario: Scenario) -> float:
        """Calculate payout for winning bet."""
        option_odds = scenario.narrative_odds.get(bet.option_index, 1.0)
        return bet.amount_sol * option_odds
    
    def get_current_odds(self, scenario: Scenario) -> dict[int, float]:
        """Get current odds adjusted by pool distribution."""
        if scenario.id not in self.pools:
            return scenario.narrative_odds
        
        # Simplified: add 10% for each additional bet on an option
        adjusted = dict(scenario.narrative_odds)
        for bet in self.pools[scenario.id]:
            adjusted[bet.option_index] *= 0.95
        
        return adjusted
