from products.models import Product
from faker import Faker
from faker.providers import python

fake = Faker()
fake.add_provider(python)

for _ in range(1500):
    q = Product(name=fake.pystr(max_chars=10), price=fake.pyint(max_value=1500), stocks=fake.pyint(max_value=20))
    print(q.save)