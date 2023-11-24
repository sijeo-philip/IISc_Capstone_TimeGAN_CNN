import os
import sys
import shutil
import csv


def organize_files(metaFilePath, dataFilePath):
    #Read the text file
    with open(metaFilePath, 'r') as file:
        lines = csv.DictReader(file)

        for row in lines:
            source = row['FileName']
            destination = row['Class']
            # print("File and folder name is {}".format(row))

        # Check if there are at least 2 values on each line
            if len(row) >= 2:
                source_file = dataFilePath+source
                folder_name = os.path.dirname(dataFilePath)+'/'+destination
                print("Source File is {} and Folder Name is {}\n".format(source_file, folder_name))

            #create the destination folder if it doesn't exist
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)

                destination_file = os.path.join(folder_name)
                print("The Destination Folder is {}\n".format(destination_file))
                try:
                    shutil.move(source_file, destination_file)
                    print("File: {} is moved to {}".format(source_file, destination_file))
                except Exception as e:
                    print(f"Exception details: {e}")


            else:
                print("Invalid line format : {line}")

    print("Files organized successfully!")

if __name__ == "__main__":
    #Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python data_file_sort.py <meta file path> <source file path>")
        sys.exit(1)

    #Get the file path from the command line arguments
    meta_file_path = sys.argv[1]
    data_file_path = sys.argv[2]

    # Call the funtion with the provided command line arguments
    print("Meta File Path is {} and Data File Path is {}".format(meta_file_path, data_file_path))
    organize_files(meta_file_path, data_file_path)
