# Tools and Function Calling

Learn how to give your AI agents real capabilities beyond text generation.

## What Are Tools?

Tools are Python functions that your agent can call during a conversation. They extend the agent's capabilities to include:

- **Calculations** - Math, data processing
- **External APIs** - Weather, search, databases
- **File Operations** - Read/write files
- **Custom Logic** - Business rules, validation

## Why Use Tools?

### 1. **Access Real-Time Data**

LLMs have a knowledge cutoff. Tools let them access current information:

```python
@agent.tool_plain
def get_current_weather(city: str) -> dict:
    """Get current weather for a city."""
    return api.fetch_weather(city)
```

### 2. **Perform Actions**

LLMs generate text. Tools let them do things:

```python
@agent.tool_plain
def send_email(to: str, subject: str, body: str) -> bool:
    """Send an email."""
    return email_service.send(to, subject, body)
```

### 3. **Ensure Accuracy**

Don't trust LLMs for calculations:

```python
@agent.tool_plain
def calculate(expression: str) -> float:
    """Accurately calculate mathematical expressions."""
    return math_parser.evaluate(expression)
```

## Two Types of Tools

### @agent.tool_plain

For **stateless** tools that don't need context:

```python
@agent.tool_plain
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b
```

**When to use:**
- Simple calculations
- Pure functions
- No dependencies needed

### @agent.tool

For **stateful** tools that need RunContext:

```python
@agent.tool
async def get_user_data(ctx: RunContext[DatabaseConn]) -> dict:
    """Get data for current user."""
    return await ctx.deps.db.query(user_id=ctx.deps.user_id)
```

**When to use:**
- Need database connections
- Require configuration
- Access user context
- Use dependency injection

## How Tools Work

### 1. Agent Calls Tool

The LLM decides to call a tool based on:
- Your system prompt
- The user's query
- Tool docstrings

### 2. Tool Executes

Your Python function runs:
- Parameters extracted from LLM's request
- Function logic executes
- Returns result

### 3. Result to LLM

Tool result goes back to the LLM:
- LLM sees the result
- Formulates response to user
- May call more tools if needed

## Registering Tools

### Basic Registration

```python
agent = Agent('anthropic:claude-sonnet-4-0')

@agent.tool_plain
def my_tool(param: str) -> str:
    """Tool description for the LLM."""
    return f"Result: {param}"
```

### With Type Hints (Required!)

```python
@agent.tool_plain
def calculate_tax(amount: float, rate: float = 0.08) -> float:
    """Calculate tax on an amount.

    Args:
        amount: Amount to calculate tax on
        rate: Tax rate (default 8%)

    Returns:
        Tax amount
    """
    return amount * rate
```

### With Dependencies

```python
@agent.tool
async def query_database(
    ctx: RunContext[DatabaseConn],
    query: str
) -> list[dict]:
    """Query the database.

    Args:
        ctx: Context with database connection
        query: SQL query to execute
    """
    return await ctx.deps.execute(query)
```

## Tool Best Practices

### 1. Clear Docstrings

The LLM uses your docstring to understand the tool:

```python
@agent.tool_plain
def search_products(
    keyword: str,
    category: str | None = None,
    max_results: int = 10
) -> list[dict]:
    """Search for products in the catalog.

    Use this when the user wants to find products.

    Args:
        keyword: Search term (e.g., "laptop", "phone")
        category: Filter by category (e.g., "electronics")
        max_results: Maximum number of results to return

    Returns:
        List of products with name, price, and description
    """
    ...
```

### 2. Type Hints Everywhere

```python
# ❌ No type hints
def bad_tool(x, y):
    return x + y

# ✅ Proper type hints
def good_tool(x: int, y: int) -> int:
    return x + y
```

### 3. Handle Errors

```python
@agent.tool_plain
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
```

### 4. Return JSON-Serializable Data

```python
# ✅ Good returns
return "string"
return 42
return [1, 2, 3]
return {"key": "value"}

# ❌ Bad returns
return some_object  # Not serializable
return open('file.txt')  # File handle
```

### 5. Keep Tools Focused

```python
# ❌ Tool does too much
@agent.tool_plain
def do_everything(action, params): ...

# ✅ Separate, focused tools
@agent.tool_plain
def get_weather(city): ...

@agent.tool_plain
def send_email(to, subject): ...
```

## Advanced Patterns

### Sequential Tools

Tools are usually concurrent, but you can make them sequential:

```python
@agent.tool(sequential=True)
async def must_run_in_order(ctx: RunContext) -> str:
    """This tool must run sequentially."""
    ...
```

### Tool with Approval

Require human approval before executing:

```python
@agent.tool(approval_required=True)
async def delete_user(ctx: RunContext, user_id: int) -> bool:
    """Delete a user (requires approval)."""
    ...
```

### Dynamic Tools

Register tools dynamically:

```python
def create_agent_with_tools(tools: list):
    agent = Agent('anthropic:claude-sonnet-4-0')

    for tool_func in tools:
        agent.tool_plain(tool_func)

    return agent
```

## Common Use Cases

### 1. API Integration

```python
@agent.tool_plain
def fetch_weather(city: str) -> dict:
    """Get weather from API."""
    response = requests.get(f"api.weather.com/city={city}")
    return response.json()
```

### 2. Database Queries

```python
@agent.tool
async def get_customer(ctx: RunContext[DB], id: int) -> dict:
    """Fetch customer from database."""
    return await ctx.deps.query("SELECT * FROM customers WHERE id=?", id)
```

### 3. Calculations

```python
@agent.tool_plain
def compound_interest(
    principal: float,
    rate: float,
    years: int
) -> float:
    """Calculate compound interest."""
    return principal * (1 + rate) ** years
```

### 4. File Operations

```python
@agent.tool_plain
def read_file(path: str) -> str:
    """Read contents of a file."""
    with open(path) as f:
        return f.read()
```

## Tool Debugging

### See Tool Calls

```python
result = agent.run_sync('Calculate 5 + 3')
for message in result.messages():
    print(message)
```

### Log Tool Execution

```python
@agent.tool_plain
def my_tool(param: str) -> str:
    print(f"Tool called with: {param}")
    result = do_work(param)
    print(f"Tool returning: {result}")
    return result
```

## Examples to Study

- `examples/basic/simple_tools.py` - Basic tool usage
- `examples/intermediate/multiple_tools.py` - Complex tool orchestration
- `pydantic-ai/examples/roulette_wheel.py` - Official example

## Related Concepts

- [Dependency Injection](dependency-injection.md) - Pass resources to tools
- [Structured Outputs](structured-outputs.md) - Get typed results
- [Error Handling](error-handling.md) - Handle tool failures

## Further Reading

- [Official Docs: Tools](https://ai.pydantic.dev/tools/)
- [API Reference](https://ai.pydantic.dev/api/tools/)
- [Advanced Tool Features](https://ai.pydantic.dev/tools-advanced/)

---

**Next Steps**: Build an agent with multiple tools in `examples/intermediate/multiple_tools.py`!
