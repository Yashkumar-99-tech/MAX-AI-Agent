import re


class IntentDetector:

    def detect(self, command):

        cmd = command.lower().strip()

        # ==========================
        # Open Commands
        # ==========================

        if re.search(r"\b(open|launch|start)\b", cmd):
            return "OPEN"

        # ==========================
        # Play Commands
        # ==========================

        if re.search(r"\b(play)\b", cmd):
            return "PLAY"

        # ==========================
        # Search Commands
        # ==========================

        if re.search(r"\b(search|find|google)\b", cmd):
            return "SEARCH"

        # ==========================
        # Screenshot
        # ==========================

        if "screenshot" in cmd:
            return "SCREENSHOT"

        # ==========================
        # Memory
        # ==========================

        if "remember" in cmd:
            return "MEMORY_SAVE"

        if "forget" in cmd:
            return "MEMORY_DELETE"

        if "what is my" in cmd:
            return "MEMORY_RECALL"

        return "CHAT"