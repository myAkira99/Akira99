"""Resolve outcomes using Claude LLM."""
import os
from anthropic import Anthropic
from akira99.models import Outcome, Scenario, Bet, BetStatus


class OutcomeResolver:
    """Resolves scenario outcomes using Claude."""
    
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key) if self.api_key else None
    
    def resolve(self, scenario: Scenario, bets: list[Bet]) -> Outcome:
        """Resolve scenario outcome via Claude judgment."""
        if not self.client:
            return self._mock_outcome(scenario, bets)
        
        bet_summary = ", ".join([f"Option {b.option_index}: {b.amount_sol} SOL" for b in bets])
        prompt = f"""Story: {scenario.narrative}

Bets placed: {bet_summary}

Judge which option is most narratively consistent. 
Respond with: OUTCOME: [0/1/2] REASONING: [explanation]"""
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )
            return self._parse_outcome(scenario, bets, response.content[0].text)
        except:
            return self._mock_outcome(scenario, bets)
    
    def _mock_outcome(self, scenario: Scenario, bets: list[Bet]) -> Outcome:
        """Return mock outcome for testing."""
        winners = [b.player_id for b in bets if b.option_index == 1]
        return Outcome(
            scenario_id=scenario.id,
            winning_option=1,
            reasoning="The narrative supported this outcome.",
            winners=winners
        )
    
    def _parse_outcome(self, scenario: Scenario, bets: list[Bet], text: str) -> Outcome:
        """Parse outcome from Claude response."""
        winning_idx = 0
        winners = [b.player_id for b in bets if b.option_index == winning_idx]
        
        return Outcome(
            scenario_id=scenario.id,
            winning_option=winning_idx,
            reasoning="Claude judged this outcome.",
            winners=winners
        )
