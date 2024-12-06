# Function to read file
def read_file(input_file):
    try:
        with open(input_file, 'r') as f: # Open the file in 'read' mode
            content = f.read()  # Read the contents of the file
        return content

    except:
        print("Couldn't open file")  # Error handling

# Function to process text into sentences & words
def process_text(text):
    sentences = text.splitlines()  # Split text into sentences
    words = text.split()  # Split text into words by spaces
    return sentences, words

# Function to find word frequency
def word_frequency(words):
    frequency = {}  # Create an empty dictionary (key-value pairs storage)
    unique_word = []
    for word in words:
        if word in frequency:  # Check if the word already exists in the dictionary
            frequency[word] += 1  # Increment the count
        else:
            frequency[word] = 1  # Initialize the count for the new word
    for word, count in frequency.items(): # Unique words list
        if count == 1:
            unique_word.append(word)
    return frequency, unique_word


import json

# Function to write output to a file
def write_output(output, output_file):
    with open(output_file, 'w') as f:  # Open file in write mode
        json.dump(output, f, indent=3)  # Write the output as JSON with indentation

# Main function to combine all functions
def main(input_file, output_file):
    text = read_file(input_file)  # Read content from input file
    if text is None:
        print("File processing aborted.")
    else:
        print("File content successfully read.")  # Exit if reading the file failed
    
    sentences, words = process_text(text)  # Process text into sentences and words
    frequency, unique_word = word_frequency(words)  # Frequency of each word
    
    # Output dictionary with results
    output = {
        'Word frequency': frequency,
        'Unique words list': unique_word,
        'Sentence count': len(sentences),  # Sentence count
        'Word count': len(words),  # Word count
        'Unique word count': len(unique_word),  # Unique word count
    }
    
    write_output(output, output_file)  # Write output to the output file

# Call main function
if __name__ == "__main__":
    main('../main_task/data/sample_inputs/test_text.txt',
         '../main_task/data/outputs/processed_output.json')    # Input file path, Output file path

