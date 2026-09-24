from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена должна быть больше 0")
    tags: list[str] = []
    market: Market


product_data = {
    'name': 'iPhone',
    'price': 499.99,
    'tags': ['electronics', 'smartphone'],
    'market': {
        'id': 23,
        'name': 'Phones Store'
    }
}

product = Product(**product_data)
print(product.market)
print(product_data['market']['name'])

new_product = Product(
    name='Android',
    price=300.00,
    tags=['electronics', 'smartphone'],
    market=Market(id=200, name='Amazon')
)
print('new_product:', new_product)
