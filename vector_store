import os
import requests

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
VECTOR_TABLE = "base44_vectors"

def query_vector_store(embedding: list, top_k: int = 3):
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/rpc/match_base44",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "query_embedding": embedding,
            "match_count": top_k,
            "table_name": VECTOR_TABLE
        }
    )
    return response.json()
