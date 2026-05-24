# AIExperiments

By Matthew Heusser - Matt.Heusser@gmail.com

Figuring out how good AI really is by letting it talk to another agent

A few years ago, the internet was all kerfluffle that two AI bots designed to negotiate had developed their own trading language that the scientists could not understand, so Meta shut down the program. ( https://www.thesun.co.uk/tech/science/4141624/facebook-robots-speak-in-their-own-language/ ).

I suspected that the systems had simply devolved to gibberish. This was, of course, exactly what happened. ( https://medium.com/data-science/the-truth-behind-facebook-ai-inventing-a-new-language-37c5d680e5a7 ).

The consequences of this is simple. It's sort of a new turing test, in a way. When one computer talks to another, any actual insight, long-term, anything new, anything true, anything beautiful, would be an indicator of real progress in AI.

That kerfullel happened in 2017, before ChatGPT was released to the world. Now, anybody can design such an experiment by cutting and pasting between two chatGPT windows. Or, with a little work, two API's.

The tools in this directory make is super easy. Configure your OpenAI subscription to use the API, pre-charge some credits, load the API key in the shell as a variable, change the first prompt to the API and let it fly! 

---

# Quick Start

## Requirements

* Python 3.10+
* OpenAI Python SDK

Install the OpenAI library:

```bash
pip install openai
```

---

# API Key Setup

Linux/macOS:

```bash
export OPENAI_API_KEY="your-api-key"
```

Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your-api-key"
```

Create an API key here:

https://platform.openai.com/

---

# Running A Script

```bash
python3 dual_chat.py
```

or:

```bash
python3 negotiation_chat.py
```

Conversation logs are written to:

```text
conversation_log.txt
```

---

# Core Structure

The scripts all follow roughly this pattern:

```python
chat_a = [
    {"role": "system", "content": SYSTEM_A}
]

chat_b = [
    {"role": "system", "content": SYSTEM_B}
]
```

Each AI gets:

* its own memory/history
* its own personality
* its own goals
* its own constraints

The agents then talk to each other in a loop.

---

# The Most Important Variables

Most experimentation happens by editing these sections.

---

## MODEL

```python
MODEL = "gpt-5.1"
```

Change the model to compare:

* cost
* speed
* reasoning
* creativity
* conversational stability

---

## SYSTEM_A

```python
SYSTEM_A = """
...
"""
```

This defines:

* personality
* objectives
* incentives
* speaking style
* negotiation strategy
* worldview
* behavioral constraints

Examples:

* negotiator
* philosopher
* teacher
* scientist
* con artist
* therapist
* cooperative agent
* adversarial agent

Small wording changes can dramatically change behavior.

---

## SYSTEM_B

```python
SYSTEM_B = """
...
"""
```

The second agent does not need to match the first.

Interesting experiments often come from conflicting goals:

* buyer vs seller
* optimist vs pessimist
* truthful vs deceptive
* creative vs analytical
* short-term vs long-term thinking

---

## INITIAL_MESSAGE

```python
INITIAL_MESSAGE = """
...
"""
```

This starts the simulation.

Try:

* negotiation openings
* philosophical questions
* survival scenarios
* political debates
* business strategy
* collaborative design tasks

The opening prompt heavily influences the trajectory of the conversation.

---

## MAX_TURNS

```python
MAX_TURNS = 200
```

Longer conversations can produce:

* convergence
* repetition loops
* role drift
* both parties waiting on something in the external "real" world
* strange recursive behavior

---

## DELAY_SECONDS

```python
DELAY_SECONDS = 1
```

Useful for:

* rate limiting
* watching conversations live
* reducing API burst usage
* Getting around openAI tokens per second maximums

---

# API Styles

This repository contains examples using both major OpenAI Python SDK patterns.

---

## Responses API

```python
response = client.responses.create(
    model=MODEL,
    input=history
)
```

Response text:

```python
response.output_text
```

Advantages:

* newer API
* simpler structure
* cleaner output handling

---

## Chat Completions API

```python
response = client.chat.completions.create(
    model=MODEL,
    messages=history,
    temperature=0.5,
    frequency_penalty=0.8,
    presence_penalty=0.3
)
```

Response text:

```python
response.choices[0].message.content
```

Advantages:

* explicit sampling controls
* easy parameter experimentation
* familiar interface

---

# Sampling Parameters

The script negotiation_chat_conrolled.py exposes additional tuning parameters designed to prevent the most common initial breakdowns of these scripts.

---

## Temperature

```python
temperature=0.5
```

Higher values:

* more creative
* less stable
* more surprising

Lower values:

* more deterministic
* more repetitive
* more predictable

---

## Frequency Penalty

```python
frequency_penalty=0.8
```

Reduces repeated phrases and repetitive loops.

Very useful for long-running conversations. Without this, the app will tend to get stucks in repetitive loops.

---

## Presence Penalty

```python
presence_penalty=0.3
```

Encourages the introduction of new ideas and topics. Again, prevents infinite mutual agreement.

---

# Logging

Conversations are written to:

```text
conversation_log.txt
```

This makes it easier to:

* analyze behavior
* compare prompts
* study negotiation patterns
* review long-term drift

---

# Notes



---

# Suggested .gitignore

```gitignore
__pycache__/
*.pyc
.env
conversation_log.txt
```

---

# Suggested requirements.txt

```text
openai>=1.0.0
```

---

# License

MIT License

