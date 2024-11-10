from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import feedparser

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_news(request: Request):
    # Placeholder news articles to display
    news_feed = []
    return templates.TemplateResponse("index.html", {"request": request, "news_feed": news_feed})
