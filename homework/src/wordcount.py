## wordcount.py

from homework.src._internals.parse_args import parse_args

def main():
    """
    Main function to count words in a file.
    """

    input_folder, output_folder = parse_args()

    print(f"Processing files from {input_folder} to {output_folder}")


if __name__ == "__main__":
    main()
    
    
