from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/sales-page", response_class=HTMLResponse)
async def sales_page(request: Request):
    sales_data = {
        "USA": {
            "units_sold": 1200,
            "total_revenue": 23000,
            "best_selling_product": {
                "name": "Widget Pro",
                "units_sold": 500
            }
        },
        "Canada": {
            "units_sold": 900,
            "total_revenue": 15000,
            "best_selling_product": {
                "name": "Gizmo Max",
                "units_sold": 300
            }
        },
        "France": {
            "units_sold": 750,
            "total_revenue": 11000,
            "best_selling_product": {
                "name": "Widget Pro",
                "units_sold": 350
            }
        },
        "Germany": {
            "units_sold": 650,
            "total_revenue": 13500,
            "best_selling_product": {
                "name": "Super Widget",
                "units_sold": 250
            }
        },
        "Japan": {
            "units_sold": 1200,
            "total_revenue": 25000,
            "best_selling_product": {
                "name": "Gizmo Max",
                "units_sold": 450
            }
        },
        "Sweden": {
            "units_sold": 1200,
            "total_revenue": 25000,
            "best_selling_product": {
                "name": "Iphone 15 Pro Max",
                "units_sold": 450
            }

        }
    }

    if request.headers.get("HX-Request"):
        template_name = "partials/_sales_widget.html"
    else:
        print('not hx-request')
        template_name = "sales_widget.html"

    return templates.TemplateResponse(template_name, {"request": request, "sales_data": sales_data})
