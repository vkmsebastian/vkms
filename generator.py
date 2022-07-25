import django
django.setup()
from products.models import Product
from faker import Faker
from faker.providers import python

fake = Faker()
fake.add_provider(python)

for _ in range(1500):