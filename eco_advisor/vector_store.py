import chromadb
import ollama
from .config import DB_PATH, EMBED_MODEL


def get_client() -> chromadb.PersistentClient:
    return chromadb.PersistentClient(path=DB_PATH)


def get_collection(client: chromadb.PersistentClient, name: str = "eco_docs"):
    return client.get_or_create_collection(name=name)


def embed_text(text: str):
    return ollama.embed(model=EMBED_MODEL, input=text)["embeddings"]


def index_if_empty(collection, documents: list[str]):
    if collection.count() == 0:
        for i, doc in enumerate(documents):
            emb = embed_text(doc)
            collection.add(ids=[str(i)], embeddings=emb, documents=[doc])


def query_top_document(collection, query: str) -> str:
    emb = embed_text(query)
    res = collection.query(query_embeddings=emb, n_results=1)
    docs = res.get("documents", [])
    return docs[0][0] if docs else ""


