# Dummy logic for now

def get_affiliate_ads(query: str, user_id: str):
    keywords = ["meditation", "stress", "job", "love", "career"]
    for keyword in keywords:
        if keyword in query.lower():
            return [
                {"title": f"Top Book on {keyword.title()}", "link": f"https://amazon.in/{keyword}-book"},
                {"title": f"{keyword.title()} Masterclass", "link": f"https://example.com/{keyword}-course"}
            ]
    return []
