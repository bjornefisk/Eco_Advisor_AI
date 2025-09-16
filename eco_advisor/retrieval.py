from .config import get_documents
from .vector_store import get_client, get_collection, index_if_empty, query_top_document


def bootstrap_index():
    client = get_client()
    collection = get_collection(client)
    docs = get_documents()
    index_if_empty(collection, docs)
    return collection


def get_relevant_context(prompt: str) -> str:
    collection = bootstrap_index()
    return query_top_document(collection, prompt)


