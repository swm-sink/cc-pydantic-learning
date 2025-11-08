"""
Dependency Injection with RunContext

Learning objectives:
- Understand what dependency injection is
- Learn how to use RunContext
- Pass dependencies to agents and tools
- Make testing easier with DI
- Use dataclasses for complex dependencies

Dependency injection allows you to pass external resources
(databases, APIs, config) to your agent and tools in a type-safe way.
"""

from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext


# Example 1: Simple Database Dependency
@dataclass
class DatabaseConnection:
    """Simulated database connection."""

    def get_user(self, user_id: int) -> dict:
        """Get user from database."""
        # In reality, this would query a real database
        return {
            "id": user_id,
            "name": "Alice Smith",
            "balance": 1234.56,
            "account_type": "premium"
        }


    def update_balance(self, user_id: int, new_balance: float) -> bool:
        """Update user balance."""
        print(f"  [DB] Updating balance for user {user_id} to ${new_balance:.2f}")
        return True


# Create agent that uses database
database_agent = Agent(
    'anthropic:claude-sonnet-4-0',
    deps_type=DatabaseConnection,  # Declare dependency type
    system_prompt='You are a helpful banking assistant.',
)


@database_agent.tool
async def get_balance(ctx: RunContext[DatabaseConnection]) -> str:
    """Get the user's current balance.

    Args:
        ctx: Context containing the database connection
    """
    # Access dependency through ctx.deps
    user_data = ctx.deps.get_user(user_id=123)
    return f"${user_data['balance']:.2f}"


def simple_dependency_example():
    """Basic dependency injection."""
    print("=== Simple Dependency Injection ===")

    # Create the dependency
    db = DatabaseConnection()

    # Pass it to the agent
    result = database_agent.run_sync(
        'What is my balance?',
        deps=db  # Inject the dependency
    )

    print(f"Agent: {result.data}\n")


# Example 2: Multiple Dependencies
@dataclass
class AppConfig:
    """Application configuration."""

    api_key: str
    max_retries: int = 3
    timeout: int = 30


@dataclass
class Dependencies:
    """All dependencies bundled together."""

    db: DatabaseConnection
    config: AppConfig
    current_user_id: int


support_agent = Agent(
    'anthropic:claude-sonnet-4-0',
    deps_type=Dependencies,
    system_prompt='You are a customer support agent.',
)


@support_agent.tool
async def check_account_status(ctx: RunContext[Dependencies]) -> dict:
    """Check account status for the current user.

    Args:
        ctx: Context with all dependencies
    """
    # Access multiple dependencies
    user_id = ctx.deps.current_user_id
    user_data = ctx.deps.db.get_user(user_id)

    print(f"  [Tool] Checking status for user {user_id}")

    return {
        "user": user_data['name'],
        "type": user_data['account_type'],
        "balance": user_data['balance'],
    }


def multiple_dependencies_example():
    """Using multiple dependencies."""
    print("=== Multiple Dependencies ===")

    # Set up all dependencies
    db = DatabaseConnection()
    config = AppConfig(api_key="test-key-123")
    deps = Dependencies(db=db, config=config, current_user_id=123)

    # Run agent with all dependencies
    result = support_agent.run_sync(
        'Can you check my account status?',
        deps=deps
    )

    print(f"Agent: {result.data}\n")


# Example 3: Dynamic System Prompts with Dependencies
@dataclass
class UserContext:
    """Context about the current user."""

    name: str
    language: str
    timezone: str


personalized_agent = Agent(
    'anthropic:claude-sonnet-4-0',
    deps_type=UserContext,
)


@personalized_agent.system_prompt
async def dynamic_prompt(ctx: RunContext[UserContext]) -> str:
    """Generate personalized system prompt based on user context.

    Args:
        ctx: Context with user information
    """
    return f"""You are a helpful assistant for {ctx.deps.name}.

    - Respond in {ctx.deps.language}
    - Consider their timezone: {ctx.deps.timezone}
    - Be friendly and personalized"""


def dynamic_prompt_example():
    """Dynamic system prompts with dependencies."""
    print("=== Dynamic System Prompts ===")

    # Different users get different experiences
    user1 = UserContext(name="Alice", language="English", timezone="PST")
    user2 = UserContext(name="Bob", language="Spanish", timezone="EST")

    result1 = personalized_agent.run_sync('What time is it?', deps=user1)
    print(f"Alice: {result1.data}")

    result2 = personalized_agent.run_sync('What time is it?', deps=user2)
    print(f"Bob: {result2.data}\n")


# Example 4: Testing with Mock Dependencies
@dataclass
class MockDatabase:
    """Mock database for testing."""

    def get_user(self, user_id: int) -> dict:
        """Return test data."""
        return {
            "id": user_id,
            "name": "Test User",
            "balance": 100.00,
            "account_type": "test"
        }


def testing_example():
    """Show how DI makes testing easier."""
    print("=== Testing with Mock Dependencies ===")

    # Use mock instead of real database
    mock_db = MockDatabase()

    result = database_agent.run_sync(
        'What is my balance?',
        deps=mock_db  # Easy to swap out!
    )

    print(f"Test result: {result.data}")
    print("✅ No real database needed for testing!\n")


# Example 5: API Client Dependency
@dataclass
class WeatherAPI:
    """Weather API client."""

    api_key: str

    def get_weather(self, city: str) -> dict:
        """Get weather for a city."""
        print(f"  [API] Fetching weather for {city}")
        # In reality, this would call a real API
        return {
            "city": city,
            "temperature": 72,
            "condition": "sunny"
        }


weather_agent = Agent(
    'anthropic:claude-sonnet-4-0',
    deps_type=WeatherAPI,
    system_prompt='You provide weather information.',
)


@weather_agent.tool
async def check_weather(ctx: RunContext[WeatherAPI], city: str) -> str:
    """Check weather for a city.

    Args:
        ctx: Context with API client
        city: City name
    """
    data = ctx.deps.get_weather(city)
    return f"{data['temperature']}°F and {data['condition']}"


def api_client_example():
    """Using API clients as dependencies."""
    print("=== API Client Dependency ===")

    api = WeatherAPI(api_key="your-api-key")

    result = weather_agent.run_sync(
        'What is the weather in San Francisco?',
        deps=api
    )

    print(f"Agent: {result.data}\n")


if __name__ == '__main__':
    # Run all examples
    simple_dependency_example()
    multiple_dependencies_example()
    dynamic_prompt_example()
    testing_example()
    api_client_example()

    print("=== Key Takeaways ===")
    print("1. Use deps_type to declare dependency type")
    print("2. Access dependencies through ctx.deps in tools")
    print("3. Pass dependencies with deps= parameter")
    print("4. Use dataclasses to bundle multiple dependencies")
    print("5. DI makes testing much easier")
    print("6. RunContext provides type-safe access")
    print("7. Dynamic system prompts can use dependencies")
