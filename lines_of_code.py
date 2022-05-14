import sys
import os

# Filenames to avoid
folder_names_to_avoid = [
    '__pycache__', 'migrations', 'font-awesome', 'images', 'bootstrap',
    'media', 'project_screenshot', 'fontawesome-free', 'fonts',
    'screenshots', 'log_images', '.git', 'img', 'fontawesome-free-5.14.0-web'
]

files_to_avoid = [
    'bootstrap.min.css', 'bootstrap.min.js', 'bootstrap.js', 'parts.html',
    'bootstrap.css', 'bootstrap.css.map', 'jquery.min.js', 'pinstrap.html',
    'bootstrap.min.js.map', 'my_jQuery.js', 'Procfile', 'aos.js', 'aos.css',
    '.env', '.gitignore', 'README.md', 'slider_range.js', 'popper.min.js',
    'pinterest-like.html', 'jquery.min.js', 'jquery-3.4.1.slim.min.js',
    'masonry.min.js', 'eNaira_Design_Paper.pdf', 'font-awesome.min.css',
    'emoji-button.min.js', 'Aptfile', 'cert.crt', 'cert.key.key', 'tipsntricks.html',
    'test.html', 'scrambler.py', 'grouper.py', 'test.py', 'chart.js', 'readme.md'
]

bad_extensions = [
    '.mp4', '.png', '.jpg', '.wav', '.mp3', '.txt', '.sqlite3', '.db', '.gif',
    '.json', '.iml', '.key'
]

# Using SYS

def count_lines():
    ''' I am using the sys module for this for simplicity instead of the click module'''
    try:
        folder_path = sys.argv[1]
        if folder_path == '--help':
            print()
            print('#------------------------------#')
            print()
            print('Enter python loc.py folder-path')
            print(r'Eg. python loc.py C:\Users\Folder')
            print()
            print('#------------------------------#')
            print()
            return
        if len(sys.argv) > 1:
            folder_path = ' '.join(sys.argv[1:])
        lines_of_code = 0

        # check if path exists
        if os.path.exists(folder_path):
            for root, folders, filenames in os.walk(folder_path):
                if not any(folder_names_to_avoid in root for folder_names_to_avoid in folder_names_to_avoid):
                    for filename in filenames:
                        if not filename in files_to_avoid and not any(bad_extensions in filename for bad_extensions in bad_extensions):
                            # print(root, filename)
                            with open(f'{root}\{filename}', encoding='utf-8') as fp:
                                contents = fp.readlines()
                                contents = [i.rstrip().upper() for i in contents]
                            lines_of_code += len(contents)
            print()
            print('#------------------------------#')
            print()
            print(f'Total lines of codes ==> {lines_of_code}')
            print()
            print('#------------------------------#')
            print()
        else:
            print()
            print('#------------------------------#')
            print()
            print('ERROR')
            print('Folder path does not exist')
            print()
            print('#------------------------------#')
            print()
            
    except IndexError:
        print('No folder path specified')
    

if __name__ == '__main__':
    count_lines()
