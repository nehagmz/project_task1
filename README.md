Text Processing Task

Project Overview:
-----------------
This project reads a text file, processes its content to split it into sentences and words, 
counts the frequency of each word, identifies unique words (words occurring only once), 
and then saves the output to a JSON file.

Setup and Installation:
------------------------
1. Python version requirement: Python 3.x
2. Clone the repository to your local machine using Git:
   git clone https://github.com/your-username/text-processing-task.git
3. Navigate to the project directory:
   cd text-processing-task
4. No additional dependencies are required for this project.

How to Run the Script:
----------------------
1. Ensure your input file (test_text.txt) is in the project directory.
2. Run the Python script `text_processor.py` using the command:
   python text_processor.py

Usage:
------
- Input file format: A plain text file (.txt) with one or more sentences.
- Output format: The output will be saved in `processed_output.json` in JSON format, 
  which contains:
    - Word frequency: A dictionary of words and their counts.
    - Unique words list: A list of words that appear only once.
    - Sentence count: The number of sentences in the text.
    - Word count: The total number of words in the text.

Example Command:
----------------
python text_processor.py

Sample Output:
--------------
The script generates an output file (`processed_output.json`) in the following format:
{
    "Word frequency": {"word1": 3, "word2": 1, "word3": 2},
    "Unique words list": ["word2"],
    "Sentence count": 5,
    "Word count": 10
}

Features:
---------
- Reads a plain text file and splits the content into sentences and words.
- Counts the frequency of each word and identifies unique words.
- Generates a JSON output with word frequencies, unique words, sentence count, and word count.

Development Decisions:
----------------------
- The script processes the input text by splitting it into sentences using line breaks and words using spaces.
- The word frequency is counted using a dictionary, and unique words are determined based on their occurrence.

Challenges Faced:
-----------------
- Handling different input file formats and ensuring robust error handling for file reading.
- Managing word frequency counting efficiently while keeping track of unique words.
- Punctuation Handling: Words in the text may be followed by punctuation (e.g., commas, periods), which can affect word counting.
