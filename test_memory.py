from memory.memory import remember
from memory.memory import recall
from memory.memory import forget
from memory.memory import list_memory

print(
    remember(
        "name",
        "Yash"
    )
)

print(
    remember(
        "college",
        "Rungta College"
    )
)

print(
    recall("name")
)

print(
    recall("college")
)

print(
    list_memory()
)

print(
    forget("college")
)

print(
    list_memory()
)