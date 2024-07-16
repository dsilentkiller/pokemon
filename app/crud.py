from sqlalchemy.orm import Session
from model import Pokemon
from schemas import PokemonSchema


# retrive all pokemon lists
def get_pokemon(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pokemon).offset(skip).limit(limit).all()


# geting pokemin with id
def get_pokemon_by_id(db: Session, pokemon_id: int):
    return db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

# creating pokemon


def create_pokemon(db: Session, pokemon: PokemonSchema):
    _pokemon = Pokemon(name=pokemon.name, type=pokemon.type,
                       image=pokemon.image)
    db.add(_pokemon)
    db.commit()
    db.refresh(_pokemon)
    return _pokemon

# dleete in pokemon list


def remove_pokemon(db: Session, pokemon_id: int):
    _pokemon = get_pokemon_by_id(db=db, pokemon_id=pokemon_id)
    db.delete(_pokemon)
    db.commit()


def update_pokemon(db: Session, pokemon_id: int, name: str, type: str, image: str):
    _pokemon = get_pokemon_by_id(db=db, pokemon_id=pokemon_id)
    _pokemon.name = name
    _pokemon.type = type
    _pokemon.image = image
    db.commit()
    db.refresh(_pokemon)
    return _pokemon
