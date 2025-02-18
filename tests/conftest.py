from fastapi.testclient import TestClient
import pytest
from app.main import app
# from app.routers import 
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db, Base
from app import models
from alembic import command

from app.oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Roundrock#1378@localhost:5432/fastapi_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):

    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db    
    yield TestClient(app)

@pytest.fixture
def test_user2(client):
    user_data = {"email": "aashish456@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    new_user = res.json()
    new_user['password'] = user_data['password']

    assert res.status_code == 201
    return new_user

@pytest.fixture
def test_user(client):
    user_data = {"email": "aashish123@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    new_user = res.json()
    new_user['password'] = user_data['password']

    assert res.status_code == 201
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token): 
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

@pytest.fixture
def test_posts(test_user, test_user2, session):
    posts_data = [{
        "title": "first title",
        "content": "first_content",
        "owner_id": test_user['id']
    }, {
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user['id']
    }, {
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user['id']
    }, {
        "title": "4th title",
        "content": "3th content",
        "owner_id": test_user2['id']
    }]

    # session.add_all([models.User(title = "first title", content = "first_content", owner_id = test_user['id']),
    #                  models.User(title = "2nd title", content = "second_content", owner_id = test_user['id']), 
    #                  models.User(title = "3rd title", content = "third_content", owner_id = test_user['id'])])

    def create_posts_model(post):
       return models.Post(**post)
    
    post_map = map(create_posts_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    session.commit()

    posts = session.query(models.Post).all()
    return posts
