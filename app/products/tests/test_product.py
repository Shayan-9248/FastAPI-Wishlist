from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Factory

from products.models import Product
from users.models import User
from .. import models
from app.main import app
import database

client = TestClient(app)


def test_get_products_returns_200():
    faker = Factory.create()
    fake_product = Product(link=faker.name())
    session = Session(bind=database.engine)
    session.add(fake_product)
    session.commit()
    session.refresh(fake_product)

    response = client.get(f"/products/all")
    assert response.status_code == 200


def test_get_unpurchased_products_returns_200():
    faker = Factory.create()
    fake_product = Product(link=faker.name())
    session = Session(bind=database.engine)
    session.add(fake_product)
    session.commit()
    session.refresh(fake_product)

    response = client.get(f"/products/unpurchased-list")
    assert response.status_code == 200


def test_create_product_returns_201():
    faker = Factory.create()
    fake_user = User(email=faker.email(), hashed_password=faker.name())
    session = Session(bind=database.engine)
    session.add(fake_user)
    session.commit()
    session.refresh(fake_user)

    auth = client.post(
        "/sign-in",
        data={"username": fake_user.email, "password": fake_user.hashed_password},
    )

    access_token = auth.json().get("access_token")

    response = client.post(
        "/products/create-link",
        json={"link": "https://google.com"},
        headers={"Authorization": f"bearer {access_token}"},
    )
    assert response.status_code == 201
