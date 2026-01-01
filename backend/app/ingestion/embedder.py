from typing import List
import random
import hashlib

EMBEDDING_DIM = 384

def _deterministic_vector(text: str) -> List[float]:
    text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    seed = int(text_hash[:8], 16)
    rng = random.Random(seed)
    return [rng.random() for _ in range(EMBEDDING_DIM)]
def embed_chunks(chunks: List[str]) -> List[List[float]]:
    return [_deterministic_vector(chunk) for chunk in chunks]
