from guidance import models, gen, system, user, assistant
from rich import print

gpt = models.OpenAI("gpt-4")

with system():
    lm = gpt + """
        You are a data project manager who interacts with potential clients.
        You ask questions to distill the clients needs to parameters that will guide a data analysts work on the project.
    """

with user():
    lm += "Can you all help me figure out the effect of this bill that reclassifies two misdemeanors to felonies?"

with assistant():
    lm += gen("follow up question", stop="?")

print(lm)
