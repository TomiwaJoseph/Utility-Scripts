import os
import sys

def rename():
    try:
        folder_path = sys.argv[1]
        if len(sys.argv) > 1:
            folder_path = ' '.join(sys.argv[1:])

        iteration_count = 0
        if os.path.exists(folder_path):
            for root, dirnames, filenames in os.walk(folder_path):
                for file in filenames:
                    all_mp4names = [i[:-4] for i in filenames if i.endswith("mp4")]
                    if file.endswith("srt"):
                        dst = all_mp4names[iteration_count] + '.srt'
                        os.rename(os.path.join(root,file), os.path.join(root,dst))
                        iteration_count += 1
            print()
            print("...")
            print('Subtitles renamed. Enjoy 😀')
            print()
        else:
            print('Folder path does not exist')
    except IndexError:
        print('No folder path specified')


if __name__ == "__main__":
    rename()
