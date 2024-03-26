def write_to_file():
  """
  Creates a new text file "my_file.txt" and writes content to it.
  """
  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line of text.\n")
      file.write("Here's some data: 42\n")
      file.write("Another line with a string and a number: 3.14\n")
      print("Successfully wrote content to my_file.txt")
  except (IOError, OSError) as e:
    print(f"Error writing to file: {e}")

def read_from_file():
  """
  Opens "my_file.txt" and reads its contents, displaying them on the console.
  """
  try:
    with open("my_file.txt", "r") as file:
      content = file.read()
      print("Contents of my_file.txt:\n", content)
  except FileNotFoundError:
    print("File 'my_file.txt' not found. Please create it first.")
  except (IOError, OSError) as e:
    print(f"Error reading from file: {e}")

def append_to_file():
  """
  Opens "my_file.txt" in append mode and writes additional lines.
  """
  try:
    with open("my_file.txt", "a") as file:
      file.write("Appending some more text...\n")
      file.write("Line 4 with new information.\n")
      file.write("The final line: Today is a good day!\n")
      print("Successfully appended content to my_file.txt")
  except (IOError, OSError) as e:
    print(f"Error appending to file: {e}")

if __name__ == "__main__":
  write_to_file()
  read_from_file()
  append_to_file()
  read_from_file()
