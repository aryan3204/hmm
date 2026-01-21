import json
import os
from datetime import datetime

class MemoryManager:
    def __init__(self):
        os.makedirs("memory", exist_ok=True)
        self.file = "memory/hmm_history.json"
        self.history = self._load()
    
    def _load(self):
        try:
            with open(self.file, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def _save(self):
        with open(self.file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def add_interaction(self, user_input, agent_output):
        self.history.append({"time": datetime.now().isoformat(), "user": user_input, "agent": agent_output})
        self.history = self.history[-100:]
        self._save()
    
    def get_context(self):
        recent = self.history[-5:]
        return "\n".join([f"Q: {h['user']} → A: {h['agent']}" for h in recent]) if recent else "No history"
