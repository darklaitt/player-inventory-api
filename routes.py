from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud, models
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/players/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db, player)

@router.get("/players/", response_model=list[schemas.Player])
def list_players(db: Session = Depends(get_db)):
    return crud.get_players(db)

@router.post("/players/{player_id}/items/", response_model=schemas.Item)
def add_item(player_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, player_id, item)

@router.get("/players/{player_id}/items/", response_model=list[schemas.Item])
def list_items(player_id: int, db: Session = Depends(get_db)):
    return crud.get_player_items(db, player_id)

@router.delete("/players/{player_id}", tags=["Players"])
def delete_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Игрок не найден")
    db.delete(player)
    db.commit()
    return {"message": "Игрок удалён"}

@router.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Предмет не найден")
    db.delete(item)
    db.commit()
    return {"message": "Предмет удалён"}