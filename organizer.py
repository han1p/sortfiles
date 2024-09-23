import os

class Organizer:
    def __init__(self, source_directory):
        self.source_directory = source_directory
        self.file_list = None
        self.file_types = {
            "Documents": [
                ".txt", ".md", ".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".csv",
            ],
            "Images": [
                ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".eps",
            ],
            "Audio": [
                ".mp3", ".wav", ".aac", ".flac", ".ogg",
            ],
            "Videos": [
                ".mp4", ".avi", ".mov", ".mkv", ".wmv",
            ],
            "Archives": [
                ".zip", ".tar", ".gz", ".rar",
            ],
            "Executables": [
                ".exe", ".bat", ".sh", ".app", ".msi",
            ],
            "Web Files": [
                ".html", ".htm", ".css", ".js", ".json", ".xml",
            ],
            "System Files": [
                ".ini", ".conf", ".log",
            ],
        }

    def get_files(self):
        self.file_list = [file for file in os.listdir(self.source_directory) if os.path.isfile(os.path.join(self.source_directory, file))]
    
    def check_file_extension(self, file):
        return os.path.splitext(file)[1].lower()
    
    def get_file_category(self, file_extension):
        for category, extensions in self.file_types.items():
            if file_extension in extensions:
                return category
        return "Unknown"
    
    def get_destination_dir(self, file, category):
        destination_path = os.path.join(self.source_directory, category)
        if not os.path.isdir(destination_path) and category!= "Unknown":
            self.create_dir(destination_path)
        return os.path.join(destination_path, file)
    
    @classmethod        
    def create_dir(cls, destination_dir):
        return os.makedirs(destination_dir, exist_ok = True)
    
    def move_files(self, source, destination):
        try:
            os.rename(source, destination)
        except OSError as e:
            print(f"Error: {str(e)}")

    def organize_files(self):
        self.get_files()
        for file in self.file_list:
            try:
                file_extension = self.check_file_extension(file)
                category = self.get_file_category(file_extension)
                if category == "Unknown":
                    continue
                current_file_path = os.path.join(self.source_directory, file)
                destination_file_path = self.get_destination_dir(file, category)
                self.move_files(current_file_path, destination_file_path)
            except Exception as e:
                print(f"Error organising file {file}: {e}")




