import os
print("✅ SYSTEM.PY LOADED")

def execute(command):

    command = command.lower().strip()

    print("SYSTEM RECEIVED :", command)

    if "calculator" in command:

        print("Calculator Command Matched")

        os.system("start calc")

        return "Opening Calculator."

    elif "notepad" in command:

        print("Notepad Command Matched")

        os.system("start notepad")

        return "Opening Notepad."

    elif "paint" in command:

        print("Paint Command Matched")

        os.system("start mspaint")

        return "Opening Paint."

    elif "cmd" in command or "command prompt" in command:

        print("CMD Command Matched")

        os.system("start cmd")

        return "Opening Command Prompt."

    print("No System Command Found")

    return None