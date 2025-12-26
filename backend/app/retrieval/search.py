from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
COLLECTION_NAME = "documents"

def retrieve_chunks(query_embedding, top_k=3):
    result = client.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[],
        query=query_embedding,
        limit=top_k,
    )

    return [p.payload["text"] for p in result.points]
