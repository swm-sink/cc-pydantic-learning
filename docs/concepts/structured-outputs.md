# Structured Outputs

Learn how to get validated, typed data from your AI agents instead of plain text.

## What Are Structured Outputs?

Structured outputs allow you to define exactly what shape of data you want from an agent. Instead of getting a string that you have to parse, you get a validated Python object.

### Without Structured Outputs

```python
agent = Agent('anthropic:claude-sonnet-4-0')
result = agent.run_sync('Extract city and country from: Paris, France')
# result.data = "The city is Paris and the country is France."
# Now you have to parse this string 😞
```

### With Structured Outputs

```python
class Location(BaseModel):
    city: str
    country: str

agent = Agent('anthropic:claude-sonnet-4-0', output_type=Location)
result = agent.run_sync('Extract city and country from: Paris, France')
# result.output = Location(city='Paris', country='France')
# Validated, typed object ready to use! 😊
```

## Why Use Structured Outputs?

### 1. **Type Safety**

Your IDE knows the exact structure and can autocomplete:

```python
location = result.output
print(location.city)  # IDE autocompletes this!
print(location.country)  # And this!
```

### 2. **Automatic Validation**

Pydantic validates the data:

```python
class PersonInfo(BaseModel):
    name: str
    age: int = Field(ge=0, le=150)  # Age must be 0-150

# If the LLM returns invalid data, it automatically retries!
```

### 3. **No Manual Parsing**

No more fragile string parsing:

```python
# ❌ Before: fragile and error-prone
text = result.data
city = text.split("city is ")[1].split(" and")[0]

# ✅ After: clean and reliable
city = result.output.city
```

### 4. **Self-Documenting**

The Pydantic model documents your data structure:

```python
class UserProfile(BaseModel):
    """User profile information."""

    name: str = Field(description="Full name")
    email: str = Field(description="Email address")
    age: int | None = Field(default=None, description="Age in years")
```

## How It Works

### Step 1: Define Your Model

```python
from pydantic import BaseModel, Field

class ProductInfo(BaseModel):
    name: str
    price: float
    in_stock: bool
    category: str
```

### Step 2: Create Agent with output_type

```python
agent = Agent(
    'anthropic:claude-sonnet-4-0',
    output_type=ProductInfo,  # Tell agent what to return
    system_prompt='Extract product information.'
)
```

### Step 3: Get Validated Output

```python
result = agent.run_sync('MacBook Pro for $2,499, in stock, electronics')
product: ProductInfo = result.output  # Typed and validated!
```

## Common Patterns

### Optional Fields

```python
class PersonInfo(BaseModel):
    name: str  # Required
    age: int | None = None  # Optional
    email: str | None = None  # Optional
```

### Lists and Nested Data

```python
class Article(BaseModel):
    title: str
    authors: list[str]  # List of strings
    tags: list[str] = Field(default_factory=list)

class BlogPost(BaseModel):
    article: Article  # Nested model
    views: int
```

### Validation Rules

```python
class UserData(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=13, le=120)  # 13-120
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
```

### Enums for Fixed Choices

```python
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(BaseModel):
    title: str
    priority: Priority  # Must be one of the enum values
```

## Under the Hood

Pydantic AI uses the model's "tool calling" capability to return structured data:

1. Converts your Pydantic model to JSON Schema
2. Tells the LLM "return data matching this schema"
3. LLM returns JSON matching the schema
4. Pydantic validates and creates your Python object
5. If validation fails, agent automatically retries

## Best Practices

### 1. Use Descriptive Field Names

```python
# ❌ Vague
class Data(BaseModel):
    val1: str
    val2: int

# ✅ Clear
class UserAccount(BaseModel):
    email_address: str
    age_in_years: int
```

### 2. Add Field Descriptions

```python
class Product(BaseModel):
    name: str = Field(description="Product name or title")
    price: float = Field(description="Price in USD")
```

### 3. Use Appropriate Types

```python
class Event(BaseModel):
    date: str  # Could be datetime if you need it
    attendees: list[str]  # List, not str
    is_virtual: bool  # Bool, not str
```

### 4. Provide Defaults Where Appropriate

```python
class Config(BaseModel):
    debug: bool = False  # Sensible default
    max_retries: int = 3  # Default value
    tags: list[str] = Field(default_factory=list)  # Empty list default
```

### 5. Keep Models Simple

```python
# ✅ Simple and focused
class Address(BaseModel):
    street: str
    city: str
    country: str

# ❌ Too complex for extraction
class PersonWithEverything(BaseModel):
    # 20 fields...
```

## Common Use Cases

### 1. Data Extraction

Extract structured data from unstructured text:

```python
class Contact(BaseModel):
    name: str
    email: str
    phone: str | None = None
```

### 2. Classification

Classify content into categories:

```python
class Classification(BaseModel):
    category: str
    confidence: float = Field(ge=0.0, le=1.0)
    reasoning: str
```

### 3. Sentiment Analysis

```python
class Sentiment(BaseModel):
    sentiment: str  # "positive", "negative", "neutral"
    score: float = Field(ge=-1.0, le=1.0)
```

### 4. Entity Recognition

```python
class Entities(BaseModel):
    people: list[str]
    organizations: list[str]
    locations: list[str]
```

## Troubleshooting

### Validation Fails Repeatedly

- Make sure your model isn't too complex
- Add clearer field descriptions
- Provide examples in the system prompt

### Wrong Data Types

- LLM returns string instead of int/bool
- Add validation rules with Field()
- Be explicit in your system prompt

### Missing Optional Fields

- That's expected! Use `| None` and provide defaults
- Check if field is None before using

## Examples to Study

- `examples/basic/structured_outputs.py` - Complete examples
- `pydantic-ai/examples/pydantic_model.py` - Official example
- `pydantic-ai/examples/bank_support.py` - Real-world usage

## Related Concepts

- [Tools](tools.md) - Give agents capabilities
- [Dependency Injection](dependency-injection.md) - Pass resources to agents
- [Error Handling](error-handling.md) - Handle validation failures

## Further Reading

- [Official Docs: Output](https://ai.pydantic.dev/output/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [API Reference](https://ai.pydantic.dev/api/agent/)

---

**Next Steps**: Try the examples in `examples/basic/structured_outputs.py` and experiment with your own models!
