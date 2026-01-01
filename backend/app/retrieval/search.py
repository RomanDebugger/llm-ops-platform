from typing import List, Dict, Any
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
COLLECTION_NAME = "documents"


def retrieve_chunks(
    query_embedding: List[float],
    top_k: int = 3,
) -> List[Dict[str, Any]]:
    result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=top_k,
    )

    retrieved = []
    for point in result.points:
        retrieved.append(
            {
                "text": point.payload.get("text"),
                "score": point.score,
            }
        )

    return retrieved
