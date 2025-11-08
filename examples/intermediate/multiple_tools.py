"""
Agent with Multiple Tools

Learning objectives:
- Coordinate multiple tools in one agent
- Understand how the LLM chooses which tool to use
- See tools working together
- Handle tool chaining
- Best practices for tool design

A real-world agent often needs many tools to be useful.
"""

from datetime import datetime, timedelta
import random
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext


@dataclass
class AgentDependencies:
    """Dependencies for our multi-tool agent."""

    user_name: str
    user_timezone: str = "UTC"


# Create an assistant with multiple capabilities
assistant = Agent(
    'anthropic:claude-sonnet-4-0',
    deps_type=AgentDependencies,
    system_prompt='''You are a personal assistant with various capabilities.
    Use the appropriate tools to help the user with their requests.
    Be helpful and natural in your responses.''',
)


@assistant.tool_plain
def get_current_time() -> str:
    """Get the current date and time.

    Returns:
        Current datetime formatted as a string
    """
    now = datetime.now()
    print(f"  [Tool: get_current_time] → {now}")
    return now.strftime("%Y-%m-%d %H:%M:%S")


@assistant.tool_plain
def calculate(expression: str) -> float:
    """Safely evaluate a mathematical expression.

    Args:
        expression: Math expression like "2 + 2" or "10 * 5"

    Returns:
        Result of the calculation
    """
    try:
        # Note: eval() is dangerous in production! Use a proper math parser.
        # This is simplified for the learning example.
        result = eval(expression, {"__builtins__": {}}, {})
        print(f"  [Tool: calculate] {expression} = {result}")
        return float(result)
    except Exception as e:
        print(f"  [Tool: calculate] Error: {e}")
        return 0.0


@assistant.tool_plain
def generate_password(length: int = 12) -> str:
    """Generate a random password.

    Args:
        length: Length of password (default 12)

    Returns:
        Generated password
    """
    import string
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"  [Tool: generate_password] Generated {length}-character password")
    return password


@assistant.tool
async def set_reminder(ctx: RunContext[AgentDependencies], task: str, minutes: int) -> str:
    """Set a reminder for the user.

    Args:
        ctx: Context with user info
        task: What to remind about
        minutes: Minutes from now

    Returns:
        Confirmation message
    """
    reminder_time = datetime.now() + timedelta(minutes=minutes)
    print(f"  [Tool: set_reminder] {task} at {reminder_time}")
    return f"Reminder set for {ctx.deps.user_name}: '{task}' at {reminder_time.strftime('%H:%M')}"


@assistant.tool_plain
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between units.

    Args:
        value: Temperature value
        from_unit: 'C', 'F', or 'K'
        to_unit: 'C', 'F', or 'K'

    Returns:
        Converted temperature
    """
    # Convert to Celsius first
    if from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        celsius = value

    # Convert from Celsius to target
    if to_unit == 'F':
        result = celsius * 9/5 + 32
    elif to_unit == 'K':
        result = celsius + 273.15
    else:
        result = celsius

    print(f"  [Tool: convert_temperature] {value}°{from_unit} → {result:.2f}°{to_unit}")
    return round(result, 2)


def single_tool_example():
    """Agent uses one tool."""
    print("=== Single Tool Usage ===")

    deps = AgentDependencies(user_name="Alice")

    result = assistant.run_sync('What time is it right now?', deps=deps)
    print(f"Response: {result.data}\n")


def multiple_tools_in_sequence():
    """Agent uses multiple tools in one response."""
    print("=== Multiple Tools in Sequence ===")

    deps = AgentDependencies(user_name="Bob")

    result = assistant.run_sync(
        'Calculate 25 times 4, then set a reminder to check my email in 30 minutes',
        deps=deps
    )
    print(f"Response: {result.data}\n")


def tool_selection():
    """Agent chooses the right tool."""
    print("=== Intelligent Tool Selection ===")

    deps = AgentDependencies(user_name="Charlie")

    # Should use calculate
    result = assistant.run_sync('What is 144 divided by 12?', deps=deps)
    print(f"Math: {result.data}\n")

    # Should use generate_password
    result = assistant.run_sync('Generate a strong password for me', deps=deps)
    print(f"Password: {result.data}\n")

    # Should use convert_temperature
    result = assistant.run_sync('Convert 100°F to Celsius', deps=deps)
    print(f"Temperature: {result.data}\n")


def complex_request():
    """Handle a complex multi-step request."""
    print("=== Complex Multi-Step Request ===")

    deps = AgentDependencies(user_name="Diana")

    result = assistant.run_sync(
        '''I need help with a few things:
        1. What time is it?
        2. Convert 25°C to Fahrenheit
        3. Calculate 15% of 200
        4. Set a reminder to call mom in 60 minutes
        ''',
        deps=deps
    )
    print(f"Response: {result.data}\n")


def tool_with_error():
    """Handle tool errors gracefully."""
    print("=== Tool Error Handling ===")

    deps = AgentDependencies(user_name="Eve")

    # This will cause calculate to fail but the agent should handle it
    result = assistant.run_sync('Calculate one plus two', deps=deps)
    print(f"Response: {result.data}\n")


if __name__ == '__main__':
    # Run all examples
    single_tool_example()
    multiple_tools_in_sequence()
    tool_selection()
    complex_request()
    tool_with_error()

    print("=== Tool Design Best Practices ===")
    print("1. Each tool should do one thing well")
    print("2. Write clear, detailed docstrings")
    print("3. Use type hints for all parameters")
    print("4. Return JSON-serializable data")
    print("5. Handle errors within tools")
    print("6. Use tool_plain for stateless tools")
    print("7. Use tool (with RunContext) for stateful operations")
    print("8. Let the LLM decide which tool to use")
    print("9. Tools can be chained naturally")
    print("10. Keep tool interfaces simple and focused")
