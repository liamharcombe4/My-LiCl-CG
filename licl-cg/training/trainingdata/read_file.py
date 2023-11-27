import numpy as np

def read_raw_file(file_path):
    """
    Reads and prints the contents of a .raw file.

    :param file_path: Path to the .raw file
    """
    # Assuming the data type is float32
    data = np.fromfile(file_path, dtype='float32')

    # Print the data
    print(data)

if __name__ == "__main__":
    file_path = input("Enter the path of the .raw file: ")
    read_raw_file(file_path)
