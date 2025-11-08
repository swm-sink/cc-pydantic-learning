"""
Model Configuration and Settings

Learning objectives:
- Configure model parameters (temperature, max_tokens)
- Use different providers and models
- Understand model settings hierarchy
- Implement fallback chains
- Choose the right model for your task

Model configuration affects response quality, cost, and latency.
"""

from pydantic_ai import Agent
from pydantic_ai.settings import ModelSettings


def basic_model_selection():
    """Using different models."""
    print("=== Model Selection ===")

    # Fast and cheap (Haiku)
    fast_agent = Agent('anthropic:claude-haiku-4-0')
    result = fast_agent.run_sync('Say hi!')
    print(f"Haiku: {result.data}")

    # Balanced (Sonnet)
    balanced_agent = Agent('anthropic:claude-sonnet-4-0')
    result = balanced_agent.run_sync('Say hi!')
    print(f"Sonnet: {result.data}")

    # Most capable (Opus)
    powerful_agent = Agent('anthropic:claude-opus-4-0')
    result = powerful_agent.run_sync('Say hi!')
    print(f"Opus: {result.data}\n")


def temperature_settings():
    """Control randomness with temperature."""
    print("=== Temperature Settings ===")

    question = 'Tell me a creative story idea in one sentence.'

    # Low temperature = more deterministic
    creative_low = Agent(
        'anthropic:claude-sonnet-4-0',
        model_settings=ModelSettings(temperature=0.2)
    )
    result = creative_low.run_sync(question)
    print(f"Low temp (0.2): {result.data}")

    # Medium temperature = balanced
    creative_med = Agent(
        'anthropic:claude-sonnet-4-0',
        model_settings=ModelSettings(temperature=0.7)
    )
    result = creative_med.run_sync(question)
    print(f"Med temp (0.7): {result.data}")

    # High temperature = more random/creative
    creative_high = Agent(
        'anthropic:claude-sonnet-4-0',
        model_settings=ModelSettings(temperature=1.0)
    )
    result = creative_high.run_sync(question)
    print(f"High temp (1.0): {result.data}\n")


def token_limits():
    """Configure max_tokens."""
    print("=== Token Limits ===")

    # Short response
    short_agent = Agent(
        'anthropic:claude-sonnet-4-0',
        model_settings=ModelSettings(max_tokens=50)
    )
    result = short_agent.run_sync('Explain Python in detail')
    print(f"Short (50 tokens): {result.data}")

    # Long response
    long_agent = Agent(
        'anthropic:claude-sonnet-4-0',
        model_settings=ModelSettings(max_tokens=500)
    )
    result = long_agent.run_sync('Explain Python in detail')
    print(f"Long (500 tokens): {result.data}\n")


def multiple_providers():
    """Use different LLM providers."""
    print("=== Multiple Providers ===")

    # Anthropic
    anthropic_agent = Agent('anthropic:claude-sonnet-4-0')
    result = anthropic_agent.run_sync('What is 2+2?')
    print(f"Anthropic: {result.data}")

    # OpenAI (if you have OPENAI_API_KEY set)
    try:
        openai_agent = Agent('openai:gpt-4')
        result = openai_agent.run_sync('What is 2+2?')
        print(f"OpenAI: {result.data}")
    except Exception as e:
        print(f"OpenAI: Skipped (key not set)")

    # Groq (fast inference)
    try:
        groq_agent = Agent('groq:llama-3.3-70b-versatile')
        result = groq_agent.run_sync('What is 2+2?')
        print(f"Groq: {result.data}")
    except Exception as e:
        print(f"Groq: Skipped (key not set or model unavailable)")

    print()


def runtime_model_override():
    """Override model at runtime."""
    print("=== Runtime Model Override ===")

    # Create agent with default model
    agent = Agent('anthropic:claude-sonnet-4-0')

    # Use default
    result = agent.run_sync('Hi!')
    print(f"Default (Sonnet): {result.data}")

    # Override with different model at runtime
    result = agent.run_sync(
        'Hi!',
        model='anthropic:claude-haiku-4-0'
    )
    print(f"Override (Haiku): {result.data}\n")


def settings_hierarchy():
    """Understand settings precedence."""
    print("=== Settings Hierarchy ===")

    # Agent-level defaults
    agent = Agent(
        'anthropic:claude-sonnet-4-0',
        model_settings=ModelSettings(
            temperature=0.5,
            max_tokens=100
        )
    )

    # Use agent defaults
    result = agent.run_sync('Tell me about Python')
    print(f"Agent defaults: {len(result.data)} chars")

    # Override at runtime
    result = agent.run_sync(
        'Tell me about Python',
        model_settings=ModelSettings(max_tokens=200)  # Runtime override
    )
    print(f"Runtime override: {len(result.data)} chars\n")


def choosing_the_right_model():
    """Guide for model selection."""
    print("=== Model Selection Guide ===")

    print("""
    **Claude Haiku** (claude-haiku-4-0):
    - Fast and cheap
    - Good for: Simple tasks, high volume, real-time
    - Examples: Classification, basic Q&A, data extraction

    **Claude Sonnet** (claude-sonnet-4-0):
    - Balanced performance and cost
    - Good for: Most applications, complex reasoning
    - Examples: Customer support, code generation, analysis

    **Claude Opus** (claude-opus-4-0):
    - Most capable, highest cost
    - Good for: Complex tasks, high accuracy needed
    - Examples: Research, advanced reasoning, creative work

    **Temperature Guide**:
    - 0.0-0.3: Focused, deterministic (code, facts)
    - 0.4-0.7: Balanced (general purpose)
    - 0.8-1.0: Creative, varied (stories, brainstorming)

    **Max Tokens**:
    - 50-100: Very short responses
    - 100-500: Normal responses
    - 500-2000: Long-form content
    - 2000+: Very detailed content
    """)


def cost_optimization():
    """Strategies for reducing costs."""
    print("\n=== Cost Optimization ===")

    print("""
    1. Use Haiku for simple tasks
    2. Set appropriate max_tokens
    3. Use lower temperature for factual tasks
    4. Cache system prompts when possible
    5. Batch similar requests
    6. Use streaming for long responses
    7. Monitor usage with result.usage()
    """)


if __name__ == '__main__':
    # Run examples
    basic_model_selection()
    temperature_settings()
    token_limits()
    multiple_providers()
    runtime_model_override()
    settings_hierarchy()
    choosing_the_right_model()
    cost_optimization()

    print("\n=== Key Takeaways ===")
    print("1. Choose model based on task complexity")
    print("2. Temperature affects randomness")
    print("3. max_tokens controls response length")
    print("4. Settings can be set at agent or runtime level")
    print("5. Runtime settings override agent settings")
    print("6. Different providers have different models")
    print("7. Monitor usage to optimize costs")
    print("8. Use ModelSettings for fine-grained control")
