from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
programming_languages = ("cpp", "python", "java", "js", "csharp", "c", "kotlin", "go", "rust", "asm", "sql", "dart")
@app.get("/")
async def read_root():
    return HTMLResponse(content=open("static/index.html", "r", encoding="UTF-8").read(), status_code=200)
@app.get("/{lang}", response_class=HTMLResponse)
async def read_root(lang:str):
    if lang in programming_languages:
        return HTMLResponse(content=open(f"static/{lang}.html", "r", encoding="UTF-8").read(), status_code=200)
    else:
        return HTMLResponse(content=open(f"static/404.html", "r", encoding="UTF-8").read(), status_code=200)
