import random

def handle(event, context):
    quotes = [
        "La vie est belle.",
        "Carpe diem.",
        "Rien ne sert de courir, il faut partir à point.",
        "Le savoir est une arme.",
        "Toujours viser la lune."
    ]
    return {"quote": random.choice(quotes)}
