from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str):
        """Converts text into a vector representation"""
        return self.model.encode(text).tolist()

if __name__ == "__main__":
    embedder = EmbeddingModel()
    test_text = "I am going to drink water."
    vector = embedder.get_embedding(test_text)
    print(f"Vector for '{test_text}': {vector[:5]}...")  
