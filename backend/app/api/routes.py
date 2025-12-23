from fastapi import APIRouter

router = APIRouter()

@router.post("/documents/upload")
def upload_document():
    return {"status": "not implemented"}

@router.post("/query/run")
def run_query():
    return {"status": "not implemented"}

@router.get("/runs/{run_id}")
def get_run(run_id: str):
    return {"run_id": run_id}

@router.get("/configs")
def list_configs():
    return []
