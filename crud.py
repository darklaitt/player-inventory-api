from sqlalchemy.orm import Session
import models, schemas

def get_players(db: Session):
    return db.query(models.Player).all()

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(username=player.username)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def create_item(db: Session, player_id: int, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict(), owner_id=player_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_player_items(db: Session, player_id: int):
    return db.query(models.Item).filter(models.Item.owner_id == player_id).all()
