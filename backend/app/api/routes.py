from fastapi import APIRouter

router = APIRouter()

@router.post("/documents/upload")
def upload_document():
    # for now, hardcode file path
    from app.ingestion.loader import load_text
    from app.ingestion.chunker import chunk_text
    from app.ingestion.embedder import embed_chunks
    from app.ingestion.indexer import index_embeddings

    text = load_text("sample.txt")
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)
    index_embeddings(chunks, embeddings)

    return {"chunks_indexed": len(chunks)}


@router.post("/query/run")
def run_query():
    return {"status": "not implemented"}

@router.get("/runs/{run_id}")
def get_run(run_id: str):
    return {"run_id": run_id}

@router.get("/configs")
def list_configs():
    return []
