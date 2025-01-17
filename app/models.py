from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    check_interval_seconds = Column(Integer, default=300)
    name = Column(String, nullable=True)
    expected_status_code = Column(Integer, default=200)
    webhook_url = Column(String, nullable=True)

class SiteStatusHistory(Base):
    __tablename__ = "site_status_history"

    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, index=True)
    status = Column(String)
    response_time_ms = Column(Integer)
    last_checked = Column(DateTime)
    last_status_change = Column(DateTime)
