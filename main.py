from fastapi import FastAPI, Request
from pydantic import BaseModel
from categorizer import categorize_input
from rag_logic import get_rag_response
from affiliate_engine import get_affiliate_ads

app = FastAPI()

class UserQuery(BaseModel):
    query: str
    user_id: str

@app.post("/process")
async def process_query(input: UserQuery):
    category = categorize_input(input.query)
    
    if category != "life_issue":
        return {"status": "rejected", "reason": f"Input categorized as '{category}'"}

    rag_result = get_rag_response(input.query)
    ads = get_affiliate_ads(input.query, input.user_id)

    return {
        "category": category,
        "advice": rag_result,
        "ads": ads
    }
