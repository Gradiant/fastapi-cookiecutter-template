import pydantic

from ..utils import snakecase_to_camelcase


class CustomBaseModel(pydantic.BaseModel):
    # Custom BaseModel for all Pydantic-based models, featuring:
    #   - all fields are aliased to camelCase notation, so they can be initialized by both
    #     canonical snake_case notation (the name defined on each class) or camelCase (the auto-generated alias)
    #   - dict() method, by default, does not return fields set to None,
    #     and returns field keys as their alias
    #   - strip whitespaces from string fields by default

    class Config:
        anystr_strip_whitespace = True
        allow_population_by_field_name = True
        alias_generator = snakecase_to_camelcase

    def dict(self, exclude_none: bool = True, by_alias: bool = True, **kwargs):
        return super().dict(exclude_none=exclude_none, by_alias=by_alias, **kwargs)
