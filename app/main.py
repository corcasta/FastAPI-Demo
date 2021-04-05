# Script example: https://fastapi-crudrouter.awtkns.com/backends/tortoise/
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi_crudrouter.core.tortoise import TortoiseCRUDRouter
from tortoise.contrib.fastapi import register_tortoise
from models import TestModel, TestSchema, TestSchemaCreate
from settings import TORTOISE_ORM


app = FastAPI()
register_tortoise(
    app, 
    config=TORTOISE_ORM
    # db_url='postgres://postgres:admin@localhost:5432/test2',
    # modules={'models': ['main']},
    # generate_schemas=True,
    # add_exception_handlers=True
)

# Make your FastAPI Router from your Pydantic schema and Tortoise Model
router = TortoiseCRUDRouter(
    schema=TestSchema,
    create_schema=TestSchemaCreate,
    db_model=TestModel,
    prefix="test"
)

# Add it to your app
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")