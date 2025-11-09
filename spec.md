# Pydantic AI Learning Repository - Specification

**Branch**: `main` (learning repository)
**Created**: 2025-11-08
**Status**: Active Development
**Version**: v1.12.0 (aligned with Pydantic AI)

---

## Overview

A comprehensive, production-ready learning repository for mastering Pydantic AI through progressive, self-paced education. This repository serves as the primary resource for developers learning to build GenAI agents with type safety, validation, and production-grade patterns.

---

## User Scenarios & Testing

### US-1: Beginner Developer Learning Pydantic AI (Priority: P1)

**As a** Python developer new to AI agents
**I want** a guided, hands-on learning path with interactive notebooks
**So that** I can build my first Pydantic AI agent in under 30 minutes

**Acceptance Scenarios**:
- **Given** I have Python 3.10+ installed
  **When** I open `notebooks/01-getting-started/01-installation.ipynb`
  **Then** I can verify my environment, install dependencies, and run my first agent

- **Given** I complete the beginner path (5 examples + 3 notebooks)
  **When** I test my understanding
  **Then** I can create agents with structured outputs and simple tools independently

- **Given** I encounter errors during setup
  **When** I reference the troubleshooting sections
  **Then** I can resolve 90% of common issues without external help

**Priority Justification**: Core user persona; enables immediate value and retention.

---

### US-2: Intermediate Developer Building Production Agents (Priority: P1)

**As a** developer building production AI applications
**I want** advanced patterns for dependency injection, error handling, and testing
**So that** I can deploy reliable agents with proper observability

**Acceptance Scenarios**:
- **Given** I complete the intermediate path
  **When** I implement dependency injection
  **Then** I can create testable agents with mock dependencies

- **Given** I need to monitor agent behavior
  **When** I integrate Logfire observability
  **Then** I can trace all LLM calls, tool executions, and errors in real-time

- **Given** I deploy to production
  **When** I use Pydantic Evals for testing
  **Then** I have automated test coverage >80% for agent behaviors

**Priority Justification**: Bridges learning to production use; critical for real-world applications.

---

### US-3: Advanced Developer Architecting Multi-Agent Systems (Priority: P2)

**As a** senior developer or architect
**I want** proven patterns for multi-agent orchestration and long-running workflows
**So that** I can build complex AI systems that scale and recover from failures

**Acceptance Scenarios**:
- **Given** I study the multi-agent examples
  **When** I implement orchestrator-worker pattern
  **Then** I achieve 90%+ performance improvement over single-agent baseline

- **Given** I need fault-tolerant workflows
  **When** I use durable execution with Temporal
  **Then** My agents recover automatically from crashes and API failures

- **Given** I need human oversight
  **When** I implement human-in-the-loop approval
  **Then** Sensitive operations require explicit approval before execution

**Priority Justification**: Enables enterprise-grade systems; differentiator from basic tutorials.

---

### Edge Cases

- **Offline Learning**: Documentation and examples work without API keys (mock mode)
- **Multiple LLM Providers**: Examples demonstrate switching between Anthropic, OpenAI, Gemini
- **Version Compatibility**: Clear documentation when features require specific versions
- **Resource Constraints**: Examples include cost tracking and token optimization strategies

---

## Requirements

### Functional Requirements

**FR-001: Interactive Learning Interface**
Repository MUST provide Jupyter notebooks as the primary learning interface with:
- Executable code cells with real examples
- Progressive difficulty (beginner → expert)
- Inline explanations and visualizations
- Optional exercises for practice

**FR-002: Comprehensive Code Examples**
Repository MUST include verified, working examples covering:
- Basic: Agent creation, structured outputs, simple tools (5+ examples)
- Intermediate: Dependency injection, multiple tools, model configuration (3+ examples)
- Advanced: Multi-agent systems, streaming, human-in-loop, durable execution (6+ examples)
- All examples MUST run successfully with current Pydantic AI version

**FR-003: Documentation Coverage**
Repository MUST provide documentation for:
- Getting started guides (installation, first agent)
- Core concepts (tools, dependencies, structured outputs, streaming)
- Production patterns (testing, observability, deployment)
- Anthropic Claude best practices (Sonnet 4.5 optimizations)

**FR-004: Testing Infrastructure**
Repository MUST include:
- Pytest test suite with >70% code coverage
- Pydantic Evals integration examples
- Mock dependencies for offline testing
- CI/CD friendly test execution

**FR-005: Production-Ready Patterns**
Repository MUST demonstrate:
- Logfire observability integration
- Error handling and retry strategies
- Human-in-the-loop approval workflows
- Durable execution for long-running tasks
- MCP (Model Context Protocol) integration

**FR-006: Verified Accuracy**
Repository MUST ensure:
- All version numbers verified against PyPI
- All features verified against official source code
- Zero hallucinations in claims about capabilities
- Regular verification against upstream updates

**FR-007: Claude Code Integration**
Repository MUST provide:
- Custom slash commands for common tasks
- Specialized learning assistant agents
- Project context in CLAUDE.md
- Automated hooks for code quality

**FR-008: Progressive Learning Paths**
Repository MUST define structured paths:
- Beginner Path (1-2 weeks, 100% coverage)
- Intermediate Path (2-3 weeks, 75%+ coverage)
- Advanced Path (3-4 weeks, 60%+ coverage)
- Expert Path (ongoing, reference materials)

---

### Key Entities

**Agent**: Pydantic AI Agent instance with model, instructions, tools, and dependencies
**RunResult**: Result object containing output, usage, messages, and metadata
**Tool**: Function decorated with @agent.tool or @agent.tool_plain for LLM to call
**Dependencies**: Type-safe context passed via RunContext for state management
**Evaluation**: Test case with inputs, expected outputs, and custom evaluators
**Notebook**: Jupyter notebook (.ipynb) with markdown cells and executable code
**Example**: Standalone Python script demonstrating specific pattern or feature

---

## Success Criteria

**SC-001: Learning Effectiveness**
- 90% of beginner path users can create a working agent within 30 minutes
- 80% of intermediate path completers can build production-ready agents with tests
- Measured via completion rates and community feedback

**SC-002: Content Quality**
- Zero hallucinations in technical claims (verified via source code inspection)
- All code examples run successfully on Python 3.10-3.13
- Notebook execution success rate >95% on clean environment

**SC-003: Documentation Coverage**
- 100% of beginner path features documented
- 80% of intermediate path features documented
- 60% of advanced path features documented
- All documentation cross-referenced with official Pydantic AI docs

**SC-004: Community Adoption**
- Repository serves as reference for 100+ developers learning Pydantic AI
- Claude Code integration demonstrates best practices for AI-assisted learning
- Contributions from community expand example coverage

**SC-005: Maintenance & Currency**
- Repository updated within 2 weeks of major Pydantic AI releases
- All examples verified compatible with latest stable version
- Deprecated features clearly marked with migration paths

---

## Out of Scope

**Not Included in This Repository**:
- Production deployment infrastructure (Kubernetes, Docker, etc.)
- LLM fine-tuning tutorials (focus on agent frameworks, not model training)
- Non-Python language bindings
- Enterprise authentication/authorization patterns
- Cost optimization for specific cloud providers
- Comparison with other agent frameworks (LangChain, AutoGen, etc.)
- GUI/web interface for running examples (CLI and notebook focused)

**Future Considerations**:
- Video tutorials and screencasts (Phase 7+)
- Interactive quizzes and assessments
- Community showcase of real-world applications
- Integration with learning management systems

---

## References

- **Pydantic AI Official Docs**: https://ai.pydantic.dev/
- **Anthropic Best Practices**: https://docs.claude.com/
- **GitHub Spec Kit**: https://github.com/github/spec-kit
- **Verification Report**: docs/research-notes/2025-11-08-verification-report.md
- **Learning Plan**: docs/research-notes/2025-11-08-updated-learning-plan.md

---

**Last Updated**: 2025-11-08
**Next Review**: Upon Pydantic AI v1.13.0 release or major Anthropic model update
