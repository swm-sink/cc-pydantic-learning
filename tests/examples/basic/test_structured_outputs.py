"""
Tests for structured_outputs.py example.

Verify structured outputs work correctly with Pydantic models.
"""

import pytest
from pydantic import BaseModel, Field
from pydantic_ai import Agent


class CityInfo(BaseModel):
    """Test model for city information."""

    city: str
    country: str


class TestStructuredOutputs:
    """Test structured output functionality."""

    def test_model_definition(self):
        """Test that we can define a Pydantic model."""
        model = CityInfo(city="Paris", country="France")
        assert model.city == "Paris"
        assert model.country == "France"

    def test_agent_with_output_type(self):
        """Test creating an agent with output_type."""
        agent = Agent(
            'anthropic:claude-sonnet-4-0',
            output_type=CityInfo,
        )
        assert agent is not None

    @pytest.mark.requires_api_key
    def test_extract_city_info(self):
        """Test extracting structured city information."""
        agent = Agent(
            'anthropic:claude-sonnet-4-0',
            output_type=CityInfo,
            system_prompt='Extract city and country from text.',
        )

        result = agent.run_sync('The city is Tokyo in Japan.')

        assert isinstance(result.output, CityInfo)
        assert result.output.city.lower() == 'tokyo'
        assert result.output.country.lower() == 'japan'

    @pytest.mark.requires_api_key
    def test_validation(self):
        """Test that Pydantic validation works."""
        class StrictModel(BaseModel):
            number: int = Field(ge=1, le=10)

        agent = Agent(
            'anthropic:claude-sonnet-4-0',
            output_type=StrictModel,
            system_prompt='Extract a number between 1 and 10.',
        )

        result = agent.run_sync('The number is 5')

        assert isinstance(result.output, StrictModel)
        assert 1 <= result.output.number <= 10
