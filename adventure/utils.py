import sys
import time

def typing_effect(text, delay=0.02) -> None:
        """Typing effect for the user."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()