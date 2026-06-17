# RULE-BASED AI CHATBOT (RuleBot)

## 1. PROJECT OVERVIEW

RuleBot is a deterministic, rule-based chatbot developed using Python. It demonstrates the core logic behind AI systems by using a dictionary-based knowledge base instead of machine learning algorithms.

The chatbot performs instant response retrieval using hash maps (Python dictionaries), ensuring:

* O(1) response lookup time
* Zero hallucination risk
* Fully predictable behavior
* Complete traceability of decisions

This project satisfies the requirements of **Project 1: The Logic Skeleton**, demonstrating how intelligent systems can be built using transparent rule-based logic.

---

## 2. FEATURES

### Continuous Input Loop

* Uses a `while True` loop to allow ongoing user interaction.

### Input Sanitization

* Converts user input to lowercase using `.lower()`
* Removes extra spaces using `.strip()`
* Example:

  * "HELLO"
  * " hello "
  * "Hello"

  All are interpreted as: `hello`

### Knowledge Base

* Uses a dictionary containing 24+ predefined intents and responses.

### Fallback Mechanism

* Unknown inputs trigger a default response using dictionary `.get()`.

### Exit Commands

The chatbot exits cleanly when the user enters:

* bye
* exit
* quit
* goodbye

### Efficient Processing

* Dictionary and set lookups provide constant-time O(1) performance.

### White-Box Traceability

* Every interaction is logged to `chat_log.txt`.
* Logs include timestamps and chatbot decisions.

---

## 3. HOW TO RUN

### Prerequisites

* Python 3.x installed on your system

### Steps

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

```bash
python main.py
```

4. Start chatting with the bot.
5. Type `help` to see all available commands.
6. Type `bye` to end the session.

---

## 4. PROJECT STRUCTURE

```text
rule_based_chatbot/
│
├── main.py         # Main chatbot logic
├── chat_log.txt    # Auto-generated conversation logs
└── README.txt      # Project documentation
```

---

## 5. WORKING PRINCIPLE (IPO MODEL)

### Input

The chatbot accepts user input using:

```python
input("You: ")
```

### Process

1. Input is cleaned using:

```python
clean_input = raw_input.lower().strip()
```

2. Response is retrieved using:

```python
RESPONSES.get(clean_input)
```

This performs an O(1) dictionary lookup.

### Output

The chatbot displays the corresponding response:

```python
print(f"RuleBot: {reply}")
```

---

## 6. KNOWLEDGE BASE

The chatbot understands more than 24 predefined commands.

### Greetings

* hello
* hi
* hey
* good morning
* good evening

### Bot Information

* how are you
* what is your name
* who are you
* who created you

### Utility Commands

* help
* time
* date
* what can you do

### Educational Commands

* what is ai
* what is a chatbot
* what is python

### Fun Commands

* joke
* thanks
* ok

### Exit Commands

* bye
* exit
* quit
* goodbye

Use the `help` command inside the chatbot to view the complete sorted command list.

---

## 7. KEY CONCEPTS DEMONSTRATED

### 1. Hash Maps

Python dictionaries are used for fast O(1) response retrieval.

### 2. Deterministic Logic

The same input always produces the same output.

### 3. Scalable Design

Avoids large `if-elif` chains by using a centralized dictionary structure.

### 4. White-Box AI

Every chatbot decision is transparent and traceable through logs.

### 5. Input Processing

Handles variations in capitalization and spacing through sanitization.

---

## 8. FUTURE EXTENSIONS

This chatbot represents the foundational layer of an AI system.

Possible enhancements include:

* Natural Language Processing (NLP)
* Intent classification
* Sentiment analysis
* Database integration
* Voice interaction
* Hybrid AI architecture

In a hybrid system, unknown user queries could be forwarded to a Large Language Model (LLM), combining:

* Rule-based reliability
* Generative AI flexibility

---

## 9. LEARNING OUTCOMES

By developing this project, the following concepts are demonstrated:

* Python programming fundamentals
* Dictionary and set data structures
* Hash map implementation
* Input sanitization
* File handling and logging
* Algorithmic efficiency
* Rule-based AI architecture
* White-box system design

---


**Objective:** Build the foundational structure that supports intelligent decision-making using transparent and deterministic rules.
