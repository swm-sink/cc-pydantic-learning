"""
Error Handling and Validation

Learning objectives:
- Understand common error types
- Learn proper exception handling
- Use validation with Pydantic
- Implement retry logic
- Handle API failures gracefully

Robust error handling is essential for production applications.
"""

from pydantic import BaseModel, Field, ValidationError
from pydantic_ai import Agent
from pydantic_ai.exceptions import UserError


class PersonInfo(BaseModel):
    """Person information with validation."""

    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=0, le=150)  # Greater than or equal to 0, less than or equal to 150
    email: str


def validation_example():
    """Demonstrate Pydantic validation."""
    print("=== Validation Example ===")

    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        output_type=PersonInfo,
        system_prompt='Extract person information.',
    )

    # Valid input
    try:
        result = agent.run_sync('John Doe, 30 years old, john@example.com')
        print(f"✅ Valid: {result.output}")
    except ValidationError as e:
        print(f"❌ Validation error: {e}")

    # The model will try to extract this, but if it fails validation,
    # Pydantic AI will retry automatically
    print("\nNote: Pydantic AI automatically retries on validation errors")


def basic_error_handling():
    """Basic try/except pattern."""
    print("\n=== Basic Error Handling ===")

    agent = Agent('anthropic:claude-sonnet-4-0')

    try:
        result = agent.run_sync('Hello!')
        print(f"Success: {result.data}")

    except UserError as e:
        # User-related errors (bad input, etc.)
        print(f"User error: {e}")

    except Exception as e:
        # Catch-all for other errors
        print(f"Unexpected error: {type(e).__name__}: {e}")


def retry_example():
    """Demonstrate retry logic."""
    print("\n=== Retry Logic ===")

    # Agent with custom retry settings
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        retries=3,  # Retry up to 3 times on failure
        system_prompt='Be helpful and concise.',
    )

    try:
        result = agent.run_sync('Hello!')
        print(f"✅ Success: {result.data}")
        print(f"Retries used: {result.usage().requests - 1}")

    except Exception as e:
        print(f"❌ Failed after retries: {e}")


def handling_tool_errors():
    """Handle errors in tools."""
    print("\n=== Tool Error Handling ===")

    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        system_prompt='You can divide numbers. Handle errors gracefully.',
    )

    @agent.tool_plain
    def divide(a: float, b: float) -> float:
        """Divide two numbers.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Result of a / b
        """
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    # Normal division
    result = agent.run_sync('What is 10 divided by 2?')
    print(f"10 / 2 = {result.data}")

    # Division by zero - the agent will handle the error
    result = agent.run_sync('What is 10 divided by 0?')
    print(f"10 / 0: {result.data}")


def api_key_handling():
    """Handle missing API keys gracefully."""
    print("\n=== API Key Handling ===")

    import os

    # Check if API key is set
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("❌ Error: ANTHROPIC_API_KEY not set!")
        print("Please set it with: export ANTHROPIC_API_KEY='your-key'")
        return

    # If we get here, key is set
    print("✅ API key is configured")


def validation_with_retries():
    """Show automatic validation retries."""
    print("\n=== Validation with Auto-Retry ===")

    class StrictData(BaseModel):
        """Strictly validated data."""

        number: int = Field(ge=1, le=100)
        text: str = Field(min_length=5)

    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        output_type=StrictData,
        retries=2,  # Will retry if validation fails
        system_prompt='Extract the requested data.',
    )

    try:
        # This should work
        result = agent.run_sync('The number is 42 and the text is "Hello World"')
        print(f"✅ Extracted: {result.output}")

    except ValidationError as e:
        print(f"❌ Validation failed after retries: {e}")


if __name__ == '__main__':
    # Run all examples
    validation_example()
    basic_error_handling()
    retry_example()
    handling_tool_errors()
    api_key_handling()
    validation_with_retries()

    print("\n=== Best Practices ===")
    print("1. Always use try/except for agent calls")
    print("2. Use Pydantic validation for structured outputs")
    print("3. Set appropriate retry counts")
    print("4. Handle tool errors gracefully")
    print("5. Check environment variables early")
    print("6. Pydantic AI automatically retries on validation errors")
    print("7. Provide helpful error messages to users")
