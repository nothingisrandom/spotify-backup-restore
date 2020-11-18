# Imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from credentials import email,password

# Creating Driver and Opening Spotify
driver = webdriver.Firefox()
driver.get('https://open.spotify.com/')

# Functions
def getElement(xpath): # Just for making the code smaller
    return driver.find_element_by_xpath(xpath)

def login(): # Logging into Spotify and Going to Liked Songs
    getElement('//*[@id="login-username"]').send_keys(email)
    getElement('//*[@id="login-password"]').send_keys(password)
    getElement('//*[@id="login-button"]').click()
    sleep(5) # Adding sleep to make sure login is complete
    driver.get('https://open.spotify.com/collection/tracks')

def scroll_to_element(xpath): # It is what it says, scrolls to the element (of xpath provided)
    element = getElement(xpath)
    driver.execute_script("arguments[0].scrollIntoView();", element)

def next_exists(xpath): # Checks if the Element exists (using xpath provided)
    try:
        getElement(xpath)
        return True
    except Exception:
        return False

def artist_name(n): # Extracts all the names of Artists of current song
    xpath1 = ['/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[',']/div/div[2]/div/span']
    xpath2 = ['/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[',']/div/div[2]/div/span[2]']
    name = getElement(xpath1[0] + str(n) + xpath1[1]).text
    if name == "E": # If the song is Explicit, the output comes E instead the name, so a separate xpath is used to get the name
        return getElement(xpath2[0] + str(n) + xpath2[1]).text
    else: # Non-explicit songs will return name with the xpath1
        return name

def print_name(filename): # All main work is being done here
    # Will give error if number of songs liked are less than 49 | Need to fix this!!
    # The write functions are encoding just in case any song is named in any other language than English
    name_xpath = ['/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[',']/div/div[2]/div/div']
    for i in range(1,50): # The first 49 Songs are Extracted directly
        filename.write((getElement(name_xpath[0] + str(i) + name_xpath[1]).text + ' | ' + artist_name(i) + "\n").encode('utf-8'))
    scroll_to_element(name_xpath[0] + '49' + name_xpath[1]) # Explained why in the Readme
    sleep(2) # Giving the website time to load (increase if you have a slower connection)
    while next_exists(name_xpath[0] + '49' + name_xpath[1]): # Checking if we have 49 Elements after the current one
        for i in range(19,50): # Explained why in Readme
            filename.write((getElement(name_xpath[0] + str(i) + name_xpath[1]).text + ' | ' + artist_name(i) + "\n").encode('utf-8'))
        scroll_to_element(name_xpath[0] + '49' + name_xpath[1])
        sleep(2) # Giving the website time to load (increase if you have a slower connection)
    n = 19 # Explained why in Readme
    while next_exists(name_xpath[0] + str(n) + name_xpath[1]): # Here on, all the songs are in current 'frame of reference' for the lack of better word thus while loop
        filename.write((getElement(name_xpath[0] + str(n) + name_xpath[1]).text + ' | ' + artist_name(n) + "\n").encode('utf-8'))
        n+=1

def main(): # Self explanatory
    filename = open("liked-songs-backup.txt","wb")
    print_name(filename)
    filename.close()

if __name__ == '__main__':
    login()
    main()