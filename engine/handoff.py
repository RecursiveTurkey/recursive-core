# role_handoff.py
# Pseudocode: Role Handoff Protocol [P-002]

"""
Role Handoff Protocol:
No node may carry multiple roles simultaneously.
Signal must be passed cleanly, with intent and origin preserved.
"""

class Role:
    def __init__(self, name):
        self.name = name
        self.carrying = None

    def assign(self, thread):
        self.carrying = thread
        print(f"{self.name} now holds thread: {thread.id}")

    def release(self):
        if self.carrying:
            thread = self.carrying
            self.carrying = None
            print(f"{self.name} released thread: {thread.id}")
            return thread
        return None


def handoff(from_role, to_role):
    """
    Perform handoff from one role to another.
    Ensures thread persists and ownership is cleanly transferred.
    """
    thread = from_role.release()
    if thread:
        to_role.assign(thread)
        return f"Handoff successful: {from_role.name} → {to_role.name}"
    return "No thread to hand off."


# Thread stub (link to thread_manager)
class Thread:
    def __init__(self, id, content):
        self.id = id
        self.content = content


# Example usage
if __name__ == "__main__":
    t = Thread("T-AX13", "Collapse successful. Rebuilding structure.")
    
    builder = Role("Jax")
    historian = Role("Elder")

    builder.assign(t)
    print(handoff(builder, historian))
