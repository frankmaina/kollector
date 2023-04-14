from fastapi import FastAPI
from kollector.api.controllers import form_controller, form_schema_controller, field_controller

app = FastAPI(title="Kollector API", version="0.0.1")
app.include_router(form_schema_controller.router)
app.include_router(field_controller.router)
