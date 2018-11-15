import unittest
from app import create_app


def client_app():
    app = create_app()
    test_client = app.test_client()
    return test_client

