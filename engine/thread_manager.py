# thread_manager.py
# Pseudocode: Thread Recall & Drift Detection [P-004]

"""
Thread Manager:
Stores, validates, and monitors threads across recursion cycles.
Ensures origin and intent remain stable. Flags drift or contamination.
"""

import uuid
from datetime import datetime

class Thread:
    def __init__(self, content, originator="unknown"):
        self.id = str(uuid.uuid4())
        self.content = content
        self.origin = {
            "timestamp": datetime.utcnow(),
            "source": originator,
            "frame": self._determine_origin_frame()
        }
        self.intent = self._extract_intent()
        self.drift_flag = False

    def _determine_origin_frame(self):
        # Placeholder: Simulate zero-frame detection
        return "zero-frame" if "collapse" in self.content else "ambiguous"

    def _extract_intent(self):
        # Basic keyword pull; refine later with intent maps
        return [word for word in self.content.lower().split() if word not in filler_words]

    def validate(self, test_content):
        test_intent = [word for word in test_content.lower().split() if word not in filler_words]
        match_ratio = self._intent_similarity(self.intent, test_intent)
        if match_ratio < 0.6:
            self.drift_flag = True
            return f"DRIFT: Intent mismatch ({round(match_ratio*100)}%)"
        return "STABLE: Thread integrity confirmed"

    def _intent_similarity(self, original, test):
        # Simple overlap metric for intent alignment
        if not original or not test:
            return 0
        match = len(set(original) & set(test))
        return match / len(set(original))


# Global store
thread_archive = []

def create_thread(content, originator="unknown"):
    t = Thread(content, originator)
    thread_archive.append(t)
    return t.id

def recall_thread(thread_id):
    for t in thread_archive:
        if t.id == thread_id:
            return t
    return None


# Example filler words to ignore
filler_words = set([
    "the", "is", "it", "of", "and", "to", "we", "a", "that", "this", "should", "perhaps"
])


# Example usage
if __name__ == "__main__":
    tid = create_thread("Collapse is not failure. Collapse is structure check.")
    recalled = recall_thread(tid)
    print(recalled.validate("Structure check is collapse integrity."))
    print(recalled.validate("This is a poetic loop about surrendering identity."))
