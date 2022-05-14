# Utility Script

These are simple scripts for solving my simple problems 😀😉😋

## No. 1 -> Lines of Code

I wanted to find out the lines of code I had in my Django application and I had some difficulty with some tools online so I decided to write my own script that does solves this problem. The script contains names of folders, files and extensions to avoid eg. __pycache__, .git, media, bootstrap.css, jquery.min.js and extensions like .mp4, .png, .wav, .mp3 etc. The script takes an argument of the folder path containing the code you want counted.
Example snippet:

```buildoutcfg
PS C:\Users\Python Scripts> python lines_of_code.py C:\Users\Documents\WatchNLearn
Total lines of codes ==> 4223
```

## No. 2 -> Word Puzzle Solver

I once encountered a word game that scrambles letters of a word and requires you to find words that can be formed from the scrambled letters. Eg. PNHOTY can form toy, ton, not, phony, typo, python etc. After using up all my hints, I had to pay to get more hints. I didn't want to pay to play a game that is supposedly free hence this script😂😂. All you have to do is enter the script's name, the letters and how many letter words you want formed
Example snippet:

```buildoutcfg
PS C:\Users\Python Scripts> python word_finder.py pnhoty 6
['phyton', 'python', 'typhon']
```

## No. 3 -> Renamer

Most of the time I download video or audio using the site y2mate.com, I get the filename as y2mate.com - name_of_file.ext. I do not want to have to rename each download individually so I created this script to go through as deep (folder inside folder) as it takes through a folder to do the renaming for me.
Example snippet:

```buildoutcfg
PS C:\Users\Python Scripts> python renamer.py C:\Users\existingpath
Successful renaming 😀

PS C:\Users\Python Scripts> python renamer.py C:\Users\somebadpath
Folder path does not exist
```

## No. 4 -> Subtitle Adder

VLC has this beautiful feature that automatically finds the subtitle for a video so long as the subtitle name is the same as the video name (excluding the extension). When I download subtitles for a series, I don't want to have to drag subtitles for each episode so I wrote this script. I just copy the subtitles into the video folder and run this script. All I need do next is press play all 😎😎
Example snippet:

```buildoutcfg
PS C:\Users\Python Scripts> python subtitle_adder.py C:\Users\videofolderpath
Subtitles renamed. Enjoy 😀
```
