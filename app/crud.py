from sqlalchemy.orm import Session

from . import models, schemas

def get_site(db: Session, site_id: int):
    return db.query(models.Site).filter(models.Site.id == site_id).first()

def get_sites(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Site).offset(skip).limit(limit).all()

def create_site(db: Session, site: schemas.SiteCreate):
    db_site = models.Site(**site.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site
