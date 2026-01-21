import json
import os

class AstroBrain:
    def __init__(self):
        self.user_chart = {
            "sun": "virgo",      # Practical + analytical
            "moon": "scorpio",   # Intense + strategic  
            "rising": "leo"      # Bold + entrepreneurial
        }
        self.transits = self._load_transits()
    
    def _load_transits(self):
        try:
            with open("data/planets.json") as f:
                return json.load(f)
        except:
            return {
                "mercury": "aquarius",  # Communication/tech
                "jupiter": "taurus",    # Growth/events  
                "saturn": "pisces",     # Career structure
                "moon_phase": "waxing"
            }
    
    def get_guidance(self, command):
        text = command.lower()
        transits = self.transits
        
        # TECH/CODING (Mercury rules your Virgo Sun)
        if any(word in text for word in ["code", "python", "tech", "debug"]):
            mercury_ok = transits["mercury"] not in ["retrograde", "pisces"]
            return f"MERCURY {transits['mercury']}: {'✅ PERFECT for coding breakthroughs' if mercury_ok else '⚠️ Double-check logic'}"
        
        # EVENTS/ENTREPRENEUR (Jupiter expansion)
        elif any(word in text for word in ["event", "sponsor", "festival", "vibenest"]):
            return f"JUPITER {transits['jupiter']}: 🚀 Massive expansion for events/sponsors"
        
        # CAREER MOVES (Saturn discipline)
        elif any(word in text for word in ["job", "career", "apply", "gcp"]):
            return f"SATURN {transits['saturn']}: 🪨 Build your tech empire now"
        
        # GENERAL TIMING
        return f"MOON {transits['moon_phase']}: {'⚡ ACT NOW' if transits['moon_phase']=='waxing' else '📋 Plan strategically'}"
