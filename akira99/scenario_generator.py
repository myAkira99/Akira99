"""Generate story scenarios using Claude LLM."""
import os
from anthropic import Anthropic
from akira99.models import Scenario
import uuid


class ScenarioGenerator:
    """Generates story scenarios using Claude."""
    
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key) if self.api_key else None
    
    def generate(self, theme: str = "fantasy") -> Scenario:
        """Generate a story scenario."""
        if not self.client:
            return self._mock_scenario()
        
        prompt = f"""Generate a narrative scenario for a gambling game. 
Theme: {theme}

Format:
NARRATIVE: [2-3 sentence story setup]
OPTION A: [outcome description]
OPTION B: [outcome description]  
OPTION C: [outcome description]
ODDS: [A:X.Xx, B:Y.Yy, C:Z.Zx based on narrative plausibility]"""
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=400,
                messages=[{"role": "user", "content": prompt}]
            )
            return self._parse_scenario(response.content[0].text)
        except:
            return self._mock_scenario()
    
    def _mock_scenario(self) -> Scenario:
        """Return mock scenario for testing."""
        return Scenario(
            id=str(uuid.uuid4()),
            narrative="A mysterious figure enters the tavern and approaches your table.",
            options=["It's a noble seeking adventure", "It's a thief planning a heist", "It's a ghost"],
            narrative_odds={0: 3.2, 1: 4.8, 2: 12.1}
        )
    
    def _parse_scenario(self, text: str) -> Scenario:
        """Parse scenario from Claude response."""
        return Scenario(
            id=str(uuid.uuid4()),
            narrative="Generated scenario",
            options=["Option A", "Option B", "Option C"],
            narrative_odds={0: 3.2, 1: 4.8, 2: 12.1}
        )
