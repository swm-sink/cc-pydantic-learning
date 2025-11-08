"""
Common Agent Patterns - Reusable snippets for Pydantic AI

Copy these patterns and adapt them to your needs.
"""

from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext


# Pattern 1: Basic Agent
def create_basic_agent():
    """Create a simple agent with instructions."""
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        system_prompt='You are a helpful assistant. Be concise and accurate.',
    )
    return agent


# Pattern 2: Agent with Structured Output
class ResponseModel(BaseModel):
    """Example response model."""

    answer: str
    confidence: float = Field(ge=0.0, le=1.0)


def create_structured_agent():
    """Agent that returns structured data."""
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        output_type=ResponseModel,
        system_prompt='Provide answers with confidence scores.',
    )
    return agent


# Pattern 3: Agent with Dependencies
@dataclass
class AgentDeps:
    """Dependencies for the agent."""

    api_key: str
    user_id: int


def create_agent_with_deps():
    """Agent using dependency injection."""
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        deps_type=AgentDeps,
        system_prompt='You are a personalized assistant.',
    )

    @agent.tool
    async def get_user_data(ctx: RunContext[AgentDeps]) -> dict:
        """Get user data using dependencies."""
        return {"user_id": ctx.deps.user_id}

    return agent


# Pattern 4: Agent with Multiple Tools
def create_multi_tool_agent():
    """Agent with several tools."""
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        system_prompt='You have various capabilities. Use tools when appropriate.',
    )

    @agent.tool_plain
    def calculate(expression: str) -> float:
        """Calculate a mathematical expression."""
        return eval(expression, {"__builtins__": {}}, {})

    @agent.tool_plain
    def format_currency(amount: float, currency: str = "USD") -> str:
        """Format amount as currency."""
        return f"{currency} {amount:.2f}"

    return agent


# Pattern 5: Agent with Dynamic System Prompt
@dataclass
class UserContext:
    """User context for personalization."""

    name: str
    language: str


def create_dynamic_prompt_agent():
    """Agent with dynamic system prompt."""
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        deps_type=UserContext,
    )

    @agent.system_prompt
    async def dynamic_prompt(ctx: RunContext[UserContext]) -> str:
        """Generate personalized prompt."""
        return f"""You are a helpful assistant for {ctx.deps.name}.
        Communicate in {ctx.deps.language}."""

    return agent


# Pattern 6: Agent with Retry Logic
def create_resilient_agent():
    """Agent with retry configuration."""
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        retries=3,
        system_prompt='Be helpful and accurate.',
    )
    return agent


# Pattern 7: Agent with Model Configuration
from pydantic_ai.settings import ModelSettings


def create_configured_agent():
    """Agent with specific model settings."""
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        model_settings=ModelSettings(
            temperature=0.7,
            max_tokens=500,
        ),
        system_prompt='Generate creative responses.',
    )
    return agent


# Pattern 8: Agent Factory
def create_agent_for_task(task_type: str):
    """Factory function to create agents based on task."""
    prompts = {
        "summarize": "Summarize text concisely and accurately.",
        "classify": "Classify the input into appropriate categories.",
        "extract": "Extract structured information from text.",
    }

    return Agent(
        'anthropic:claude-sonnet-4-0',
        system_prompt=prompts.get(task_type, "Be helpful."),
    )


# Pattern 9: Testing Pattern
def create_test_agent_with_mocks():
    """Agent configured for testing."""

    @dataclass
    class MockDeps:
        """Mock dependencies for testing."""

        def get_data(self) -> dict:
            return {"test": "data"}

    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        deps_type=MockDeps,
    )

    return agent, MockDeps()


# Usage Examples
if __name__ == '__main__':
    # Example 1: Basic usage
    basic = create_basic_agent()
    # result = basic.run_sync('Hello!')

    # Example 2: Structured output
    structured = create_structured_agent()
    # result = structured.run_sync('What is 2+2?')

    # Example 3: With dependencies
    agent_with_deps, deps = create_agent_with_deps()
    # result = agent_with_deps.run_sync('Help me', deps=deps)

    print("✅ All agent patterns loaded successfully!")
