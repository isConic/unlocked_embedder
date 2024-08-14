from unlocked import Embedder

MODEL_NAME = "BAAI/bge-small-en-v1.5"
embedder = Embedder(model_name = MODEL_NAME)

print(embedder.embed("Hello"))
print(embedder.batch_embed(["Hello", "World"]))