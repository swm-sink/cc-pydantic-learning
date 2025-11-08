# Pydantic AI Learning Repository

A comprehensive, production-ready learning repository for mastering Pydantic AI with Claude Code.

**Updated**: November 2025 | **Pydantic AI**: v1.12.0 | **Claude**: Sonnet 4.5

## Overview

This repository is designed to support progressive, self-paced learning of Pydantic AI framework. It combines official examples, custom research notes, interactive Jupyter notebooks, and Claude Code automation to create an optimal learning environment.

### What's New in November 2025 🚀

- ✅ **Pydantic AI v1.12.0** support with latest features
- ✅ **Human-in-the-Loop** tool approval patterns
- ✅ **Durable Execution** with Temporal integration
- ✅ **Pydantic Evals** testing framework
- ✅ **MCP Integration** (Model Context Protocol)
- ✅ **Claude Sonnet 4.5** best practices (77.2% SWE-bench)
- ✅ **Multi-agent orchestration** patterns (90% improvement)
- ✅ **Interactive Notebooks** for hands-on learning
- ✅ **Logfire Observability** integration

## Repository Structure

```
cc-pydantic-learning/
├── pydantic-ai/              # Official Pydantic AI repository (reference)
├── docs/                     # Comprehensive documentation
│   ├── getting-started/      # Setup and first steps
│   ├── concepts/             # Core concepts (tools, deps, streaming, etc.)
│   ├── production/           # Production patterns (Logfire, MCP, deployment)
│   ├── anthropic-best-practices/  # Claude Sonnet 4.5 best practices
│   └── research-notes/       # Latest research and findings (Nov 2025)
├── notebooks/                # 🆕 Interactive Jupyter notebooks (PRIMARY LEARNING)
│   ├── 01-getting-started/   # Installation, first agent, structured outputs
│   ├── 02-intermediate/      # Tools, dependencies, error handling
│   ├── 03-advanced/          # Multi-agent, streaming, extended thinking
│   └── 04-production/        # Testing, observability, deployment
├── learning-paths/           # Structured learning progressions
├── examples/                 # Code examples by difficulty
│   ├── basic/               # 5 foundational examples ✅
│   ├── intermediate/        # 3 intermediate patterns ✅
│   └── advanced/            # 🆕 Multi-agent, human-in-loop, durable, etc.
├── evaluations/              # 🆕 Pydantic Evals test cases & benchmarks
├── snippets/                # Reusable code patterns
├── tests/                   # Pytest test suite
├── .claude/                 # Claude Code configuration
│   ├── commands/            # Custom slash commands (/run-example, etc.)
│   ├── agents/              # Custom subagents (learning-assistant, etc.)
│   └── settings.local.json  # Personal settings (gitignored)
└── CLAUDE.md               # Project context for Claude Code
```

## Learning Paths

This repository provides structured learning paths based on November 2025 best practices:

### 🟢 Beginner Path (1-2 weeks) - ✅ COMPLETE
- Basic agent creation, structured outputs, simple tools
- Async/await patterns, error handling
- Usage tracking and validation
- **Coverage**: 100% with 5 examples + docs

### 🟡 Intermediate Path (2-3 weeks) - 75% Complete
- Dependency injection and dynamic prompts
- Multiple tools and coordination
- Model configuration (Haiku/Sonnet/Opus)
- Context engineering with XML tags
- Testing with Pydantic Evals
- **Coverage**: 3 examples, need testing modules

### 🔴 Advanced Path (3-4 weeks) - Major Update
- **Multi-Agent Systems**: Orchestrator-worker patterns (90% improvement)
- **Claude Sonnet 4.5**: Extended thinking, long-horizon tasks
- **Production Features**: Human-in-the-loop, durable execution
- **Observability**: Logfire integration, monitoring
- **Coverage**: New section being developed

### 🎓 Expert Path (Ongoing)
- Domain specialization (RAG, fine-tuning)
- Distributed systems and enterprise deployment
- Custom evaluation metrics and performance optimization

See [learning-paths/](learning-paths/) and [docs/research-notes/2025-11-08-updated-learning-plan.md](docs/research-notes/2025-11-08-updated-learning-plan.md) for detailed guides.

## Quick Start

### Prerequisites

- Python 3.10 or higher (required for Pydantic AI v1.12.0)
- Claude Code CLI installed
- Basic understanding of Python and async programming
- Jupyter/JupyterLab for notebook-based learning (optional but recommended)

### Setup

1. Clone this repository (already done!)

2. Install Pydantic AI with latest features:
   ```bash
   pip install 'pydantic-ai[anthropic]>=1.12.0'
   ```

3. Install optional dependencies for full experience:
   ```bash
   # For notebooks
   pip install jupyter jupyterlab ipywidgets

   # For testing and evaluation
   pip install pytest pytest-asyncio pydantic-evals

   # For observability
   pip install logfire
   ```

4. Set up your API keys:
   ```bash
   export ANTHROPIC_API_KEY='your-key-here'
   ```

5. Start learning (choose your path):
   ```bash
   # Option 1: Interactive notebooks (recommended)
   jupyter lab notebooks/

   # Option 2: Run examples directly
   python examples/basic/hello_world.py

   # Option 3: Use Claude Code commands
   /run-example hello_world
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

### Official Resources (November 2025)
- [Pydantic AI Official Docs](https://ai.pydantic.dev/) - Complete documentation
- [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai) - Source code and examples
- [API Reference](https://ai.pydantic.dev/api/) - Full API documentation
- [Pydantic Logfire](https://logfire.pydantic.dev/) - Observability platform
- [Anthropic Claude Docs](https://docs.claude.com/) - Claude API documentation

### Key Updates & Articles (2025)
- [Pydantic AI v1 Release](https://pydantic.dev/articles/pydantic-ai-v1) - Production-ready framework
- [Q2 2025 Summary](https://pydantic.dev/articles/q2-2025-summary) - MCP, Evals, Dashboards
- [Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) - 90% improvement pattern
- [Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - Evolution of prompting
- [Claude Sonnet 4.5 Announcement](https://www.anthropic.com/news/claude-sonnet-4-5) - Best coding model

### Learning Tutorials
- [DataCamp Pydantic AI Guide](https://www.datacamp.com/tutorial/pydantic-ai-guide) - Beginner to advanced
- [Comprehensive Medium Guide](https://szeyusim.medium.com/a-comprehensive-guide-on-agent-development-with-pydantic-ai-beginner-to-advanced-12d90e0ba1a6) - 6 chapters
- [Anthropic Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) - Interactive course

### Best Practices Guides
- [Claude 4 Best Practices](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices) - Official guidance
- [Pydantic AI Tools Documentation](https://ai.pydantic.dev/tools/) - Function calling patterns
- [Multi-Agent Applications](https://ai.pydantic.dev/multi-agent-applications/) - Architecture patterns

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
