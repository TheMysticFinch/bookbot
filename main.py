def get_book_text(file_path):
    
    with open(file_path) as f:
        files_contents = f.read()

    return files_contents

def main():
    
    frankenstein = get_book_text("~/projects/bookbot/books/frankenstein.txt")
    print(frankenstein)


main()
    
    