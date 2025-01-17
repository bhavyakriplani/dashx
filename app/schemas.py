from pydantic import BaseModel

class SiteCreate(BaseModel):
    url: str
    check_interval_seconds: int = 300
    name: str = None
    expected_status_code: int = 200
    webhook_url: str = None

class Site(BaseModel):
    id: int
    url: str
    check_interval_seconds: int
    name: str
    expected_status_code: int
    webhook_url: str = None

    class Config:
        from_attributes = True
