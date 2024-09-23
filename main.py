from organizer import Organizer

def main():
    directory = "/home/santosh/Downloads"

    try:
        file_organizer = Organizer(directory)
        file_organizer.organize_files()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()