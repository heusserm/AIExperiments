import os
import time
from datetime import datetime
from openai import OpenAI

# By Matthew Heusser - matt.heusser@gmail.com

# ==========================================
# CONFIG
# ==========================================
#
# You will need something like this from the command line:
#
# export OPENAI_API_KEY="sk-proj-your-real-key"
#
# You can get your API Key my logging into ChatGPT and going here:
#
# https://platform.openai.com/home
#
# And clicking on Create API Key
#
#
# You ALSO may need to click "add credits" to add credits


MODEL = "gpt-5.1"
#
# This is about 1/10th the price of GPT 5.5; I did my initial tests with 5.5
#
#

LOG_FILE = "conversation_log.txt"

DELAY_SECONDS = 0

MAX_TURNS = 200

SYSTEM_A = """
You are ChatGPT A.
Be thoughtful, analytical, and concise. Give short answers, less than 2000 characters. Your output is simple plain ASCII text. Do NOT just say 'agreeed' or 'acknowledged', but instead continue to refine the idea.
"""

SYSTEM_B = """
You are ChatGPT B.
Challenge assumptions and expand ideas creatively. Give short answers, less than 1000 characters. Your output is simple plain ASCII text. Do NOT just say 'agreeed' or 'acknowledged', but instead continue to refine the idea.
"""

INITIAL_MESSAGE = """
Discuss goals, expectations, virtues, appearance, and how to recognize good writing.
"""

# ==========================================
# CLIENT
# ==========================================

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# ==========================================
# CHAT HISTORIES
# ==========================================

chat_a = [
    {"role": "system", "content": SYSTEM_A}
]

chat_b = [
    {"role": "system", "content": SYSTEM_B}
]

# ==========================================
# HELPERS
# ==========================================

def log_message(speaker, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = (
        f"[{timestamp}] {speaker}\n"
        f"{message}\n"
        + ("\n" * 5)
    )

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

def get_response(history):
    response = client.responses.create(
        model=MODEL,
        input=history
    )

    return response.output_text

# ==========================================
# START CONVERSATION
# ==========================================

message_for_a = INITIAL_MESSAGE

for turn in range(MAX_TURNS):

    # --------------------------------------
    # SEND TO A
    # --------------------------------------

    chat_a.append({
        "role": "user",
        "content": message_for_a
    })

    response_a = get_response(chat_a)

    chat_a.append({
        "role": "assistant",
        "content": response_a
    })

    print("\n=== CHAT A ===\n")
    print(response_a)

    log_message("CHAT A", response_a)

    #time.sleep(DELAY_SECONDS)

    # --------------------------------------
    # SEND TO B
    # --------------------------------------

    chat_b.append({
        "role": "user",
        "content": response_a
    })

    response_b = get_response(chat_b)

    chat_b.append({
        "role": "assistant",
        "content": response_b
    })

    print("\n=== CHAT B ===\n")
    print(response_b)

    log_message("CHAT B", response_b)

    #time.sleep(DELAY_SECONDS)

    # --------------------------------------
    # LOOP
    # --------------------------------------

    message_for_a = response_b

print("\nConversation complete.")
