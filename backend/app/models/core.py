from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime

class QueryRun(BaseModel):
    id: str
    question: str
    config_id: str
    retrieved_chunks: List[str]
    response: str
    latency_ms: float
    token_usage: Dict[str, int]
    cost: float
    created_at: datetime
