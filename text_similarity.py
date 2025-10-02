from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')
emb1 = model.encode("I love AI")
emb2 = model.encode("I enjoy machine learning")
print(util.cos_sim(emb1, emb2))
# Cosine similarity ranges from -1 to 1; normalized to 0-1 for probability-like interpretation
