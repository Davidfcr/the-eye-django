"""
Json schemas vault for event and applications, for a new combination of category + name + application id
add a new class with name Category_name_applicationid
"""
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class Pageinteraction_pageview_100(BaseModel):
    host: str
    path: str


class Pageinteraction_ctaclick_100(BaseModel):
    host: str
    path: str
    element: str


class Form_100(BaseModel):
    first_name: str
    last_name: str


class Forminteraction_submit_100(BaseModel):
    host: str
    path: str
    element: str
    form: Form_100
