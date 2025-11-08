# Contributing to This Learning Repository

Thank you for your interest in contributing! While this is primarily a personal learning repository, contributions are welcome.

## Types of Contributions

### 1. Documentation Improvements

- Fix typos or clarify explanations
- Add more examples or explanations
- Improve learning path descriptions
- Add helpful resources

### 2. Code Examples

- Add new examples (basic, intermediate, advanced)
- Improve existing examples
- Add more comments for clarity
- Include tests for examples

### 3. Learning Resources

- Curate helpful external resources
- Add notes about useful patterns
- Share insights from Pydantic AI exploration

### 4. Claude Code Enhancements

- Improve slash commands
- Add new custom subagents
- Enhance hooks configuration
- Share useful MCP servers

## Guidelines

### Code Style

Follow the conventions in `CLAUDE.md`:

- Use type hints everywhere
- Follow PEP 8
- Include comprehensive docstrings
- Add inline comments explaining concepts
- Use async/await appropriately

### Documentation

- Write clear, concise explanations
- Include code examples
- Add learning objectives
- Link to official docs
- Suggest related topics

### Examples

Structure examples as:

```python
"""
Brief description.

Learning objectives:
- Objective 1
- Objective 2
- Objective 3
"""

# Imports
from pydantic_ai import Agent

# Main code with comments
# Explain what each part does

if __name__ == '__main__':
    # Example usage
    pass
```

### Commits

- Use clear, descriptive commit messages
- One logical change per commit
- Reference learning path or topic

Example commit messages:
- `docs: Add guide on dependency injection`
- `examples: Add bank support agent tutorial`
- `claude: Add slash command for testing agents`

## Submitting Changes

1. **Fork the repository** (if you have access)
2. **Create a branch**: `git checkout -b feature/your-feature`
3. **Make changes**: Follow guidelines above
4. **Test**: Run examples to ensure they work
5. **Commit**: With clear messages
6. **Push**: `git push origin feature/your-feature`
7. **Pull Request**: Describe what you've added

## What NOT to Contribute

Please don't:

- ❌ Commit API keys or secrets
- ❌ Modify the official pydantic-ai repository directly
- ❌ Add production code (this is for learning)
- ❌ Remove learning scaffolding or comments

## Questions?

Open an issue or discussion to:

- Ask questions about Pydantic AI
- Suggest improvements
- Share insights
- Request clarifications

## License

By contributing, you agree that your contributions will be licensed under the same license as this repository.

## Recognition

Contributors will be acknowledged in the README!

---

**Remember**: The goal is to create the best possible learning resource for Pydantic AI. All contributions should support that mission.
