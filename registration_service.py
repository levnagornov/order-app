from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")
registered_users = []

@app.get("/", response_class=HTMLResponse)
async def get_registration_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register_user(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    registered_users.append(
        {"name": name, "email": email, "password": password}
    )
    return templates.TemplateResponse("confirmation.html", {"request": request, "name": name})
    