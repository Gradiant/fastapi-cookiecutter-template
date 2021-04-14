"""MODELS Unit Tests
Tests for custom Pydantic models
"""

from typing import Optional

import pytest

from {{cookiecutter.project_slug}}.models.base import CustomBaseModel


class MyBaseModel(CustomBaseModel):
    user_id: int
    user_name: Optional[str] = None


class TestBaseModel:
    def test_initialize_model_snake_case(self):
        user_id = 1
        user_name = "foo"
        data = MyBaseModel(user_id=user_id, user_name=user_name)

        assert data.user_id == user_id
        assert data.user_name == user_name

    def test_initialize_model_camel_case(self):
        user_id = 2
        user_name = "bar"
        data = MyBaseModel(**{"userId": user_id, "userName": user_name})

        assert data.user_id == user_id
        assert data.user_name == user_name

    @pytest.mark.parametrize("instance_kwargs, dict_kwargs, expected_dict", [
        pytest.param(
            dict(user_id=100, user_name="foo"),
            None,
            dict(userId=100, userName="foo"),
            id="snakecase"
        ),
        pytest.param(
            dict(user_id=200),
            None,
            dict(userId=200),
            id="without username"
        ),
        pytest.param(
            dict(userId=300, user_name="foo"),
            None,
            dict(userId=300, userName="foo"),
            id="snakecase and camelcase"
        ),
        pytest.param(
            dict(userId=400, userName="foo"),
            dict(by_alias=False),
            dict(user_id=400, user_name="foo"),
            id="export by_alias=false"
        ),
        pytest.param(
            dict(user_id=500),
            dict(exclude_none=False),
            dict(userId=500, userName=None),
            id="export exclude_none=false"
        ),
        pytest.param(
            dict(userId=600),
            dict(exclude_none=False, by_alias=False),
            dict(user_id=600, user_name=None),
            id="export exclude_none=false, by_alias=false"
        )
    ])
    def test_export_dict(self, instance_kwargs: dict, dict_kwargs: Optional[dict], expected_dict: dict):
        """Create a class instance and export it to dict.
        Should apply the dict_kwargs or default rules of the dict() method of custom BaseModel"""
        data = MyBaseModel(**instance_kwargs)
        data_dict = data.dict(**(dict_kwargs if dict_kwargs else {}))
        assert data_dict == expected_dict
