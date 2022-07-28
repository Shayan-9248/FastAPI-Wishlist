from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Factory

from products.models import Product
from users.models import User
from .. import models
from app.main import app
import database

client = TestClient(app)


def test_get_comments_returns_200():
    faker = Factory.create()
    fake_product = Product(link=faker.name())
    session = Session(bind=database.engine)
    session.add(fake_product)
    session.commit()
    session.refresh(fake_product)

    response = client.get(f"/comments/{fake_product.id}")
    assert response.status_code == 200


def test_create_comment_returns_201():
    faker = Factory.create()
    fake_product = Product(link=faker.name())
    fake_user = User(email=faker.email(), hashed_password=faker.name())
    session = Session(bind=database.engine)
    session.add(fake_product)
    session.add(fake_user)
    session.commit()
    session.refresh(fake_product)

    auth = client.post(
        "/sign-in",
        data={"username": fake_user.email, "password": fake_user.hashed_password},
    )

    access_token = auth.json().get("access_token")

    response = client.post(
        "/comments/create",
        json={"product_id": fake_product.id, "content": "comment 1"},
        headers={"Authorization": f"bearer {access_token}"},
    )
    assert response.status_code == 201


def test_update_comment_returns_200():
    faker = Factory.create()
    fake_product = Product(link=faker.name())
    fake_comment = models.Comment(content=faker.name(), product_id=fake_product.id)
    fake_user = User(email=faker.email(), hashed_password=faker.name())
    session = Session(bind=database.engine)
    session.add(fake_user)
    session.add(fake_product)
    session.add(fake_comment)
    session.commit()
    session.refresh(fake_user)

    auth = client.post(
        "/sign-in",
        data={"username": fake_user.email, "password": fake_user.hashed_password},
    )

    access_token = auth.json().get("access_token")

    response = client.put(
        f"/comments/update/{fake_comment.id}",
        json={"content": "test"},
        headers={"Authorization": f"bearer {access_token}"},
    )

    assert response.status_code == 200


def test_delete_comment_returns_204():
    faker = Factory.create()
    fake_product = Product(link=faker.name())
    fake_comment = models.Comment(content=faker.name(), product_id=fake_product.id)
    fake_user = User(email=faker.email(), hashed_password=faker.name())
    session = Session(bind=database.engine)
    session.add(fake_user)
    session.add(fake_product)
    session.add(fake_comment)
    session.commit()
    session.refresh(fake_user)

    auth = client.post(
        "/sign-in",
        data={"username": fake_user.email, "password": fake_user.hashed_password},
    )

    access_token = auth.json().get("access_token")

    response = client.delete(
        f"/comments/delete/{fake_comment.id}",
        json={"content": "test"},
        headers={"Authorization": f"bearer {access_token}"},
    )

    assert response.status_code == 204
