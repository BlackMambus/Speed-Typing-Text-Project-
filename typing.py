import time
import random

# Sample sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing tests are a fun way to improve your speed.",
    "Python is a great language for beginners and pros alike.",
    "Practice makes perfect when it comes to typing fast.",
    "Artificial intelligence is transforming the world."
]

def typing_test():
    print("🎯 Welcome to the Speed Typing Test!")
    input("Press Enter when you're ready to begin...")

    # Choose a random sentence
    sentence = random.choice(sentences)
    print("\n📝 Type the following sentence as fast as you can:")
    print(f"\n\"{sentence}\"\n")

    input("Press Enter to start typing...")
    start_time = time.time()
    typed = input("\nStart typing here:\n")
    end_time = time.time()

    # Calculate results
    time_taken = end_time - start_time
    words = len(sentence.split())
    wpm = (len(typed.split()) / time_taken) * 60
    accuracy = sum(1 for a, b in zip(sentence, typed) if a == b) / len(sentence) * 100

    print("\n⏱️ Time Taken: {:.2f} seconds".format(time_taken))
    print("💨 Words Per Minute (WPM): {:.2f}".format(wpm))
    print("🎯 Accuracy: {:.2f}%".format(accuracy))

if __name__ == "__main__":
    typing_test()

