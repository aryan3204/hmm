class InsightEngine:
    patterns = {
        "coding": ["code", "python", "debug", "leet", "function", "algorithm"],
        "events": ["event", "sponsor", "festival", "booking", "vibenest"],
        "career": ["job", "apply", "resume", "interview", "gcp"],
        "learning": ["learn", "tutorial", "explain", "teach"]
    }
    
    def analyze(self, input_text):
        text = input_text.lower()
        insights = {}
        
        for category, keywords in self.patterns.items():
            if any(keyword in text for keyword in keywords):
                insights[category] = True
        
        # Proactive suggestions
        if insights.get("coding"):
            insights["suggestion"] = "Optimize LeetCode + Python focus"
        elif insights.get("events"):
            insights["suggestion"] = "Target 5 sponsors this week"
        elif insights.get("career"):
            insights["suggestion"] = "Tailor resume for cloud roles"
        
        return insights
