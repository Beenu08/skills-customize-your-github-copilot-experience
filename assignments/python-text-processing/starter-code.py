# Python Text Processing Assignment
# Starter code for text processing tasks

def word_frequency_counter(input_file, output_file):
    """
    Task 1: Count word frequencies from input_file and write to output_file
    """
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        
        # TODO: Process text and count words
        # Convert to lowercase, remove punctuation, split into words
        # Count frequencies using a dictionary
        # Sort and write to output_file
        
        pass
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

def text_search_replace(input_file, output_file, search_term, replace_term):
    """
    Task 2: Search and replace in text file
    """
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        
        # TODO: Replace search_term with replace_term
        # Count replacements
        # Write to output_file
        
        pass
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

def text_statistics(text):
    """
    Task 3: Analyze text statistics
    """
    # TODO: Calculate characters, words, average word length, sentences
    pass

# Example usage (uncomment to test)
# word_frequency_counter('input.txt', 'word_counts.txt')
# text_search_replace('input.txt', 'output.txt', 'old', 'new')
# stats = text_statistics("This is a sample text.")
# print(stats)