# Creating Your First Agent

Learn how to create a basic Pydantic AI agent.

## Learning Objectives

After completing this guide, you will:

- Understand what a Pydantic AI agent is
- Know how to create and configure an agent
- Be able to run agents synchronously and asynchronously
- Understand system prompts and their importance

## What is an Agent?

A Pydantic AI `Agent` is the core abstraction for interacting with Large Language Models (LLMs). It combines:

- A **model** (e.g., Claude, GPT-4)
- **System instructions** (how the agent should behave)
- **Tools** (optional capabilities the agent can use)
- **Result type** (optional structured output format)

Think of an agent as a configured AI assistant with specific instructions and capabilities.

## The Simplest Agent

Here's the most basic agent possible:

```python
from pydantic_ai import Agent

# Create an agent with a model
agent = Agent('anthropic:claude-sonnet-4-0')

# Run it synchronously
result = agent.run_sync('What is 2 + 2?')

# Print the response
print(result.data)  # Output: "4" (or similar explanation)
```

**Key points**:
- `Agent()` creates a new agent instance
- Model string format: `provider:model-name`
- `run_sync()` executes synchronously (blocks until complete)
- `result.data` contains the response

## Adding System Instructions

Make your agent behave in specific ways:

```python
from pydantic_ai import Agent

# Agent with personality
agent = Agent(
    'anthropic:claude-sonnet-4-0',
    system_prompt='You are a helpful math tutor. Explain concepts clearly and encourage learning.',
)

result = agent.run_sync('What is 2 + 2?')
print(result.data)
# Now you'll get a more educational response!
```

## Async Agents

For better performance in production:

```python
import asyncio
from pydantic_ai import Agent

agent = Agent(
    'anthropic:claude-sonnet-4-0',
    system_prompt='Be concise and helpful.',
)

async def main():
    # Run asynchronously
    result = await agent.run('Tell me a fun fact about Python')
    print(result.data)

# Run the async function
asyncio.run(main())
```

**Why async?**
- Non-blocking I/O
- Better for multiple concurrent requests
- Standard in production applications

## Multiple Interactions

Agents maintain conversation context:

```python
from pydantic_ai import Agent

agent = Agent('anthropic:claude-sonnet-4-0')

# First query
result1 = agent.run_sync('My name is Alex')
print(result1.data)

# Follow-up query (with context)
result2 = agent.run_sync('What is my name?')
print(result2.data)  # Should remember "Alex"
```

## Model Selection

Different models for different needs:

```python
# Fast and cheap (good for learning)
agent_fast = Agent('anthropic:claude-haiku-4-0')

# Balanced (recommended)
agent_balanced = Agent('anthropic:claude-sonnet-4-0')

# Most capable (for complex tasks)
agent_advanced = Agent('anthropic:claude-opus-4-0')

# OpenAI alternative
agent_openai = Agent('openai:gpt-4')
```

## System Prompt Best Practices

Good system prompts are:

1. **Clear**: Specific instructions, not vague
2. **Concise**: Under 200 words usually
3. **Role-based**: "You are a..."
4. **Task-focused**: What should the agent do?

Examples:

```python
# ❌ Too vague
agent = Agent('...', system_prompt='Be helpful')

# ✅ Clear and specific
agent = Agent(
    '...',
    system_prompt='''You are a Python programming tutor.

    - Explain concepts clearly
    - Provide working code examples
    - Encourage best practices
    - Be patient and encouraging
    '''
)
```

## Complete Example

Here's a complete, runnable example:

```python
"""
My first Pydantic AI agent.

Learning objectives:
- Create an agent
- Configure system prompt
- Run sync and async
- Handle responses
"""

import asyncio
from pydantic_ai import Agent

# Create agent with clear instructions
agent = Agent(
    'anthropic:claude-sonnet-4-0',
    system_prompt='''You are a friendly coding assistant.

    When answering questions:
    - Be concise but thorough
    - Provide code examples when relevant
    - Explain your reasoning
    ''',
)

def sync_example():
    """Run agent synchronously."""
    print("=== Sync Example ===")
    result = agent.run_sync('What is a Python decorator?')
    print(result.data)

async def async_example():
    """Run agent asynchronously."""
    print("\n=== Async Example ===")
    result = await agent.run('Explain async/await in Python')
    print(result.data)

if __name__ == '__main__':
    # Run sync example
    sync_example()

    # Run async example
    asyncio.run(async_example())
```

Save this as `examples/basic/first_agent.py` and run it:

```bash
python examples/basic/first_agent.py
```

## Understanding the Result Object

When you run an agent, you get a `RunResult` object:

```python
result = agent.run_sync('Hello!')

# Access the response
print(result.data)  # The actual response

# Access metadata
print(result.usage())  # Token usage info
print(result.messages())  # Conversation messages
```

## Common Pitfalls

### 1. Forgetting to await async calls

```python
# ❌ Wrong
result = agent.run('Hello')  # Missing await!

# ✅ Correct
result = await agent.run('Hello')
```

### 2. Not handling errors

```python
# ✅ Better
try:
    result = agent.run_sync('Hello')
    print(result.data)
except Exception as e:
    print(f"Error: {e}")
```

### 3. API key not set

Make sure `ANTHROPIC_API_KEY` is in your environment!

## Practice Exercises

1. **Exercise 1**: Create an agent that acts as a historian and ask it 3 questions
2. **Exercise 2**: Create an agent with different system prompts and compare responses
3. **Exercise 3**: Modify the complete example to use a different model

## Next Steps

1. ✅ Create and run your first agent
2. 📖 Read about [Structured Outputs](../concepts/structured-outputs.md)
3. 🔨 Try [Basic Tools Tutorial](../tutorials/basic-tools-tutorial.md)
4. 📝 Update your progress in `PROGRESS.md`

## Additional Resources

- [Official Agent Docs](https://ai.pydantic.dev/agents/)
- [Models Overview](https://ai.pydantic.dev/models/)
- [Examples in pydantic-ai repo](../../pydantic-ai/examples/)

---

**Checkpoint**: Can you create an agent with custom instructions and run it both sync and async? If yes, you're ready to move on!
