from fastapi import FastAPI
from google.cloud import spanner

app = FastAPI()

# Connect to Cloud Spanner
spanner_client = spanner.Client(project="testingcloud001")
instance = spanner_client.instance("demo-instance")
database = instance.database("demo-db")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on App Engine!"}



@app.get("/products")
def list_products():
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql("SELECT * FROM Products")
        return [dict(row.items()) for row in results]

@app.post("/products")
def add_product(product: dict):
    with database.batch() as batch:
        batch.insert(
            table="Products",
            columns=("ProductId", "Name", "Category", "Price", "InStock", "LastUpdated"),
            values=[(
                product["ProductId"],
                product["Name"],
                product["Category"],
                product["Price"],
                product["InStock"],
                spanner.COMMIT_TIMESTAMP
            )]
        )
    return {"status": "added"}

