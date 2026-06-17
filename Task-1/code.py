import datetime

RESPONSES = {
    'hello': 'Hi there! I am RuleBot. I know 24 commands.',
    'hi': 'Hello! Type help to see what I can do.',
    'hey': 'Hey! How can I help you today?',
    'good morning': 'Good morning! Hope your day goes well.',
    'good evening': 'Good evening! What can I do for you?',
    'how are you': 'I am just code, but I am running perfectly.',
    'what is your name': 'I am RuleBot, a deterministic logic engine for Project 1.',
    'who are you': 'I am a rule-based chatbot using Python dictionaries.',
    'what can you do': 'I respond to 24 predefined commands using hash maps.',
    'time': 'I cannot tell live time, but your system clock can.',
    'date': 'Check your system date. I log today in chat_log.txt.',
    'who created you': 'You created me for Project 1: Rule-Based AI Chatbot.',
    'joke': 'Why do programmers prefer dark mode? Because light attracts bugs!',
    'thanks': 'You are welcome!',
    'thank you': 'Happy to help anytime!',
    'ok': 'Got it. Ask me another command.',
    'what is ai': 'AI means Artificial Intelligence. I am a simple rule-based example.',
    'what is a chatbot': 'A program that simulates conversation using rules or ML.',
    'what is python': 'Python is the programming language used to build me.',
    'bye': 'Goodbye! Session ended. Check chat_log.txt for the full trace.',
    'exit': 'Exit command received. Shutting down.',
    'quit': 'Quit command received. Goodbye!',
    'goodbye': 'Goodbye! Thanks for using RuleBot.'
}


COMMAND_LIST = [key for key in RESPONSES.keys()]
HELP_TEXT = "I understand these commands:\n" + "\n".join(f"- {cmd}" for cmd in sorted(COMMAND_LIST))
RESPONSES['help'] = HELP_TEXT

DEFAULT_RESPONSE = "I do not understand that. Type 'help' to see all my commands."
EXIT_COMMANDS = {'bye', 'exit', 'quit', 'goodbye'}

def main():
    print("RuleBot: Hello! I am a rule-based chatbot.")
    print("RuleBot: Type 'help' to know which commands I know. To end, type 'bye'.")
    
    with open('chat_log.txt', 'a', encoding='utf-8') as log_file:
        while True:
            raw_input = input("You: ")
            clean_input = raw_input.lower().strip()
            
            reply = RESPONSES.get(clean_input, DEFAULT_RESPONSE)
            print(f"RuleBot: {reply}")
            
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] You: {raw_input}\n")
            log_file.write(f"[{timestamp}] RuleBot: {reply}\n\n")
            log_file.flush()
            
            if clean_input in EXIT_COMMANDS:
                break

if __name__ == "__main__":
    main()