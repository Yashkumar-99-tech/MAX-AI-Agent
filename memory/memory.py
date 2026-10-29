from memory.database import MemoryDB

db = MemoryDB()


def remember(title, content):
    """
    Save memory
    """
    db.save_memory(title, content)

    return f"Okay Yash, I will remember your {title}."


def recall(title):
    """
    Recall memory
    """
    data = db.get_memory(title)

    if data:
        return data

    return None


def forget(title):
    """
    Delete memory
    """
    db.delete_memory(title)

    return f"I forgot your {title}."


def list_memory():

    memories = db.get_all()

    if not memories:
        return "I don't remember anything yet."

    text = "Here's what I remember:\n\n"

    for title, content in memories:

        text += f"{title} : {content}\n"

    return text