import re

from memory.memory import (
    remember,
    recall,
    forget,
    list_memory
)


def process(command):

    cmd = command.lower().strip()

    # ==========================
    # Remember
    # ==========================

    match = re.search(
        r"remember my (.+?) is (.+)",
        cmd
    )

    if match:

        title = match.group(1).strip()

        value = match.group(2).strip()

        return remember(title, value)

    # ==========================
    # Recall
    # ==========================

    match = re.search(
        r"what is my (.+)",
        cmd
    )

    if match:

        title = match.group(1).strip()

        data = recall(title)

        if data:

            return f"Your {title} is {data}."

        return f"I don't know your {title}."

    # ==========================
    # Forget
    # ==========================

    match = re.search(
        r"forget my (.+)",
        cmd
    )

    if match:

        title = match.group(1).strip()

        return forget(title)

    # ==========================
    # List Memory
    # ==========================

    if (
        "what do you remember" in cmd
        or
        "list memory" in cmd
        or
        "show memory" in cmd
    ):

        return list_memory()

    return None