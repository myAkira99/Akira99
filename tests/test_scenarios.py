"""Tests for scenario generation."""
import pytest
from akira99.scenario_generator import ScenarioGenerator


@pytest.fixture
def generator():
    return ScenarioGenerator()


def test_scenario_generation(generator):
    """Test scenario generation."""
    scenario = generator.generate("fantasy")
    assert scenario.id is not None
    assert scenario.narrative is not None
    assert len(scenario.options) == 3


def test_scenario_has_odds(generator):
    """Test scenario has odds."""
    scenario = generator.generate()
    assert len(scenario.narrative_odds) == 3
    for odd in scenario.narrative_odds.values():
        assert odd > 1.0


def test_different_themes(generator):
    """Test different themes."""
    for theme in ["fantasy", "scifi", "horror"]:
        scenario = generator.generate(theme)
        assert scenario is not None
