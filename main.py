from dotenv import load_dotenv
import os
from brain.agent_core import AstroAgent

load_dotenv()
agent = AstroAgent()

print("🤖 AstroBrain awake! Type 'hmm + your question' to activate")
print("Type 'quit' to exit\n")

while True:
    command = input("You: ").strip().lower()
    
    if command == "quit":
        print("👋 AstroBrain offline")
        break
    
    if command.startswith("hmm"):
        # Extract command after "hmm"
        query = command[3:].strip()
        if query:
            print("🔥 ASTROBRAIN ACTIVATED!")
            print(f"🧠 Processing: {query}")
            response = agent.process(query)
            print(f"🌌 AstroBrain: {response}\n")
        else:
            print("❓ Say 'hmm should I code now' etc.\n")
    else:
        print("💤 Say 'hmm' first to wake me up!\n")
