from sqlalchemy.orm import Session
from bs4 import BeautifulSoup, NavigableString
import requests

from users.authentication import get_current_active_user
from . import schemas, models


async def create_product_link(
    product_link: schemas.ProductCreate,
    db: Session, 
    current_user: get_current_active_user
):
    """
    Choose your wish product from this website:
        https://primashop.ir/
    """
    product_db = models.Product(link=product_link.link, user_id=current_user.id)
    db.add(product_db)
    db.commit()
    db.refresh(product_db)

    url = product_db.link
    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")

    title = content.find("h1", class_="product-title")
    title = title.get_text(strip=True) if title else None
    unit_price = content.find("span", attrs={"id": "dc-price-wrapper"})
    unit_price = unit_price.get_text(strip=True) if unit_price else None
    discount = content.find("div", class_="discount-item")
    discount = discount.get_text(strip=True) if discount else None
    total_price = content.find("span", attrs={"id": "dc-special-wrapper"})
    total_price = total_price.get_text(strip=True) if total_price else None
    score = content.find("div", class_="product-engagement-rating")
    score = score.get_text(strip=True) if score else None

    product = db.query(models.Product).filter(models.Product.id == product_db.id)
    product.update(
        {
            models.Product.title: title,
            models.Product.unit_price: unit_price,
            models.Product.discount: discount,
            models.Product.total_price: total_price,
            models.Product.score: score
        }
    )
    db.commit()

    return product_db


async def get_all_products(skip: int, limit: int, db: Session):
    return db.query(models.Product).offset(skip).limit(limit).all()
