# Pydantic AI Interactive Notebooks

Welcome to the **primary learning interface** for Pydantic AI! These Jupyter notebooks provide hands-on, interactive learning experiences.

## 📚 Notebook Structure

### 01-getting-started/
Introduction to Pydantic AI fundamentals:
- Installation and setup
- Your first agent
- Structured outputs with Pydantic models
- Basic tool usage

**Time**: 1-2 hours
**Prerequisites**: Python 3.10+, basic Python knowledge

### 02-intermediate/
Core patterns and advanced features:
- Function calling and tools
- Dependency injection
- Error handling and validation
- Model configuration

**Time**: 3-4 hours
**Prerequisites**: Completion of 01-getting-started

### 03-advanced/
Production-ready patterns:
- Multi-agent systems and orchestration
- Streaming responses
- Extended thinking mode (Claude Sonnet 4.5)
- Human-in-the-loop approval

**Time**: 4-6 hours
**Prerequisites**: Completion of 02-intermediate

### 04-production/
Deployment and observability:
- Testing with Pydantic Evals
- Logfire observability integration
- MCP (Model Context Protocol)
- Deployment patterns

**Time**: 3-4 hours
**Prerequisites**: Completion of 03-advanced

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Core dependencies
pip install 'pydantic-ai[anthropic]>=1.12.0'

# Notebook support
pip install jupyter jupyterlab ipywidgets

# Optional: Testing and observability
pip install pydantic-evals logfire
```

### 2. Set Up API Keys

```bash
export ANTHROPIC_API_KEY='your-key-here'
```

### 3. Launch Jupyter

```bash
# From repository root
jupyter lab notebooks/

# Or from this directory
jupyter lab
```

### 4. Start with 01-getting-started

Open `01-getting-started/01-installation.ipynb` and work through the notebooks sequentially.

---

## 📖 Learning Path

Each notebook is designed to be completed in order:

```
01-getting-started/
├── 01-installation.ipynb          ⏱️ 15 min
├── 02-first-agent.ipynb           ⏱️ 30 min
└── 03-structured-outputs.ipynb    ⏱️ 30 min

02-intermediate/
├── 01-tools-and-functions.ipynb   ⏱️ 45 min
├── 02-dependency-injection.ipynb  ⏱️ 45 min
├── 03-error-handling.ipynb        ⏱️ 30 min
└── 04-model-configuration.ipynb   ⏱️ 30 min

03-advanced/
├── 01-multi-agent-systems.ipynb   ⏱️ 60 min
├── 02-streaming-responses.ipynb   ⏱️ 45 min
├── 03-extended-thinking.ipynb     ⏱️ 45 min
└── 04-human-in-loop.ipynb         ⏱️ 60 min

04-production/
├── 01-testing-evaluation.ipynb    ⏱️ 45 min
├── 02-observability-logfire.ipynb ⏱️ 45 min
├── 03-mcp-integration.ipynb       ⏱️ 45 min
└── 04-deployment-patterns.ipynb   ⏱️ 45 min
```

**Total Time**: ~12-14 hours

---

## 💡 Tips for Success

### Before You Start
- ✅ Ensure Python 3.10+ is installed
- ✅ Set up your Anthropic API key
- ✅ Install all dependencies
- ✅ Clone the repository with examples

### While Learning
- 📝 Run all code cells sequentially
- 🎯 Complete exercises before moving forward
- 🐛 Debug errors before proceeding
- 💭 Experiment with modifications

### Best Practices
- 🔄 Restart kernel if you get unexpected errors
- 💾 Save your work frequently
- 📚 Reference official docs when stuck
- 🤝 Use Claude Code commands for help

---

## 🛠️ Troubleshooting

### Common Issues

**"Module not found: pydantic_ai"**
```bash
pip install 'pydantic-ai[anthropic]>=1.12.0'
```

**"API key not found"**
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

**"Kernel died unexpectedly"**
- Restart kernel: Kernel → Restart Kernel
- Check Python version: `python --version` (must be 3.10+)

**Rate Limits**
- Wait a few moments between API calls
- Use smaller examples if testing frequently

---

## 📚 Additional Resources

### Official Documentation
- [Pydantic AI Docs](https://ai.pydantic.dev/)
- [API Reference](https://ai.pydantic.dev/api/)
- [Anthropic Claude Docs](https://docs.claude.com/)

### Examples
- See `../examples/` for standalone Python scripts
- See `../pydantic-ai/examples/` for official examples

### Help Commands
- `/pydantic-help` - Get help with concepts
- `/run-example` - Run an example with explanation
- `/create-agent` - Interactive agent creation wizard

---

## 🎯 Learning Objectives

By completing these notebooks, you will:

### Fundamentals (01-getting-started)
- ✅ Create and run basic Pydantic AI agents
- ✅ Use structured outputs with Pydantic models
- ✅ Implement simple tools and function calling
- ✅ Understand sync vs async patterns

### Intermediate (02-intermediate)
- ✅ Master dependency injection
- ✅ Handle errors and retries elegantly
- ✅ Configure models and parameters
- ✅ Build multi-tool agents

### Advanced (03-advanced)
- ✅ Design multi-agent systems
- ✅ Implement streaming responses
- ✅ Use extended thinking for complex reasoning
- ✅ Add human-in-the-loop approval

### Production (04-production)
- ✅ Test agents with Pydantic Evals
- ✅ Monitor with Logfire observability
- ✅ Integrate MCP toolsets
- ✅ Deploy production-ready agents

---

## 🤝 Contributing

Found a bug or have a suggestion? Please:
1. Check existing issues
2. Open a new issue with details
3. Submit a pull request if you have a fix

---

## 📄 License

These notebooks are part of the Pydantic AI Learning Repository.
See LICENSE for details.

---

**Happy Learning! 🚀**

Start with `01-getting-started/01-installation.ipynb` and build your way to production-ready AI agents.
