# unlocked_embedder
A short natural language embedding utility for sociology research. Encapsulates models that are  less restrictive than "aligned" embeders.


# usage example:  

```python

from unlocked import Embedder

MODEL_NAME = "BAAI/bge-small-en-v1.5"
embedder = Embedder(model_name = MODEL_NAME)

print(embedder.embed("Hello"))
print(embedder.batch_embed(["Hello", "World"]))

```


## How to contribute


Main branch is sacred. You merge finished things in there. Things are deemed finish once you've gone through `the process``

`The process`:   

- Create a branch for the thing you want to add `git branch feature/my_fancy_branch`. Start the branch with `feature/`. You only ever add feature sized things.   
- Work on it, make the branch as messy as you'd like. Consult iwth other to make sure you're not stepping on their code/work.   
- When you've got something you like, show it off to other team members. 
- When everyone is ok with what you've written and you've gotten the A OK from them. Clean up your code.  
- Create a pull request to main. 
- Merge into main
- Celebrate `the process`
