from sqlalchemy import  create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from infastructure.database import Base
from main import app
from models.user import  Users
from fastapi.testclient import TestClient
from passlib.context import CryptContext
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {
        'username': 'john_doe',
        'id': 1,
        'user_role': 'admin',
    }


client = TestClient(app)


@pytest.fixture
def test_user():
    user = Users(
        email='john_doe@exmaple.com',
        username='john_doe',
        first_name='John',
        last_name='Doe',
        hashed_password=bcrypt_context.hash("test123"),
        role="admin",
        phone_number="1112220"
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()

