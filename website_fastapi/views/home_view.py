
from pathlib import Path

from fastapi.requests import Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

BASE_PATH = Path(__file__).parent
project_root = BASE_PATH.parent
templates_path = project_root / 'templates'

templates = Jinja2Templates(directory=templates_path)


@router.get('/', name='index')
async def index(request: Request):
    return templates.TemplateResponse("home/index.html", context={"request": request})


@router.get('/contact', name='contact')
async def contact(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/contact.html", context=context)


@router.get('/about', name='about')
async def about(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/about.html", context=context)


@router.get('/pricing', name='pricing')
async def pricing(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/pricing.html", context=context)


@router.get('/faq', name='faq')
async def faq(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/faq.html", context=context)


@router.get('/portfolio', name='portfolio')
async def portfolio(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/portfolio.html", context=context)


@router.get('/portfolio_item', name='portfolio_item')
async def portfolio_item(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/portfolio_item.html", context=context)


@router.get('/blog_post', name='blog_post')
async def blog_post(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/blog_post.html", context=context)


@router.get('/blog_home', name='blog_home')
async def blog_home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home/blog_home.html", context=context)
