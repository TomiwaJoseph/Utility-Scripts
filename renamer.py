import os
import sys

def rename():
    try:
        folder_path = sys.argv[1]
        if folder_path == '--help':
            print('#------------------------------#')
            print()
            print('Enter python renamer.py folder-path')
            print(r'Eg. python renamer.py C:\Users\Folder')
            print()
            print('#------------------------------#')
            print()
            return
        if len(sys.argv) > 1:
            folder_path = ' '.join(sys.argv[1:])
        
        to_remove = 'y2mate.com - '

        # Search in folder content and stuff...
        if os.path.exists(folder_path):
            for root, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    if filename.startswith(to_remove):
                        dst = filename[len(to_remove):]
                        os.rename(os.path.join(root,filename), os.path.join(root,dst))
            print()
            print("...")
            print('Successful renaming 😀')
            print()
        else:
            print('Folder path does not exist')
    except IndexError:
        print()
        print('No folder path specified')
        print('#------------------------------#')
        print()
        print('Enter python renamer.py folder-path')
        print(r'Eg. python renamer.py C:\Users\Folder')
        print()
        print('#------------------------------#')
        print()


if __name__ == "__main__":
    rename()
