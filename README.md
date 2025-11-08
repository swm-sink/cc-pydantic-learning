# Pydantic AI Learning Repository

A comprehensive research and learning repository for mastering Pydantic AI with Claude Code.

## Overview

This repository is designed to support progressive, self-paced learning of Pydantic AI framework. It combines official examples, custom research notes, and Claude Code automation to create an optimal learning environment.

## Repository Structure

```
cc-pydantic-learning/
├── pydantic-ai/              # Official Pydantic AI repository (cloned)
├── docs/                     # Comprehensive documentation
│   ├── getting-started/      # Beginner tutorials and setup guides
│   ├── concepts/             # Core concepts and theory
│   ├── tutorials/            # Step-by-step tutorials
│   ├── examples/             # Practical examples with explanations
│   └── research-notes/       # Personal research and findings
├── learning-paths/           # Structured learning progressions
├── examples/                 # Code examples by difficulty
│   ├── basic/               # Foundational examples
│   ├── intermediate/        # Intermediate patterns
│   └── advanced/            # Advanced implementations
├── snippets/                # Reusable code snippets
├── .claude/                 # Claude Code configuration
│   ├── commands/            # Custom slash commands
│   ├── agents/              # Custom subagents
│   └── settings.local.json  # Personal settings (gitignored)
└── CLAUDE.md               # Project context for Claude Code
```

## Learning Paths

This repository provides structured learning paths:

1. **Beginner Path**: Basic agent creation, structured outputs, simple tools
2. **Intermediate Path**: Dependency injection, multi-model support, error handling
3. **Advanced Path**: Multi-agent systems, production deployment, custom models

See [learning-paths/](learning-paths/) for detailed progression guides.

## Quick Start

### Prerequisites

- Python 3.9 or higher
- Claude Code CLI installed
- Basic understanding of Python and async programming

### Setup

1. Clone this repository (already done!)
2. Install Pydantic AI:
   ```bash
   pip install pydantic-ai
   ```

3. Set up your API keys:
   ```bash
   export ANTHROPIC_API_KEY='your-key-here'
   ```

4. Start with the beginner path:
   ```bash
   cd learning-paths/01-beginner
   ```

## Using This Repository with Claude Code

This repository is optimized for use with Claude Code:

- **CLAUDE.md**: Contains project context and coding standards
- **Custom Commands**: Use `/pydantic-help`, `/run-example`, `/create-agent`
- **Custom Agents**: Specialized subagents for learning assistance
- **Hooks**: Automatic testing and formatting on code changes

### Available Slash Commands

- `/pydantic-help [topic]` - Get help on specific Pydantic AI topics
- `/run-example [name]` - Run an example with explanation
- `/create-agent` - Interactive agent creation wizard
- `/test-agent [file]` - Test an agent with validation

## Resources

### Official Resources
- [Pydantic AI Official Docs](https://ai.pydantic.dev/)
- [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai)
- [API Reference](https://ai.pydantic.dev/api/)

### Learning Materials
- [DataCamp Tutorial](https://www.datacamp.com/tutorial/pydantic-ai-guide)
- [Comprehensive Medium Guide](https://szeyusim.medium.com/a-comprehensive-guide-on-agent-development-with-pydantic-ai-beginner-to-advanced-12d90e0ba1a6)
- [DeepLearning.AI Course](https://www.deeplearning.ai/short-courses/pydantic-for-llm-workflows/)

## Progress Tracking

Track your learning progress in [PROGRESS.md](PROGRESS.md).

## Contributing

This is a personal learning repository, but contributions and suggestions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Research Notes

Detailed research findings and insights are documented in [docs/research-notes/](docs/research-notes/).

## License

This repository contains examples and learning materials. The official Pydantic AI code in `pydantic-ai/` follows its original MIT license.

---

**Note**: This is a research and learning repository created with Claude Code. It's designed to help developers understand and master Pydantic AI through progressive, hands-on learning.
