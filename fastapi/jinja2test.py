from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name='static')

templates = Jinja2Templates(directory='templates')

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.get('/item/{id}', response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    print(request)
    return templates.TemplateResponse("item.html", {"request": request, "id": id})