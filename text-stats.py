from flask import Flask, request

app = Flask(__name__)

# Function to count words
def count_words(text):
  return len(text.split())

# Function to calculate average word length
def avg_word_length(text):
  words = text.split()
  if not words:
    return 0  # Handle empty input
  return sum(len(word) for word in words) / len(words)

# Function to find most common word
def most_common_word(text):
  words = text.lower().split()
  word_counts = {}
  for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
  most_common = max(word_counts, key=word_counts.get)
  return most_common

# Endpoints
@app.route("/", methods=["POST"])
def handle_text():
  text = request.data.decode("utf-8")
  word_count = count_words(text)
  avg_length = avg_word_length(text)
  most_common = most_common_word(text)
  return f"Word count: {word_count}, Average word length: {avg_length:.2f}, Most common word: {most_common}"

if __name__ == "__main__":
  app.run(debug=True)