from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(max_length=10)
    description: str | None = None
    price: float
    in_stock: bool = True

if __name__ == "__main__":
    new_item = Item(price=10.0, name="my_item")
    print(new_item.model_dump_json())
