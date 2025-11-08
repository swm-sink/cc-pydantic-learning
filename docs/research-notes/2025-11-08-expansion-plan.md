# Repository Expansion Roadmap

**Date**: 2025-11-08
**Status**: Planning Phase
**Methodology**: Research → Plan → Implement → Verify

## Research Summary

### Official Examples Reviewed
- ✅ bank_support.py - Dependency injection + structured outputs + tools
- ✅ pydantic_model.py - Structured outputs
- ✅ roulette_wheel.py - Tools with dependencies
- ✅ Identified 13+ official examples

### Gaps Identified

1. **Examples** (only 2/30+ planned):
   - ❌ Structured outputs
   - ❌ Tools and function calling
   - ❌ Dependency injection
   - ❌ Error handling
   - ❌ Streaming
   - ❌ Model configuration
   - ❌ Intermediate examples
   - ❌ Advanced multi-agent

2. **Documentation** (20% complete):
   - ❌ Core concepts (structured outputs, tools, deps)
   - ❌ Advanced tutorials
   - ❌ Best practices guide
   - ❌ Testing guide
   - ❌ Troubleshooting

3. **Infrastructure** (0% complete):
   - ❌ Testing framework
   - ❌ requirements.txt
   - ❌ pyproject.toml
   - ❌ Tests for examples
   - ❌ CI/CD setup (future)

4. **Automation** (0% complete):
   - ❌ Hooks configuration
   - ❌ Auto-formatting
   - ❌ Auto-testing
   - ❌ SessionStart hooks

5. **Snippets** (0% complete):
   - ❌ Common patterns library
   - ❌ Reusable components
   - ❌ Quick reference

## Expansion Plan

### Priority 1: Core Examples (Beginner)

1. **structured_outputs.py**
   - Extract city/country from text
   - Product information extraction
   - Customer data parsing

2. **simple_tools.py**
   - Calculator agent with math tools
   - Date/time tools
   - Tool_plain vs tool decorators

3. **basic_error_handling.py**
   - Try/except patterns
   - Validation errors
   - Retry logic

### Priority 2: Concept Documentation

1. **docs/concepts/structured-outputs.md**
   - What are structured outputs?
   - Why use Pydantic models?
   - Examples and patterns

2. **docs/concepts/tools.md**
   - Tool registration
   - Function calling
   - Best practices

3. **docs/concepts/dependency-injection.md**
   - RunContext explained
   - deps_type usage
   - Testing with deps

4. **docs/concepts/error-handling.md**
   - Error types
   - Retry strategies
   - Validation patterns

### Priority 3: Intermediate Examples

1. **dependency_injection.py**
   - Database connections
   - API clients
   - Configuration

2. **multiple_tools.py**
   - Agent with 3-5 tools
   - Tool coordination
   - Sequential execution

3. **model_configuration.py**
   - Different providers
   - Temperature, max_tokens
   - Fallback chains

4. **dynamic_prompts.py**
   - @agent.system_prompt decorator
   - Context-aware instructions
   - Personalization

### Priority 4: Testing Infrastructure

1. **tests/** directory structure
2. **pytest.ini** configuration
3. **test_basic_examples.py**
4. **test_intermediate_examples.py**
5. **requirements-dev.txt**

### Priority 5: Automation (Hooks)

1. **.claude/settings.local.json** (template)
2. **PostToolUse hook** for auto-formatting
3. **SessionStart hook** for environment setup
4. **PreToolUse hook** for safety

### Priority 6: Snippets Library

1. **snippets/agent-patterns.py**
2. **snippets/tool-patterns.py**
3. **snippets/validation-patterns.py**
4. **snippets/testing-patterns.py**

### Priority 7: Additional Documentation

1. **docs/tutorials/building-bank-agent.md**
2. **docs/tutorials/tools-deep-dive.md**
3. **docs/guides/best-practices.md**
4. **docs/guides/testing.md**
5. **docs/guides/troubleshooting.md**

### Priority 8: Advanced Examples

1. **multi_agent_simple.py** - Agent delegation
2. **streaming_example.py** - Streaming responses
3. **rag_simple.py** - Simple RAG pattern
4. **custom_model.py** - Custom model provider

## Implementation Order

### Phase 1 (This Session)
- [ ] Priority 1: Core beginner examples (3 examples)
- [ ] Priority 2: Concept documentation (4 docs)
- [ ] Priority 3: Intermediate examples (4 examples)
- [ ] Priority 4: Testing infrastructure
- [ ] Priority 5: Hooks configuration

### Phase 2 (Next Session)
- [ ] Priority 6: Snippets library
- [ ] Priority 7: Additional documentation
- [ ] Priority 8: Advanced examples

## Success Criteria

### Examples
- ✅ At least 10 complete, runnable examples
- ✅ Cover all core concepts
- ✅ Progressive difficulty
- ✅ Fully commented for learning

### Documentation
- ✅ Every concept explained
- ✅ Learning objectives clear
- ✅ Links to official docs
- ✅ Related examples referenced

### Infrastructure
- ✅ All examples have tests
- ✅ Dependencies documented
- ✅ Hooks configured and working
- ✅ Auto-formatting enabled

### User Experience
- ✅ Can follow learning path start to finish
- ✅ Each example builds on previous
- ✅ Custom commands enhance workflow
- ✅ Repository feels complete and professional

## Estimated Completion

- **Core Examples**: 30 minutes
- **Concept Docs**: 20 minutes
- **Intermediate Examples**: 30 minutes
- **Testing Infrastructure**: 15 minutes
- **Hooks Configuration**: 10 minutes
- **Verification**: 10 minutes
- **Total**: ~2 hours

## Next Steps

1. Move to implementation phase
2. Start with Priority 1 (Core Examples)
3. Add concept documentation
4. Build intermediate examples
5. Set up testing
6. Configure hooks
7. Verify everything works
8. Commit and push

---

**Note**: This plan follows the Research → Plan → Implement → Verify methodology recommended by Claude Code best practices.
