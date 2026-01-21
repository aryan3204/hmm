import os
from openai import OpenAI
from brain.memory_manager import MemoryManager
from brain.insight_engine import InsightEngine
from brain.astro_brain import AstroBrain

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AstroAgent:
    def __init__(self):
        self.memory = MemoryManager()
        self.insights = InsightEngine()
        self.astro = AstroBrain()
    
    def process(self, command):
        insights = self.insights.analyze(command)
        astro_guidance = self.astro.get_guidance(command)
        context = self.memory.get_context()
        
        full_context = f"""
MEMORY: {context}
INSIGHTS: {insights}
ASTROLOGY: {astro_guidance}
User: Lucknow full-stack dev + event entrepreneur
        """
        
        messages = [
            {"role": "system", "content": self._get_system_prompt() + full_context},
            {"role": "user", "content": command}
        ]
        
        resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        output = resp.choices[0].message.content
        self.memory.add_interaction(command, output)
        return output
    
    def _get_system_prompt(self):
        try:
            with open("prompts/hmm_wake_prompt.txt") as f:
                return f.read()
        except:
            return "You are AstroBrain. Give best action using memory + astrology."
