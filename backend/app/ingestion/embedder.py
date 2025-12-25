import random

def embed_chunks(chunks: list[str]) -> list[list[float]]:
    # TEMPORARY STUB: deterministic fake embeddings
    return [[random.random() for _ in range(384)] for _ in chunks]
