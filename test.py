# test_ai.py - Version 2.0 (Future-Proof)
import os
from dotenv import load_dotenv

# NEW package name
try:
    from google import genai
    from google.genai import types
except ImportError:
    print("❌ ERROR: You need to install 'google-genai'")
    print("Run: pip install google-genai")
    exit(1)

# Load key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Comprehensive checks
if not api_key:
    print("❌ ERROR: GOOGLE_API_KEY not found in .env file")
    print("Create a .env file with: GOOGLE_API_KEY=your_key_here")
    exit(1)

if not api_key.startswith("AIza"):
    print("❌ ERROR: API key looks wrong. Should start with 'AIza'")
    exit(1)

print("✅ API key loaded successfully")

# Create client (NEW way)
try:
    client = genai.Client(api_key=api_key)
    print("✅ AI client created successfully")
except Exception as e:
    print(f"❌ ERROR creating client: {e}")
    exit(1)

# Make a SAFE call
try:
    print("\n🤖 Making AI call...")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Tell me about yourself."
    )
    
    # NEW way to access response
    if response.candidates and response.candidates[0].content.parts:
        text = response.candidates[0].content.parts[0].text
        print("\n" + "="*50)
        print("AI RESPONSE:")
        print(text)
        print("="*50)
        print("\n✅ SUCCESS!")
    else:
        # No text = blocked or error
        finish_reason = response.candidates[0].finish_reason if response.candidates else "UNKNOWN"
        print(f"❌ No text generated. Finish reason: {finish_reason}")
        
        if finish_reason == 2:
            print("The AI blocked your prompt (safety filter).")
            print("Try something more neutral.")
        elif finish_reason == 3:
            print("AI stopped early (max tokens reached).")
        elif finish_reason == 4:
            print("AI stopped due to another reason.")

except Exception as e:
    print(f"❌ ERROR during AI call: {e}")
    print("\nPossible causes:")
    print("- API key is invalid")
    print("- Prompt violates safety policy")
    print("- Network issue (try again)")
    print("- Rate limit (wait 60 seconds)")