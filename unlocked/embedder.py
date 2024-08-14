from fastembed import TextEmbedding
from typing import List

class NoHuggingFaceModelProvidedException(Exception):
    pass

class Embedder:
    def __init__(self, model_name = None):
        if model_name is None:
            raise NoHuggingFaceModelProvidedException("model_name is None. Please pass a model name")

        self.model = TextEmbedding(model_name=model_name)
    
    def embed(self, document):
        return next(self.model.embed([document]))

    def batch_embed(self, documents:List[str]):
        return list(self.model.embed(documents))

if __name__ == "__main__":
    MODEL_NAME = "BAAI/bge-small-en-v1.5"

    embedder = Embedder(model_name = MODEL_NAME)

    print(embedder.embed("Foo"))
    print(embedder.batch_embed(["Foo", "Bar"]))

