from typing import List
from app.ingestion.embedder import _deterministic_vector


def embed_query(question: str) -> List[float]:
    return _deterministic_vector(question)
