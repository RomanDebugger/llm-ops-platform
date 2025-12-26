from fastapi import APIRouter

router = APIRouter()

@router.post("/documents/upload")
def upload_document():
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
def run_query(payload: dict):
    question = payload.get("question")
    if not question:
        return {"error": "question is required"}

    from app.retrieval.embed_query import embed_query
    from app.retrieval.search import retrieve_chunks

    query_embedding = embed_query(question)
    chunks = retrieve_chunks(query_embedding)

    return {
        "question": question,
        "retrieved_chunks": chunks
    }


@router.get("/runs/{run_id}")
def get_run(run_id: str):
    return {"run_id": run_id}

@router.get("/configs")
def list_configs():
    return []
