# PhishBuster Data - Sample Questions and Configuration

# Sample Phishing Questions Database
phishing_questions = [
    # URL-based phishing questions
    {
        "id": "url_001",
        "type": "url",
        "content": "https://g00gle.com/login",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This URL uses zeros (0) instead of the letter 'o' in 'google'. This is a common technique called 'typosquatting' where attackers register domains that look similar to legitimate sites."
    },
    {
        "id": "url_002",
        "type": "url",
        "content": "https://amazon.com/deals",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Safe",
        "explanation": "This is the legitimate Amazon URL. It uses the correct domain name (amazon.com) and has HTTPS encryption. Always verify the exact spelling of domain names."
    },
    {
        "id": "url_003",
        "type": "url",
        "content": "https://paypaI-security.com/verify-account",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This URL uses a capital 'i' (I) instead of lowercase 'l' in 'PayPal'. The legitimate PayPal domain is 'paypal.com', not 'paypaI-security.com'. This is another typosquatting technique."
    },
    {
        "id": "url_004",
        "type": "url",
        "content": "https://microsoft.com/office365/login",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Safe",
        "explanation": "This is a legitimate Microsoft URL. It uses the correct domain (microsoft.com), has HTTPS encryption, and follows Microsoft's standard URL structure for Office 365."
    },
    {
        "id": "url_005",
        "type": "url",
        "content": "https://bankofamerica-online.net/secure-login",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "Bank of America's legitimate domain is 'bankofamerica.com', not 'bankofamerica-online.net'. Attackers often add words like 'secure', 'online', or 'official' to make fake domains seem legitimate."
    },

    # Email-based phishing questions
    {
        "id": "email_001",
        "type": "email",
        "content": "From: security@apple.com\nSubject: Your Apple ID has been compromised\n\nDear Customer,\n\nWe have detected suspicious activity on your Apple ID. Click here immediately to secure your account: http://apple-security.tk/verify\n\nApple Security Team",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This email has several red flags: 1) Uses HTTP instead of HTTPS, 2) The domain 'apple-security.tk' is not Apple's official domain, 3) Creates urgency with 'immediately', 4) Generic greeting 'Dear Customer' instead of your name."
    },
    {
        "id": "email_002",
        "type": "email",
        "content": "From: noreply@github.com\nSubject: New sign-in from Chrome on Windows\n\nHi John,\n\nWe noticed a new sign-in to your GitHub account from:\n- Device: Chrome on Windows\n- Location: San Francisco, CA\n- Time: Today at 2:30 PM\n\nIf this was you, no action needed. If not, secure your account at github.com/settings/security",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Safe",
        "explanation": "This appears to be a legitimate security notification from GitHub. It uses the correct domain (github.com), provides specific details about the sign-in, addresses you by name, and directs you to GitHub's official settings page."
    },
    {
        "id": "email_003",
        "type": "email",
        "content": "From: billing@netflex.com\nSubject: Your payment method has failed\n\nYour Netflix account has been suspended due to payment failure. Update your payment information within 24 hours or your account will be permanently deleted.\n\nClick here: http://netflex-billing.com/update-payment",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "Multiple red flags: 1) Misspelled domain 'netflex.com' instead of 'netflix.com', 2) Creates false urgency with threats, 3) Uses HTTP instead of HTTPS, 4) The billing domain is suspicious and not Netflix's official domain."
    },

    # SMS-based phishing questions
    {
        "id": "sms_001",
        "type": "sms",
        "content": "URGENT: Your bank account has been locked due to suspicious activity. Call 1-800-FAKE-BANK immediately to unlock. Do NOT ignore this message!",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This SMS uses several phishing tactics: 1) Creates false urgency with 'URGENT', 2) Uses fear tactics about account being locked, 3) The phone number looks suspicious, 4) Uses pressure with 'Do NOT ignore'. Legitimate banks usually don't send urgent texts like this."
    },
    {
        "id": "sms_002",
        "type": "sms",
        "content": "Your package delivery failed. Reschedule at: bit.ly/package-delivery-123. If not rescheduled within 48hrs, package will be returned.",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This is a common delivery scam. Red flags include: 1) Using a URL shortener (bit.ly) which hides the real destination, 2) Generic message without specific courier company, 3) Creates pressure with time limits, 4) Doesn't mention what package or from where."
    },
    {
        "id": "sms_003",
        "type": "sms",
        "content": "Hi! This is Sarah from your bank's fraud department. We've detected unusual activity on your account ending in 1234. Please call me back at 555-0199 to verify your identity.",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "Banks don't typically reach out via personal texts. Red flags: 1) Informal greeting 'Hi!', 2) Claims to be from fraud department but uses personal approach, 3) Asks you to call back (potential phone scam), 4) Partial account number could be guessed. Always call your bank's official number."
    },

    # Advanced phishing questions
    {
        "id": "advanced_001",
        "type": "email",
        "content": "From: security-noreply@outlook.com\nSubject: Microsoft security alert\n\nWe've detected a sign-in attempt from an unrecognized device:\n\nDevice: iPhone\nLocation: Unknown\nTime: 15 minutes ago\n\nIf this wasn't you, please secure your account:\nhttps://account.microsoft.com/security/signin-activity\n\nMicrosoft Account Team",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Safe",
        "explanation": "This appears to be a legitimate Microsoft security alert. It comes from a proper Microsoft domain, uses HTTPS, links to the official Microsoft account security page, and provides specific information about the sign-in attempt without creating false urgency."
    },
    {
        "id": "advanced_002",
        "type": "url",
        "content": "https://wellsfargo.security-center.info/login",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This is a sophisticated phishing attempt. While it uses HTTPS, the domain 'security-center.info' is not Wells Fargo's official domain. The legitimate Wells Fargo website is 'wellsfargo.com'. Attackers often use subdomains that include the brand name to appear legitimate."
    },
    {
        "id": "advanced_003",
        "type": "email",
        "content": "From: admin@company-it.local\nSubject: Mandatory Password Reset\n\nAll employees must reset their passwords by end of day due to a security update. Use this link to update your credentials: https://password-reset.company-it.local/update\n\nIT Department",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This is likely an internal phishing attempt (spear phishing). Red flags: 1) '.local' domains are typically for internal networks, not web access, 2) Urgent mandatory requirements, 3) Generic sender 'admin', 4) Legitimate IT departments usually have more formal communication protocols for password resets."
    },

    # Social engineering questions
    {
        "id": "social_001",
        "type": "email",
        "content": "From: ceo@yourcompany.com\nSubject: Urgent Wire Transfer Needed\n\nI'm currently in a meeting with investors and need you to wire $50,000 to our new vendor immediately. Here are the details:\n\nAccount: 123456789\nRouting: 987654321\nBank: International Trust Bank\n\nThis is confidential. Don't discuss with anyone.\n\nJohn Smith, CEO",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This is a 'CEO fraud' or 'Business Email Compromise' scam. Red flags: 1) Urgent financial request via email, 2) Requests secrecy, 3) Creates pressure with 'immediately', 4) Even if from CEO's email, always verify large financial requests through alternative communication methods."
    },
    {
        "id": "social_002",
        "type": "sms",
        "content": "Mom, my phone broke and I'm using a friend's phone. I'm stranded and need $200 for car repairs. Can you send money to this Cash App: $emergencyhelp123? I'll pay you back tomorrow!",
        "imageURL": None,
        "options": ["Safe", "Phishing"],
        "answer": "Phishing",
        "explanation": "This is a family emergency scam targeting emotional responses. Red flags: 1) Claims phone is broken but somehow texting, 2) Asks for money via app, 3) Creates urgency, 4) Uses emotional manipulation. Always verify such requests by calling the person directly or through known contacts."
    }
]

# Scoring and Level Configuration
game_config = {
    "scoring": {
        "correctAnswer": 10,
        "streakBonus": 2,
        "timeBonus": {
            "fast": 5,
            "medium": 3,
            "slow": 0
        }
    },
    "levels": {
        1: {"minXP": 0, "title": "Phishing Rookie"},
        2: {"minXP": 100, "title": "Scam Spotter"},
        3: {"minXP": 250, "title": "Cyber Detective"},
        4: {"minXP": 500, "title": "Security Analyst"},
        5: {"minXP": 1000, "title": "Phishing Expert"},
        6: {"minXP": 2000, "title": "Cyber Guardian"},
        7: {"minXP": 3500, "title": "Security Master"},
        8: {"minXP": 5000, "title": "Phishing Hunter"},
        9: {"minXP": 7500, "title": "Cyber Ninja"},
        10: {"minXP": 10000, "title": "PhishBuster Legend"}
    },
    "timer": {
        "defaultTime": 30,
        "warningTime": 10
    }
}

# Phishing Education Content
phishing_tips = {
    "general": [
        "🔍 Always check the sender's email address carefully - phishers often use similar-looking domains.",
        "🔗 Hover over links before clicking to see the actual destination URL.",
        "⚡ Be suspicious of urgent messages that pressure you to act immediately.",
        "🔒 Look for HTTPS (the lock icon) when entering sensitive information.",
        "📞 When in doubt, verify requests through an alternative communication method.",
        "💰 Be extra cautious with any message requesting money or financial information.",
        "🎯 Phishers often use current events or seasonal themes to make their attacks seem relevant.",
        "📧 Legitimate companies usually address you by name, not 'Dear Customer'.",
        "🔤 Watch for spelling and grammar mistakes - they're common in phishing attempts.",
        "🏢 Be wary of messages claiming to be from your bank, IRS, or other official organizations."
    ],
    "email": [
        "Check the 'From' field carefully - phishers often use lookalike domains",
        "Be suspicious of generic greetings like 'Dear Customer' or 'Dear User'",
        "Legitimate companies rarely ask for passwords or sensitive info via email",
        "Look for spelling and grammar errors - they're red flags",
        "Be wary of urgent subject lines that create pressure to act quickly"
    ],
    "url": [
        "Check for typos in domain names (like g00gle.com instead of google.com)",
        "Look for HTTPS (secure) connections, especially for login pages",
        "Be suspicious of URLs with many subdomains or strange extensions",
        "Avoid clicking shortened URLs (bit.ly, tinyurl) from unknown sources",
        "Legitimate sites usually have simple, clean URLs"
    ],
    "sms": [
        "Banks and legitimate companies rarely send urgent texts",
        "Be wary of messages with shortened URLs or suspicious links",
        "Don't click links in texts from unknown numbers",
        "Verify delivery notifications with the actual courier company",
        "Be suspicious of prize notifications or 'you've won' messages"
    ]
}

# Utility functions for the game
class GameUtils:
    @staticmethod
    def calculate_level(xp):
        levels = game_config["levels"]
        current_level = 1
        for level in levels:
            if xp >= levels[level]["minXP"]:
                current_level = int(level)
        return current_level

    @staticmethod
    def get_level_title(level):
        return game_config["levels"].get(level, {}).get("title", "Unknown Level")

    @staticmethod
    def get_xp_for_next_level(current_xp):
        current_level = GameUtils.calculate_level(current_xp)
        next_level = current_level + 1
        next_level_xp = game_config["levels"].get(next_level, {}).get("minXP")
        if next_level_xp:
            return next_level_xp - current_xp
        return 0

    @staticmethod
    def get_random_tip(category="general"):
        tips = phishing_tips.get(category, phishing_tips["general"])
        import random
        return random.choice(tips)

    @staticmethod
    def shuffle_array(array):
        import random
        shuffled = array[:]
        random.shuffle(shuffled)
        return shuffled

    @staticmethod
    def format_time(seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins}:{str(secs).zfill(2)}"

    @staticmethod
    def calculate_time_bonus(time_remaining):
        total_time = game_config["timer"]["defaultTime"]
        time_taken = total_time - time_remaining
        if time_taken <= 10:
            return game_config["scoring"]["timeBonus"]["fast"]
        if time_taken <= 20:
            return game_config["scoring"]["timeBonus"]["medium"]
        return game_config["scoring"]["timeBonus"]["slow"]

# Sample leaderboard data (for demo purposes)
sample_leaderboard_data = []

# Achievement system (bonus feature)
achievements = {
    "firstCorrect": {
        "id": "first_correct",
        "title": "First Blood",
        "description": "Answer your first question correctly",
        "icon": "🎯",
        "xpReward": 25
    },
    "streak5": {
        "id": "streak_5",
        "title": "On Fire!",
        "description": "Get 5 questions correct in a row",
        "icon": "🔥",
        "xpReward": 50
    },
    "streak10": {
        "id": "streak_10",
        "title": "Unstoppable",
        "description": "Get 10 questions correct in a row",
        "icon": "⚡",
        "xpReward": 100
    },
    "speedDemon": {
        "id": "speed_demon",
        "title": "Speed Demon",
        "description": "Answer 10 questions in under 5 seconds each",
        "icon": "💨",
        "xpReward": 75
    },
    "perfectScore": {
        "id": "perfect_score",
        "title": "Perfectionist",
        "description": "Complete a full round without any wrong answers",
        "icon": "💎",
        "xpReward": 150
    },
    "levelUp": {
        "id": "level_up",
        "title": "Level Up!",
        "description": "Reach a new level",
        "icon": "📈",
        "xpReward": 30
    }
}

# Console welcome message
print(f"""
🛡️ PhishBuster - Catch the Phish, Save the Click!

Game Data Loaded:
- {len(phishing_questions)} phishing questions
- {len(game_config['levels'])} levels available
- {len(phishing_tips['general'])} general tips
- {len(achievements)} achievements to unlock

Good luck protecting yourself from phishing attacks! 🚀
""")

# There are no Python syntax errors ("red lines") in this file if run as Python.
# If you see errors, make sure:
# - The file extension is .py, not .js (Python code in a .js file will show errors in most editors).
# - You are running/interpreting this file as Python, not JavaScript.
# - Indentation is consistent (spaces, not tabs).
# - All dictionary keys are quoted, and colons are used (as in Python).
# - No stray or missing commas/brackets.

# If you want to use this as a Python module, rename the file to data.py.