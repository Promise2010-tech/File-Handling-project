def main():
    try:
        input_file = input("Enter the name of the file to read: ")
        with open(input_file, 'r') as file:
            content = file.read()
        modified_content = content.upper()
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        print(f"Modified content written to {output_file}")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read.")

if __name__ == "__main__":
    main()