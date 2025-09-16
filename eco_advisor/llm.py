import ollama
from .config import GEN_MODEL


def generate_answer(context: str, question: str) -> str:
    prompt = (
        f"Background:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer as an expert eco‐advisor:"
    )
    res = ollama.generate(model=GEN_MODEL, prompt=prompt)
    return res.get("response", "")


