"""
Tests for hello_world.py example.

These tests verify the basic example runs correctly.
"""

import pytest
from pydantic_ai import Agent


class TestHelloWorld:
    """Test the hello world example."""

    def test_agent_creation(self):
        """Test that we can create a basic agent."""
        agent = Agent(
            'anthropic:claude-sonnet-4-0',
            system_prompt='Be concise.',
        )
        assert agent is not None

    @pytest.mark.requires_api_key
    def test_simple_run(self):
        """Test a simple agent run."""
        agent = Agent(
            'anthropic:claude-sonnet-4-0',
            system_prompt='Reply with just "Hello"',
        )

        result = agent.run_sync('Say hello')

        assert result.output is not None
        assert len(result.output) > 0
        assert 'hello' in result.output.lower()

    @pytest.mark.requires_api_key
    def test_usage_tracking(self):
        """Test that usage information is available."""
        agent = Agent('anthropic:claude-sonnet-4-0')

        result = agent.run_sync('Hi!')

        usage = result.usage()
        assert usage.requests > 0
        assert usage.request_tokens > 0
        assert usage.response_tokens > 0
