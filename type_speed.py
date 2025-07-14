import time

sentence = "The quick brown fox jumps over the lazy dog."
print("Type the following sentence as fast as you can:")
print(f"\n👉 {sentence}\n")

input("Press Enter to start...")

start = time.time()
typed = input("Start typing: ")
end = time.time()

time_taken = end - start
word_count = len(sentence.split())
accuracy = sum(1 for a, b in zip(sentence, typed) if a == b) / len(sentence) * 100

wpm = (len(typed.split()) / time_taken) * 60

print(f"\n⏱️ Time taken: {time_taken:.2f} seconds")
print(f"⚡ Typing Speed: {wpm:.2f} words per minute")
print(f"🎯 Accuracy: {accuracy:.2f}%")
