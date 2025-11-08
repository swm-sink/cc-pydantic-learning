# Installation and Setup

Getting started with Pydantic AI in this learning repository.

## Prerequisites

Before you begin, ensure you have:

- **Python 3.9 or higher**: Check with `python --version`
- **pip or uv**: Package manager for Python
- **Virtual environment** (recommended): `venv` or `conda`
- **API Keys**: From Anthropic, OpenAI, or other providers

## Installation Methods

### Method 1: Using pip (Recommended for Learning)

```bash
# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Unix/MacOS
# or
.\venv\Scripts\activate   # On Windows

# Install Pydantic AI
pip install pydantic-ai

# Install optional dependencies
pip install 'pydantic-ai[anthropic]'  # For Claude
pip install 'pydantic-ai[openai]'     # For OpenAI
pip install 'pydantic-ai[logfire]'    # For observability
```

### Method 2: Using uv (Faster)

```bash
# Install with uv
uv pip install pydantic-ai

# Or with extras
uv pip install 'pydantic-ai[anthropic,openai,logfire]'
```

### Method 3: Development Installation

```bash
# Clone and install from the official repo
cd pydantic-ai
pip install -e .

# With all extras for development
pip install -e '.[dev]'
```

## Setting Up API Keys

### Anthropic Claude (Recommended)

```bash
# Set environment variable
export ANTHROPIC_API_KEY='your-key-here'

# Or add to your shell profile
echo 'export ANTHROPIC_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### OpenAI

```bash
export OPENAI_API_KEY='your-key-here'
```

### Multiple Providers

You can set up multiple providers for testing:

```bash
export ANTHROPIC_API_KEY='...'
export OPENAI_API_KEY='...'
export GEMINI_API_KEY='...'
```

## Verify Installation

Create a test file `test_install.py`:

```python
"""Verify Pydantic AI installation."""

from pydantic_ai import Agent

# Create a simple agent
agent = Agent('anthropic:claude-sonnet-4-0')

# Run a simple query
result = agent.run_sync('Say hello!')

print(result.data)
```

Run it:

```bash
python test_install.py
```

You should see a greeting response from Claude!

## Installing Development Tools

For the best learning experience:

```bash
# Code quality tools
pip install black ruff mypy

# Testing tools
pip install pytest pytest-cov pytest-asyncio

# Documentation tools
pip install mkdocs mkdocs-material
```

## Project-Specific Setup

For this learning repository:

```bash
# Navigate to the repo
cd /home/user/cc-pydantic-learning

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# Or create your own requirements.txt
cat > requirements.txt << EOF
pydantic-ai[anthropic,openai]
pytest
pytest-asyncio
black
ruff
mypy
EOF

pip install -r requirements.txt
```

## IDE Setup

### VS Code

Recommended extensions:
- Python (Microsoft)
- Pylance
- Black Formatter
- Ruff

### PyCharm

Configure:
- Python interpreter to your venv
- Enable type checking
- Set up Black as formatter

## Troubleshooting

### Import Error

```
ModuleNotFoundError: No module named 'pydantic_ai'
```

**Solution**: Make sure you've activated your virtual environment and installed the package.

### API Key Not Found

```
AuthenticationError: API key not set
```

**Solution**: Verify your environment variable is set: `echo $ANTHROPIC_API_KEY`

### Version Conflicts

```
pip install --upgrade pydantic-ai
```

## Next Steps

1. ✅ Verify installation works
2. 📖 Read [02-first-agent.md](02-first-agent.md)
3. 🚀 Try the hello world example
4. 📚 Explore the official examples in `pydantic-ai/examples/`

## Additional Resources

- [Official Installation Docs](https://ai.pydantic.dev/install/)
- [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai)
- [API Keys Setup Guide](https://docs.anthropic.com/en/api/getting-started)

---

**Progress Checkpoint**: Mark this complete in `PROGRESS.md` once you've successfully run your first agent!
