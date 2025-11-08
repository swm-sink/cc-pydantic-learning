"""
Simple Tools and Function Calling

Learning objectives:
- Understand what tools are and why they're useful
- Learn to register tools with @agent.tool_plain
- See how the LLM decides when to call tools
- Handle tool responses

Tools give your agent capabilities beyond text generation,
like calculations, API calls, or database queries.
"""

import random
from datetime import datetime
from pydantic_ai import Agent


# Create agent that will use tools
calculator_agent = Agent(
    'anthropic:claude-sonnet-4-0',
    system_prompt='''You are a helpful assistant with calculation abilities.
    Use the tools available to you when appropriate.''',
)


@calculator_agent.tool_plain
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    print(f"  [Tool called: add_numbers({a}, {b})]")
    return a + b


@calculator_agent.tool_plain
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    print(f"  [Tool called: multiply_numbers({a}, {b})]")
    return a * b


@calculator_agent.tool_plain
def get_current_time() -> str:
    """Get the current date and time.

    Returns:
        Current datetime as a string
    """
    print("  [Tool called: get_current_time()]")
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculator_example():
    """Agent with calculator tools."""
    print("=== Calculator Agent ===")

    # The agent will call the add_numbers tool
    result = calculator_agent.run_sync('What is 15 + 27?')
    print(f"Answer: {result.data}\n")

    # The agent will call the multiply_numbers tool
    result = calculator_agent.run_sync('Calculate 8 times 12')
    print(f"Answer: {result.data}\n")

    # The agent will call get_current_time
    result = calculator_agent.run_sync('What time is it?')
    print(f"Answer: {result.data}\n")


# Create a different agent with different tools
dice_agent = Agent(
    'anthropic:claude-sonnet-4-0',
    system_prompt='You are a game master. Use the dice rolling tool when players want to roll dice.',
)


@dice_agent.tool_plain
def roll_dice(num_dice: int = 1, sides: int = 6) -> dict[str, int | list[int]]:
    """Roll one or more dice.

    Args:
        num_dice: Number of dice to roll (default 1)
        sides: Number of sides on each die (default 6)

    Returns:
        Dictionary with individual rolls and total
    """
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(rolls)
    print(f"  [Tool called: roll_dice({num_dice}d{sides}) = {rolls}]")
    return {"rolls": rolls, "total": total}


def dice_example():
    """Agent with game-related tools."""
    print("=== Dice Rolling Agent ===")

    result = dice_agent.run_sync('Roll 2 six-sided dice for me')
    print(f"Result: {result.data}\n")

    result = dice_agent.run_sync('I need to roll 3d20')
    print(f"Result: {result.data}\n")


# Agent that chooses when to use tools
smart_agent = Agent(
    'anthropic:claude-sonnet-4-0',
    system_prompt='''You are a helpful assistant. Use tools when appropriate,
    but answer simple questions directly without tools.''',
)


@smart_agent.tool_plain
def search_web(query: str) -> str:
    """Search the web for information.

    Args:
        query: What to search for

    Returns:
        Search results (simulated)
    """
    print(f"  [Tool called: search_web('{query}')]")
    # In reality, this would call a real search API
    return f"[Simulated search results for: {query}]"


def smart_tool_usage():
    """Agent that decides when to use tools."""
    print("=== Smart Tool Usage ===")

    # Simple question - no tool needed
    result = smart_agent.run_sync('What is 2+2?')
    print(f"Q: What is 2+2?")
    print(f"A: {result.data}\n")

    # Complex question - might use tool
    result = smart_agent.run_sync('What is the current weather in Tokyo?')
    print(f"Q: What is the current weather in Tokyo?")
    print(f"A: {result.data}\n")


if __name__ == '__main__':
    # Run all examples
    calculator_example()
    dice_example()
    smart_tool_usage()

    print("=== Key Takeaways ===")
    print("1. Tools are registered with @agent.tool_plain decorator")
    print("2. Docstrings are important - they tell the LLM what the tool does")
    print("3. Type hints are required for parameters")
    print("4. The LLM decides when to call tools")
    print("5. Tools can return any JSON-serializable data")
    print("\nNote: @agent.tool_plain is for simple tools.")
    print("Use @agent.tool when you need access to RunContext.")
