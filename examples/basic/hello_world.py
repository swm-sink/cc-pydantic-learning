"""
Hello World - Your First Pydantic AI Agent

Learning objectives:
- Understand basic agent creation
- Learn how to run agents synchronously
- See how to access agent responses

This is the simplest possible Pydantic AI agent.
"""

from pydantic_ai import Agent


def main():
    """Create and run a basic hello world agent."""

    # Create agent with a specific model
    # Format: 'provider:model-name'
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        system_prompt='Be concise and friendly. Reply with one sentence.',
    )

    # Run the agent with a simple query
    # run_sync() blocks until the response is ready
    result = agent.run_sync('Say hello and introduce yourself!')

    # Access the response through result.data
    print("Agent response:")
    print(result.data)

    # You can also see token usage
    print("\nUsage information:")
    print(result.usage())


if __name__ == '__main__':
    # Run the example
    main()

    # Output will be something like:
    # Agent response:
    # Hello! I'm Claude, an AI assistant created by Anthropic to be helpful, harmless, and honest.
    #
    # Usage information:
    # Usage(requests=1, request_tokens=52, response_tokens=24, total_tokens=76)
