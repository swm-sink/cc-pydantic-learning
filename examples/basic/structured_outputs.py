"""
Structured Outputs with Pydantic Models

Learning objectives:
- Understand structured outputs vs plain text
- Learn to define output models with Pydantic
- See how automatic validation works
- Extract structured data from natural language

Structured outputs ensure the agent returns data in a predictable,
validated format that you can use programmatically.
"""

from pydantic import BaseModel, Field
from pydantic_ai import Agent


# Define the structure we want the agent to return
class CityInfo(BaseModel):
    """Information about a city."""

    city: str = Field(description="The name of the city")
    country: str = Field(description="The country the city is in")
    population: int | None = Field(
        default=None, description="Approximate population"
    )
    famous_for: str = Field(description="What the city is famous for")


# Create agent with structured output
city_agent = Agent(
    'anthropic:claude-sonnet-4-0',
    output_type=CityInfo,  # This tells the agent to return CityInfo
    system_prompt='Extract city information from the user query.',
)


def basic_example():
    """Extract city information from text."""
    print("=== Basic Structured Output ===")

    result = city_agent.run_sync('Tell me about the windy city in the US.')

    # result.output is now a validated CityInfo object, not a string!
    city_info = result.output

    print(f"City: {city_info.city}")
    print(f"Country: {city_info.country}")
    print(f"Famous for: {city_info.famous_for}")
    print(f"\nFull object: {city_info}")
    print(f"Type: {type(city_info)}")


class Product(BaseModel):
    """Product information extracted from text."""

    name: str
    price: float
    currency: str = "USD"
    in_stock: bool
    category: str


def product_example():
    """Extract product info from a description."""
    print("\n=== Product Information Extraction ===")

    product_agent = Agent(
        'anthropic:claude-sonnet-4-0',
        output_type=Product,
        system_prompt='Extract product information from the description.',
    )

    description = """
    We have a new MacBook Pro available for $2,499.
    It's currently in stock and part of our electronics category.
    """

    result = product_agent.run_sync(description)
    product = result.output

    print(f"Product: {product.name}")
    print(f"Price: {product.currency} {product.price:.2f}")
    print(f"In Stock: {product.in_stock}")
    print(f"Category: {product.category}")


class UserData(BaseModel):
    """Customer information."""

    full_name: str
    email: str
    age: int | None = None
    interests: list[str] = Field(default_factory=list)


def complex_example():
    """Extract complex structured data."""
    print("\n=== Complex Data Extraction ===")

    user_agent = Agent(
        'anthropic:claude-sonnet-4-0',
        output_type=UserData,
        system_prompt='Extract user information from the text.',
    )

    text = """
    Hi, I'm Sarah Johnson (sarah.j@email.com). I'm 28 years old.
    I'm interested in hiking, photography, and cooking.
    """

    result = user_agent.run_sync(text)
    user = result.output

    print(f"Name: {user.full_name}")
    print(f"Email: {user.email}")
    print(f"Age: {user.age}")
    print(f"Interests: {', '.join(user.interests)}")


if __name__ == '__main__':
    # Run all examples
    basic_example()
    product_example()
    complex_example()

    # Key takeaways:
    print("\n=== Key Takeaways ===")
    print("1. Define structure with Pydantic BaseModel")
    print("2. Set output_type when creating agent")
    print("3. result.output is a validated Python object")
    print("4. Automatic validation catches errors")
    print("5. Much better than parsing text manually!")
