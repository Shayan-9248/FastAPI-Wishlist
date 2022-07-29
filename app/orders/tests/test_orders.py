from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Factory

from users.models import User
from carts.models import Cart, CartItem
from products.models import Product
from .. import models
from app.main import app
import database

client = TestClient(app)


def test_get_orders_returns_200():
    faker = Factory.create()
    fake_user = User(email=faker.email(), hashed_password=faker.name())
    fake_order = models.Order(user_id=fake_user.id, status="pending")
    session = Session(bind=database.engine)
    session.add(fake_user)
    session.add(fake_order)
    session.commit()

    auth = client.post(
        "/sign-in",
        data={"username": fake_user.email, "password": fake_user.hashed_password},
    )
    access_token = auth.json().get("access_token")

    response = client.get(
        "/orders", headers={"Authorization": f"bearer {access_token}"}
    )
    assert response.status_code == 200
