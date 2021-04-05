from tortoise.models import Model
from tortoise import fields, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

# Tortoise ORM Model
class TestModel(Model):
    test = fields.IntField(null=False, description=f"Test value")
    ts = fields.IntField(null=False, description=f"Epoch time")
    ts3 = fields.IntField(null=True, description=f"Epoch time")

# Pydantic schema
TestSchema = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}Schema")
TestSchemaCreate = pydantic_model_creator(TestModel, name=f"{TestModel.__name__}SchemaCreate", exclude_readonly=True)