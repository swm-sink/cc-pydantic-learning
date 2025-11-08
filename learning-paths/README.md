# Learning Paths

Structured progressions for mastering Pydantic AI.

## Overview

Each learning path is designed to build on previous knowledge, following adult learning principles and progressive disclosure of complexity.

## Available Paths

### 1. Beginner Path (1-2 weeks)

**Goal**: Understand core concepts and create simple agents

**Prerequisites**: Basic Python knowledge, understanding of async/await

**Topics**:
- Installation and setup
- Basic agent creation
- System prompts and instructions
- Structured outputs with Pydantic models
- Simple tool registration
- Running agents (sync and async)

**Learning Resources**:
- `docs/getting-started/01-installation.md`
- `docs/getting-started/02-first-agent.md`
- `docs/tutorials/basic-agent-tutorial.md`
- `examples/basic/`

**Hands-on Projects**:
1. Personal assistant agent
2. Data extraction agent
3. Simple calculator agent with tools

**Assessment**: Can you create an agent that uses structured outputs and one custom tool?

---

### 2. Intermediate Path (2-3 weeks)

**Goal**: Build production-ready agents with advanced features

**Prerequisites**: Completed beginner path

**Topics**:
- Dependency injection with RunContext
- Advanced tool patterns
- Model configuration and settings
- Dynamic system prompts
- Error handling and validation
- Multiple model providers
- Testing strategies

**Learning Resources**:
- `docs/concepts/dependency-injection.md`
- `docs/concepts/tools-advanced.md`
- `docs/tutorials/bank-support-agent.md`
- `examples/intermediate/`

**Hands-on Projects**:
1. Customer support agent with database access
2. Research assistant with web search
3. Code analysis agent

**Assessment**: Can you build an agent that uses dependency injection, multiple tools, and handles errors gracefully?

---

### 3. Advanced Path (3-4 weeks)

**Goal**: Master complex patterns and production deployment

**Prerequisites**: Completed intermediate path

**Topics**:
- Multi-agent systems and orchestration
- Agent delegation and hand-off
- Graph-based workflows
- Custom model providers
- Streaming responses
- Production deployment
- Observability with Logfire
- Performance optimization

**Learning Resources**:
- `docs/concepts/multi-agent.md`
- `docs/concepts/production.md`
- `docs/tutorials/multi-agent-workflow.md`
- `examples/advanced/`

**Hands-on Projects**:
1. Multi-agent research system
2. Production API with agents
3. Custom model integration

**Assessment**: Can you design and implement a multi-agent system for a real-world use case?

---

## Learning Methodology

### Research → Plan → Code Pattern

For each topic:

1. **Research**: Read official docs, study examples
2. **Plan**: Write pseudocode or outline approach
3. **Code**: Implement with type safety and tests
4. **Reflect**: Document learnings and insights

### Spaced Repetition

- Revisit core concepts regularly
- Build increasingly complex examples
- Refactor early examples with new knowledge

### Active Learning

- Type out all examples (don't just read)
- Modify examples to test understanding
- Create variations and extensions
- Ask "what if?" questions

## Progress Tracking

Update `PROGRESS.md` as you complete each section.

## Getting Help

- Check official docs: https://ai.pydantic.dev/
- Review examples in `pydantic-ai/examples/`
- Use Claude Code's `/pydantic-help` command
- Document questions in research notes

## Customizing Your Path

Feel free to:
- Skip topics you're already familiar with
- Spend more time on challenging concepts
- Create additional projects that interest you
- Adjust the timeline to your schedule

The paths are guides, not rigid requirements. Learn at your own pace!
