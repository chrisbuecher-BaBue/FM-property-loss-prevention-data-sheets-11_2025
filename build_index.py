from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

TEXT_DIR = "pdf_texts"
model = SentenceTransformer("all-MiniLM-L6-v2")

filenames = []
vectors = []

for fname in os.listdir(TEXT_DIR):
    with open(os.path.join(TEXT_DIR, fname), "r", encoding="utf-8") as f:
        text = f.read()
    embedding = model.encode(text)
    vectors.append(embedding)
    filenames.append(fname)

vectors_np = np.array(vectors).astype("float32")
index = faiss.IndexFlatL2(vectors_np.shape[1])
index.add(vectors_np)

faiss.write_index(index, "vector.index")

with open("filenames.pkl", "wb") as f:
    pickle.dump(filenames, f)

print("✅ Vektorindex erstellt und gespeichert.")
