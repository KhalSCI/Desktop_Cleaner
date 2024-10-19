import os
import shutil
import argparse
import pathlib
from tqdm import tqdm 
CATEGORIES = {
    'Photos': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.heic', '.webp', '.raw','.cr2', '.nef', '.arw', '.orf', '.rw2', '.dng'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm', '.mpeg', '.3gp', '.vob', '.m4v', '.rmvb', '.mpg', '.m2ts','.weba'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.doc','.odt', '.ods', '.odp', '.rtf', '.md','.tex','.log','.wpd','.pages'],
    'Applications': ['.exe', '.msi', '.apk', '.app', '.deb', '.dmg', '.pkg', '.rpm', '.jar','.bin', '.run'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz', '.iso', '.dmg','.z','.lz','.cab'],
    'Sounds': ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.aiff', '.alac', '.pcm', '.dsd','.opus'],
    'Code': ['.py', '.java', '.c', '.cpp', '.html', '.css', '.js', '.php', '.rb', '.go', '.ts', '.json', '.xml', '.swift', '.kt','.ini', '.yml', '.sql', '.pl','.lua','.cs','.r'],
    'Notebooks': ['.ipynb', '.rmd', '.rproj', '.rdata', '.rhistory', '.rprofile', '.rdata'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2','.eot','.fon'],
    '3D Models': ['.obj', '.fbx', '.stl', '.blend', '.dae', '.gltf', '.glb'],
    'Presentations': ['.ppt', '.pptx', '.key', '.odp','.pps','.ppsx'],
    'Spreadsheets': ['.xlsx', '.xls', '.ods', '.csv','.tsv','.gsheet','.xlr'],
    'Ebooks': ['.epub', '.mobi', '.azw3'],
    'Scripts': ['.sh', '.bat', '.ps1','.cmd','.vbs','.ahk','.swift','.jar'],
    'Shortcuts': ['.lnk'],
    'torrents': ['.torrent'],
}
logs = []
def get_category(file_extension):
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize(path):
    
    files = [f for f in os.listdir(path) if not os.path.isdir(os.path.join(path, f))]
    
    for filename in tqdm(files, desc="Organizing files", unit="file"):
        file_path = os.path.join(path, filename)

        file_extension = os.path.splitext(filename)[1]
        category = get_category(file_extension)

        category_folder = os.path.join(path, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        try:
            shutil.move(file_path, os.path.join(category_folder, filename))
        except (shutil.Error, OSError) as e:
            print(f"Error moving file '{filename}': {e}")
    
    
def format_input_path():
    user_input = input("Enter the path (e.g., ~/Downloads/test): ")
    formatted_path = os.path.expanduser(os.path.join(*user_input.split('/')))
    return formatted_path
def main():
    parser = argparse.ArgumentParser(description="Organize files on your desktop based on their extensions.")
    parser.add_argument("--path", type=str, default=os.path.expanduser("~/Desktop"),
                        help="Path to the desktop (default is the current user's desktop).")
    args = parser.parse_args()
    downloads_path = os.path.expanduser(os.path.join("~", "Downloads"))
    test_path = os.path.expanduser(os.path.join("~", "Downloads", "test"))
    desktop_path = args.path
    if not os.path.exists(desktop_path):
        print(f"The specified path '{desktop_path}' does not exist.")
        return

    while True:
        command = get_command()
        if command == 'desktop':
            organize(desktop_path)
            print("Desktop cleaned and files organized!")
        elif command == 'downloads':
            organize(downloads_path)
            print("Downloads cleaned and files organized!")
        elif command == 'path':
            temp_path = format_input_path()
            organize(temp_path)
        elif command == 'help':
            print_help()
        elif command == 'exit':
            print("Exiting...")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")

def print_help():
    print('--- Help ---')
    print(' Commands:')
    print(' desktop  - Organize files on the desktop')
    print(' downloads - Organize files in the downloads folder')
    print(' path - Organize files in the desired path')
    print(' help - Show this help message')
    print(' exit - Exit the program')

def get_command():
    return input('command> ').lower()
if __name__ == "__main__":
    main()