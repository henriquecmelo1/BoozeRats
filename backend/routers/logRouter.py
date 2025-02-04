from fastapi import APIRouter, Depends
from schemas.logSchema import LogBase, Log
from services.log_service import create_log, get_log, get_logs, update_log, delete_log
from sqlalchemy.orm import Session
from db.database import get_db

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.post("/", response_model=Log)
async def create_new_log(log: LogBase, db: Session = Depends(get_db)):
    return create_log(db=db, log=log)

@router.get("/{log_id}", response_model=Log)
async def get_single_log(log_id: int, db: Session = Depends(get_db)):
    return get_log(db=db, log_id=log_id)

@router.get("/", response_model=list[Log])
async def get_all_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_logs(db=db, skip=skip, limit=limit)

@router.put("/{log_id}", response_model=Log)
async def update_single_log(log_id: int, log: LogBase, db: Session = Depends(get_db)):
    return update_log(db=db, log_id=log_id, log=log)

@router.delete("/{log_id}", response_model=str)
async def delete_single_log(log_id: int, db: Session = Depends(get_db)):
    return delete_log(db=db, log_id=log_id)

