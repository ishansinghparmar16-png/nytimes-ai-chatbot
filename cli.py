"""
Simple CLI interface for testing the NY Times AI Chatbot.
"""
from orchestrator import run_chatbot
import sys


def main():
    """Run the chatbot from command line."""
    print("\n" + "=" * 80)
    print("NY TIMES AI CHATBOT - Command Line Interface")
    print("=" * 80)
    print("\nType your query below (or 'quit' to exit)")
    print("-" * 80)
    
    while True:
        try:
            user_query = input("\n📝 Your query: ").strip()
            
            if not user_query:
                continue
                
            if user_query.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye!\n")
                break
            
            # Run the chatbot
            result = run_chatbot(user_query)
            print("\n" + result + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()

