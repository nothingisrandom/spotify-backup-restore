# Spotify Backup and Restore (WIP)

This is a simple Python Project to make backup of your Spotify Liked songs and Restoring them to a new account for whatever reasons you might have. The programs need some prerequisites and they have limitations too. I'll try to explain everything here.

Note: Currently only Backup Script is ready and uploaded on the Repository. I still need to make the Restoration script (any help for it would be awesome since I don't get much time)

## Requirements

- This Project
  - Either use `git clone` to clone it to your computer
  - Or download the Project using the button provided above and then extract the zip somewhere
- Python 3 - https://www.python.org/downloads/
  - Make sure you do install pip and python3 both and also add them to path if they weren't added automatically (you will get an option to add them to path when you are installing python)
- Firefox Browser - https://www.mozilla.org/en-US/firefox/
  - Currently the program only supports Firefox and I may or may not add a support for other browsers in future 
- Geckodriver - https://github.com/mozilla/geckodriver/releases
  - Make sure to check if the Geckodriver you are downloading is compatible with the version of Firefox
  - After downloading the Geckodriver, rename it to `geckodriver.exe` if not already and move it to the project folder
  - Alternatively, you can create a folder somewhere in your PC and move the `geckodriver.exe` into that folder and;
  - Add the `geckodriver.exe` to Path using this guide: [Here's how to add a program to Path](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)
- Selenium Library
  - Type `pip install selenium` in command prompt to install it

## How to Use the Program + Working

A simple explanation for the usage of the program and how the program is working:

### Backup Working

- The Backup Script is basically extracting all the names of the songs and their artists in a text file one song per line. The output of the program would be of this format in the text file: `Song Name | Artist Name(s)`
- I am not a hundred percent sure but when you run the script, you might get errors if your resolution is not 1920x1080 (can be more or less). I am not sure because it depends on screen to screen and user to user that how their Firefox will look.
- This is important because on a 1080p screen with 100% Scale ratio in display settings, the Spotify webpage loads 49 songs at a time. Its somewhat of a container, it only loads 49 songs in it at a time. Each time you scroll, the songs loaded change.
- So, let's say song A is on number 1 in the current container of 49 and B is the 49th Song, then if you scroll to the 49th song using the Selenium library, the song B is now on the 18th Number of the new 49 Songs.
- This is why in the loops, I extracted first 49 songs, then after the first 49, I scroll to the next 49th song and then start extracting from the 19th Element to the 49th Element.
- I know this is a wrong approach and I currently haven't thought of a better way for them. Also, just to let you know, I tested it on my account with 504 songs liked. For some reason, out of 504 songs, 2 didn't get into the text file. I will try to fix this when I can. If you have worked on Selenium in Python before, do let me know if you find the issue.
- So, all the screen resolution mumbo jumbo was because I am not sure if the case will be the same for everyone. I am open for suggestions/edits. Unfortunately I can't say this script will work for everyone but if Spotify loads those 49 Songs at the same time, then you're good to go.

### Backup Usage

1. I am assuming you have installed all the requirements at this point
2. Open `credentials.py` enter your email and password inside the quotes
3. Open a command prompt inside the Project folder and run the script using the command `python backup.py`
4. Hopefully if everything goes right, a Firefox window will pop up, log your account in, and start exporting. If you don't see any errors in the command line (CMD/Powershell) then you can open the new text file created in the Project Folder and find all your songs along with the artist names

### Restore Working + Usage [WIP]

Currently there is no Restoration Script, I would make it if I get some time and if you can make it, here is what we have to do:

- Open Firefox using Geckodriver
- Login to Account
- Open the Backup text file in readline mode
- Flip the List (So that the Order they are added is same as previous account)
- Read current line, split using the separator ' | '
- Click the search button on Spotify
- Enter Song name  + " " + Artist name
- Select the first one
- Click the button to Add to liked songs

Should be pretty easy to do and maybe I will do in future

## Possible Issues

- If liked songs are less than 49, you WILL get error. I am assuming you have more than at least 60-70 songs in your Saved/Liked Songs
- Different resolutions might have different count of songs per container (talked about this in Backup Working section above) so if one container doesn't have 49 songs at a time, I don't really know what will happen
- The program is far from being 100% working condition. The container issue needs to be fixed, I need to make a way to find the number of songs the current container has instead of just saying it has 49.