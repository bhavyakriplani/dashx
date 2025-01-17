from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/") 
def read_root(): 
    return {"message": "Uptime Monitor API"}

@app.post("/sites/", response_model=schemas.Site)
def create_site(site: schemas.SiteCreate, db: Session = Depends(database.get_db)):
    return crud.create_site(db=db, site=site)

@app.get("/sites/", response_model=list[schemas.Site])
def read_sites(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    sites = crud.get_sites(db, skip=skip, limit=limit)
    return sites

@app.post("/webhook/{site_id}")
def configure_webhook(site_id: int, webhook_url: str, db: Session = Depends(database.get_db)):
    site = crud.get_site(db, site_id=site_id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    site.webhook_url = webhook_url
    db.add(site)
    db.commit()
    db.refresh(site)
    return {"message": "Webhook URL configured successfully"}

        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
