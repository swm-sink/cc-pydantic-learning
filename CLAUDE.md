# Claude Code Context for Pydantic AI Learning Repository

## Project Overview

This is a **research and learning repository** for Pydantic AI, designed to support progressive self-paced learning. The primary goal is to understand and master the Pydantic AI framework through hands-on examples, documentation, and experimentation.

## Tech Stack

- **Python**: 3.9+
- **Framework**: Pydantic AI (GenAI Agent Framework)
- **LLM Providers**: Anthropic Claude, OpenAI (for testing)
- **Testing**: pytest, pytest-cov
- **Code Quality**: black, ruff, mypy

## Repository Structure

```
cc-pydantic-learning/
├── pydantic-ai/              # Official repo (READ-ONLY reference)
├── docs/                     # All documentation
├── learning-paths/           # Structured learning progressions
├── examples/                 # Working code examples (basic/intermediate/advanced)
├── snippets/                 # Reusable code snippets
└── .claude/                  # Claude Code configuration
```

## Development Conventions

### File Organization

- **Examples**: Place in `examples/{basic|intermediate|advanced}/`
- **Documentation**: Use `docs/` with appropriate subdirectory
- **Research Notes**: Add to `docs/research-notes/` with date prefix (YYYY-MM-DD)
- **Snippets**: Short, reusable code in `snippets/` with descriptive names

### Code Style

- Use **type hints** everywhere (Pydantic AI is fully type-safe)
- Follow **PEP 8** conventions
- Use **async/await** for agent operations when applicable
- Include **docstrings** for all functions and classes
- Add **inline comments** for complex logic

### Naming Conventions

- **Files**: Use snake_case (e.g., `basic_agent.py`)
- **Classes**: Use PascalCase (e.g., `CustomerSupportAgent`)
- **Functions**: Use snake_case (e.g., `create_agent`)
- **Constants**: Use UPPER_CASE (e.g., `DEFAULT_MODEL`)

### Testing Standards

- Place tests in `tests/` directory
- Match structure: `tests/examples/basic/test_basic_agent.py`
- Use pytest fixtures for common setups
- Include docstrings explaining what each test validates

## Common Commands

```bash
# Run tests
pytest -v

# Run with coverage
pytest --cov=examples --cov-report=html

# Format code
black .

# Lint code
ruff check .

# Type check
mypy examples/
```

## Pydantic AI Specific Guidelines

### Agent Creation Pattern

```python
from pydantic_ai import Agent

# Always specify model and system instructions
agent = Agent(
    'anthropic:claude-sonnet-4-0',
    system_prompt='Clear, specific instructions',
    deps_type=YourDepsType,  # If using dependency injection
)
```

### Dependency Injection

- Use dataclasses for dependencies when multiple objects needed
- Access via `RunContext[YourDepsType]`
- Always type-annotate dependencies

### Structured Outputs

- Define Pydantic models for structured responses
- Use `result_type` parameter when creating agents
- Validate outputs automatically with Pydantic

### Tools

- Register with `@agent.tool` or `@agent.tool_plain`
- Include clear docstrings (used for schema generation)
- Use `RunContext` as first parameter for context-aware tools

## Do NOT

- ❌ Modify the official `pydantic-ai/` repository directly
- ❌ Commit API keys or secrets
- ❌ Skip type hints (this is a type-safe framework!)
- ❌ Create examples without corresponding documentation
- ❌ Use synchronous methods when async is more appropriate

## Research Workflow

When researching a new Pydantic AI concept:

1. **Explore**: Read official docs and examples in `pydantic-ai/`
2. **Document**: Create notes in `docs/research-notes/YYYY-MM-DD-topic.md`
3. **Implement**: Write example in appropriate `examples/` subdirectory
4. **Test**: Add tests to verify behavior
5. **Refine**: Update learning path documentation

## Claude Code Integration

This repository uses:

- **Custom Commands**: Slash commands for common tasks
- **Custom Agents**: Specialized subagents for learning assistance
- **Hooks**: Automatic formatting and testing
- **MCP Servers**: (Future) Integration with documentation servers

## Learning Approach

Follow the **Research → Plan → Code** workflow:

1. Research the topic using official docs and examples
2. Plan the implementation in plain language
3. Code the solution with tests
4. Document learnings

## Important Notes

- This is a **learning repository**, not production code
- Prioritize **understanding** over optimization
- **Document discoveries** as you learn
- **Experiment freely** - this is a safe space to learn
- Use **Claude Code's plan mode** for exploring complex topics

## Key Resources

- Official Docs: https://ai.pydantic.dev/
- API Reference: https://ai.pydantic.dev/api/
- GitHub: https://github.com/pydantic/pydantic-ai
- Examples: See `pydantic-ai/examples/` for official examples
