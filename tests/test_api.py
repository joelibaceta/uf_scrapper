import pytest

from ..api import app


class TestAPI:
    def test_get_uf_api(self):
        response = app.app.test_client().get("/uf?year=2020&month=1&day=1")

        assert response.status_code == 200
        assert response.json == {"status": "success", "data": {"uf_value": 28310.86}}

    def test_get_uf_api_with_invalid_day(self):
        response = app.app.test_client().get("/uf?year=2020&month=1&day=32")

        assert response.status_code == 200
        assert response.json == {
            "status": "error",
            "message": "Day must be between 1 and 31",
        }

    def test_get_uf_api_with_invalid_month(self):
        response = app.app.test_client().get("/uf?year=2020&month=13&day=1")

        assert response.status_code == 200
        assert response.json == {
            "status": "error",
            "message": "Month must be between 1 and 12",
        }

    def test_get_uf_api_with_invalid_year(self):
        response = app.app.test_client().get("/uf?year=2012&month=1&day=1")

        assert response.status_code == 200
        assert response.json == {
            "status": "error",
            "message": "Year must be equal or greater than 2013",
        }
