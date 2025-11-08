"""
Async Agent Example

Learning objectives:
- Understand async/await with Pydantic AI
- Learn when to use async vs sync
- See how to handle multiple concurrent requests

Async agents are better for production use and multiple concurrent requests.
"""

import asyncio
from pydantic_ai import Agent


# Create agent at module level (can be reused)
agent = Agent(
    'anthropic:claude-sonnet-4-0',
    system_prompt='You are a helpful assistant. Be brief and clear.',
)


async def single_query():
    """Run a single async query."""
    print("=== Single Async Query ===")
    result = await agent.run('What is Pydantic AI in one sentence?')
    print(result.data)


async def multiple_queries():
    """Run multiple queries concurrently."""
    print("\n=== Multiple Concurrent Queries ===")

    # Define multiple questions
    questions = [
        'What is Python?',
        'What is async programming?',
        'What is type safety?',
    ]

    # Create tasks for concurrent execution
    tasks = [agent.run(q) for q in questions]

    # Wait for all to complete
    results = await asyncio.gather(*tasks)

    # Print all results
    for question, result in zip(questions, results):
        print(f"\nQ: {question}")
        print(f"A: {result.data}")


async def conversation():
    """Have a multi-turn conversation."""
    print("\n=== Multi-turn Conversation ===")

    # First message
    result1 = await agent.run('My favorite color is blue.')
    print(f"Agent: {result1.data}")

    # Follow-up (maintains context)
    result2 = await agent.run('What is my favorite color?')
    print(f"Agent: {result2.data}")


async def main():
    """Run all async examples."""
    await single_query()
    await multiple_queries()
    await conversation()


if __name__ == '__main__':
    # Run the async main function
    asyncio.run(main())

    # Why use async?
    # 1. Non-blocking I/O - other code can run while waiting for LLM
    # 2. Concurrent requests - handle multiple queries at once
    # 3. Production standard - most web frameworks use async
    # 4. Better resource utilization
