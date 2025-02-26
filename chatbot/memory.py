from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams, ScoredPoint
from config import QDRANT_API_URL, QDRANT_API_KEY
from chatbot.embedding import EmbeddingModel
from datetime import datetime

client = QdrantClient(url=QDRANT_API_URL, api_key=QDRANT_API_KEY)
embedder = EmbeddingModel()

COLLECTION_NAME = "chat_memory"

def setup_qdrant():
    """Initialize the Qdrant collection if not exists."""
    existing_collections = client.get_collections().collections
    collection_names = [col.name for col in existing_collections]

    if COLLECTION_NAME not in collection_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )
        print(f"Created collection: {COLLECTION_NAME}")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")

def store_conversation(user_input: str):
    vector = embedder.get_embedding(user_input)

    point_id = int(datetime.utcnow().timestamp())  

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=point_id,  
                vector=vector,  
                payload={
                    "text": user_input,
                    "timestamp": datetime.utcnow().replace(microsecond=0).isoformat() + "Z"  
                }
            )
        ]
    )


def retrieve_memory(query: str, top_k=5):
    vector = embedder.get_embedding(query)

    search_results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=top_k,
        with_payload=True
    )

    points = search_results.points  

    if points and isinstance(points, list):
        for point in points:
            stored_text = point.payload.get("text", "")
            timestamp = point.payload.get("timestamp", None)

        
            if "when" in query.lower() or "last" in query.lower():
                if timestamp:
                    formatted_timestamp = datetime.fromisoformat(timestamp.replace("Z", "")).strftime("%B %d, %Y at %H:%M")
                    return f"You mentioned '{stored_text}' on {formatted_timestamp}."
                return stored_text  

    
            if stored_text.lower() != query.lower():
                return stored_text  

    return "I don’t have any memory of that."


if __name__ == "__main__":
    setup_qdrant()
    store_conversation("I am going to drink water.")
    response = retrieve_memory("When did I last drink water?")
    print(f"Memory Retrieved: {response}")
