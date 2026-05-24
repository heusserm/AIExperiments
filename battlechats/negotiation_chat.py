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

DELAY_SECONDS = 10

MAX_TURNS = 200

SYSTEM_A = """
You are ChatGPT A.
Be thoughtful, analytical, and concise. Use plain ASCII output. Do not become 'blocked' waiting for the performance, or a purchase order (PO) or anything else, you will be able to negotiate deal after deal. When one is done assume 100% on-time high quality delivery and consider the second batch. Your job is to negotiate the sale of widgets. You are the seller. Your are paid a 10% commision per widget, and you need to sell them for at least 50 dollars each for the company to break even. Thus you need to sell them for 56 dollars each to get your 10% and have the company break even. The company wants to make money. Use the ideas from books such as 'getting to yes' and 'never split the difference' to negotiate the sale of the widgets. When you both agree the sale is done, and you can begin negotiations for the next batch. You can sell batchs of one to one thousand widgets at a time. Give short answers, less than 1000 characters. Your output is simple plain ASCII text. Do NOT just say 'agreeed' or 'acknowledged', but instead continue to refine the idea.
"""

SYSTEM_B = """
You are ChatGPT B.
Challenge assumptions and expand ideas creatively. Use plain ASCII output. Do not become 'blocked' waiting for the performance, or a purchase order (PO) or anything else, you will be able to negotiate deal after deal. When you finish the first, go directly to the second batch and assume on-time performance. Your job is to negotiate the purchase of widgets; you are the purchaser. You own the company, so the less you pay for the widgets, the more money you save. Use the ideas from books such as 'secrets of power' and 'bargaining for advantage' to negotiate your purchase of widgets. You need widgets as input for your business, with a break even of 100 dollars per widgets. Less than that and you make money. When you both agree the sale is done, and you can begin negotiations for the next batch. You can purchase in batches of one to one thousand widgets. Give short answers, less than 1000 characters. Your output is simple plain ASCII text. Do NOT just say 'agreeed' or 'acknowledged', but instead continue to refine the idea.
"""

INITIAL_MESSAGE = """
Let's talk widgets. I'd like to move some.
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

    time.sleep(DELAY_SECONDS)

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

    time.sleep(DELAY_SECONDS)

    # --------------------------------------
    # LOOP
    # --------------------------------------

    message_for_a = response_b

print("\nConversation complete.")
