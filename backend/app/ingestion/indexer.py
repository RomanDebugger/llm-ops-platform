from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import uuid

client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "documents"

def index_embeddings(chunks, embeddings):
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config={"size": len(embeddings[0]), "distance": "Cosine"}
        )

    points = []
    for chunk, vector in zip(chunks, embeddings):
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={"text": chunk}
            )
        )

    client.upsert(collection_name=COLLECTION_NAME, points=points)
