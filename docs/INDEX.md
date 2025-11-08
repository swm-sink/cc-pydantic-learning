# Documentation Index

Complete guide to all documentation in this repository.

## Getting Started

Start here if you're new to Pydantic AI:

1. **[Installation Guide](getting-started/01-installation.md)** - Set up your environment
2. **[First Agent](getting-started/02-first-agent.md)** - Create your first agent

## Core Concepts

Deep dives into key Pydantic AI concepts:

- **[Structured Outputs](concepts/structured-outputs.md)** - Get typed, validated data from agents
- **[Tools and Function Calling](concepts/tools.md)** - Give agents real capabilities
- **[Dependency Injection](concepts/dependency-injection.md)** - Pass resources to agents *(Coming soon)*
- **[Error Handling](concepts/error-handling.md)** - Handle failures gracefully *(Coming soon)*

## Examples

### Basic Examples (Beginner)

Located in `examples/basic/`:

1. **hello_world.py** - Simplest possible agent
2. **async_agent.py** - Async patterns and concurrency
3. **structured_outputs.py** - Extract typed data from text
4. **simple_tools.py** - Basic function calling
5. **error_handling.py** - Validation and error patterns

### Intermediate Examples

Located in `examples/intermediate/`:

1. **dependency_injection.py** - Using RunContext and deps
2. **multiple_tools.py** - Coordinating multiple tools
3. **model_configuration.py** - Configure models and settings
4. **dynamic_prompts.py** *(Coming soon)* - Context-aware instructions

### Advanced Examples

Located in `examples/advanced/`:

*(Coming soon)*

- Multi-agent systems
- Streaming responses
- Custom model providers
- RAG patterns

## Tutorials

Step-by-step guides:

*(Coming soon)*

- Building a bank support agent
- Creating a research assistant
- Implementing tool-based workflows

## Learning Paths

Structured progressions through the material:

- **[Learning Paths Overview](../learning-paths/README.md)** - Beginner → Intermediate → Advanced

## Snippets

Reusable code patterns:

- **[Agent Patterns](../snippets/agent-patterns.py)** - Common agent configurations
- **[Tool Patterns](../snippets/tool-patterns.py)** *(Coming soon)* - Tool design patterns
- **[Testing Patterns](../snippets/testing-patterns.py)** *(Coming soon)* - Test utilities

## Research Notes

Development and learning notes:

- **[Repository Setup](research-notes/2025-11-08-repository-setup.md)** - Initial research and setup
- **[Expansion Plan](research-notes/2025-11-08-expansion-plan.md)** - Repository expansion roadmap

## Reference

- **[Progress Tracker](../PROGRESS.md)** - Track your learning progress
- **[Contributing Guide](../CONTRIBUTING.md)** - How to contribute
- **[README](../README.md)** - Repository overview

## External Resources

### Official Documentation

- [Pydantic AI Official Docs](https://ai.pydantic.dev/)
- [API Reference](https://ai.pydantic.dev/api/)
- [GitHub Repository](https://github.com/pydantic/pydantic-ai)

### Tutorials and Guides

- [DataCamp Tutorial](https://www.datacamp.com/tutorial/pydantic-ai-guide)
- [Comprehensive Guide on Medium](https://szeyusim.medium.com/a-comprehensive-guide-on-agent-development-with-pydantic-ai-beginner-to-advanced-12d90e0ba1a6)
- [DeepLearning.AI Course](https://www.deeplearning.ai/short-courses/pydantic-for-llm-workflows/)

### Community

- [GitHub Discussions](https://github.com/pydantic/pydantic-ai/discussions)
- [Pydantic Slack](https://pydantic.dev/slack)

## Quick Navigation

**By Topic:**

- **Agents**: [First Agent](getting-started/02-first-agent.md), [Agent Patterns](../snippets/agent-patterns.py)
- **Structured Data**: [Structured Outputs](concepts/structured-outputs.md), [Examples](../examples/basic/structured_outputs.py)
- **Tools**: [Tools Concepts](concepts/tools.md), [Simple Tools](../examples/basic/simple_tools.py), [Multiple Tools](../examples/intermediate/multiple_tools.py)
- **Dependencies**: [DI Concepts](concepts/dependency-injection.md), [DI Examples](../examples/intermediate/dependency_injection.py)
- **Configuration**: [Model Config](../examples/intermediate/model_configuration.py)
- **Testing**: [Test Examples](../tests/), [Pytest Config](../pytest.ini)

**By Difficulty:**

- **Beginner**: Start with [Installation](getting-started/01-installation.md) → [First Agent](getting-started/02-first-agent.md) → [Basic Examples](../examples/basic/)
- **Intermediate**: Study [Concepts](concepts/) → Try [Intermediate Examples](../examples/intermediate/)
- **Advanced**: Review [Advanced Examples](../examples/advanced/) → Study official examples in `pydantic-ai/`

---

**Last Updated**: 2025-11-08

**Repository**: [cc-pydantic-learning](../)

**Status**: Active development
