
import schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import PokemonSchema, RequestPokemon, Response
from config import sessionLocal
import crud


from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

import model

router = APIRouter()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/pokemon/search')
async def search_pokemon(q: str = Query(None), db: Session = Depends(get_db)):
    if q:
        results = db.query(model.Pokemon).filter(
            model.Pokemon.name.ilike(f"%{q}%")).all()
    else:
        results = []

    return results

# @router.post('/create')
# async def create(request: RequestPokemon, db: Session = Depends(get_db)):
#     crud.create_pokemon(db, request.parameter)
#     return Response(code="200", status="ok", message="Pokemon created successfully").dict(exclude_none=True)


# @router.post('/create')
# async def create_pokemon(request: schemas.RequestPokemon, db: Session = Depends(get_db)):
#     crud.create_pokemon(db, request)
#     return Response(status_code=200, content="Pokemon created successfully")

# route for creating pokemon list
@router.post('/create')
async def create_pokemon(request: schemas.RequestPokemon, db: Session = Depends(get_db)):
    try:
        return crud.create_pokemon(db, request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.get('/')
# async def get(db: Session = Depends(get_db)):
#     _pokemon = crud.get_pokemon(db, 0, 100)
#     return Response(code="200", status="ok", message="Successfully fetched all data", result=_pokemon).dict(exclude_none=True)
# listing all pokemon data
@router.get('/')
async def get(db: Session = Depends(get_db)):
    _pokemon = crud.get_pokemon(db, 0, 100)
    return Response(code="200", status="ok", message="Successfully fetched all data", result=_pokemon).dict(exclude_none=True)

# this for detail view  data


@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _pokemon = crud.get_pokemon_by_id(db, id)
    return Response(code="200", status="ok", message="Success get data", result=_pokemon).dict(exclude_none=True)

# for edit


@router.post("/update")
async def update_pokemon(request: RequestPokemon, db: Session = Depends(get_db)):
    _pokemon = crud.update_pokemon(db, pokemon_id=request.parameter.id, name=request.parameter.name,
                                   type=request.parameter.type)
    # , image_path=request.parameter.image_path
    return Response(code="200", status="ok", message="success update data", result=_pokemon).dict(exclude_none=True)

# for deleteing data


@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    crud.remove_pokemon(db, pokemon_id=id)
    return Response(code="200", status="ok", message="success delete data").dict(exclude_none=True)


# from fastapi import APIRouter, HTTPException, Path, Depends
# from schemas import PokemonSchema, RequestPokemon, Response
# from config import sessionLocal
# from sqlalchemy.orm import Session
# import crud

# router = APIRouter()


# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @router.post('/create')
# async def create(request: RequestPokemon, db: Session = Depends(get_db)):
#     crud.create_pokemon(db, request.parameter)
#     return Response(code=200, status="ok", message="Pokemon created successfully").dict(exclude_none=True)


# @router.get('/')
# async def get(db: Session = Depends(get_db)):
#     _pokemon = crud.get_pokemon(db, 0, 100)
#     return Response(code=200, status="ok", message="Successfully fetched all  data", result=_pokemon).dict(exclude_none=True)


# @router.get("/{id}")
# async def get_by_id(id: int, db: Session = Depends(get_db)):
#     _pokemon = crud.get_pokemon_by_id(db, id)
#     return Response(code=200, status="ok", message="Success get data", results=_pokemon).dict(exclude_none=True)


# @router.post("/update")
# async def update_pokemon(request: RequestPokemon, db: Session = Depends(get_db)):
#     _pokemon = crud.update_pokemon(db, pokemon_id=request.parameter.id, name=request.parameter.name,
#                                    type=request.parameter.type, image_path=request.parameter.image_path)
#     return Response(code=200, status="ok", message="success update data", results=_pokemon)


# @router.delete("/{id}")
# async def delete(id: int, db: Session = Depends(get_db)):
#     crud.remove_pokemon(db, pokemon_id=id)
#     return Response(code=200, status="ok", message="success delete data").dict(exclude_none=True)
