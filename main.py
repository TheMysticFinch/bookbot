def get_book_text(file_path):
    
    with open(file_path) as f:
        files_contents = f.read()

    return files_contents

def get_number_words(file_path):
    
    with open(file_path) as f:
        files_contents = f.read()
        word_count = len(files_contents.split())

    return word_count

def main():
    
    frankenstein = get_book_text("books/frankenstein.txt")
    print(frankenstein)

    frankenstein_wc = get_number_words("books/frankenstein.txt")
    print(frankenstein_wc)

main()
    
    