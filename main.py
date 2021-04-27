import time
import datetime
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TASK
# 1. GUI
# 2. Userinput (posts to like & comment, comment, hashtag)
# 3. Options (only like, or like and comment)
# 4. Field (hashtag, explore, or account feed.)
# 5. Find out who is following you and who is not following you.
# 5. Download option, use URLLIB
#    go to the image or video url and press CMD+S to save and press ENTER


# ISSUES
# 1. We can only like 350 posts an hour
# 2. Comment up to 60 comments per hour

# SOLUTIONS
# 1. have one int variable to keep track of comments and one to keep track of likes


######################### GLOBAL STUFF #########################
# ARRAYS
posts = []
users = []
images = []
videos = []
followers = []
following = []
notFollowingBack = []

# OTHER GLOBAL VARIABLES
postMaster = None
numOfPosts = ""
imageOrVideo = ""
imageURL = ""
videoURL = ""
hashtag = ""
userComment = ""
aTags = {}

# USERNAME & PASSWORD
username = "abdulaziz2029"
password = "abdulaziz24"
################################################################

# print out the options
print("\t\tOPTIONS\n[1] Explore\t\t[2] Hashtag\t\t[3] is following?\n")
# take an input from the user
userPrefrence = input("Enter 1, 2, or 3: ").strip()
# if the input is 2
if userPrefrence == "2":
    # ask the user for a hashtag name | clear out any white spaces at the end
    hashtag = input("Hashtag [#gaming, #comedy, etc../]:").strip()
# take an input for scroll amount from the user
scrollAmount = input("Enter a number [scroll amount]:").strip()
# if the input is not 3
if userPrefrence != "3":
    # ask the user for a comment | will be used to comment under posts
    userComment = input("Enter a comment:")
# convert str to int
scrollAmount = int(scrollAmount)

# open browser
browser = webdriver.Chrome(ChromeDriverManager().install())
# maximize the browser
browser.maximize_window()

browser.get("https://www.instagram.com/?hl=en")
# time.sleep(3)
# username box
usernameBox = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.NAME, "username")))
# usernameBox = browser.find_element_by_xpath("//*[@name='username']")
# time.sleep(2)
# type the username
usernameBox.send_keys(username + Keys.TAB)
# password box
passwordBox = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.NAME, "password")))
# passwordBox = browser.find_element_by_xpath("//*[@name='password']")
# type the password
passwordBox.send_keys(password + Keys.ENTER)
# time.sleep(5)

# notification On or Not Now button
notificationBtn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
notificationBtn.click()
# browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
# time.sleep(2)


def isFollowing():
    global followers
    global following
    global notFollowingBack
    global aTags

    # link to profile
    profileLink = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')))
    profileLink = profileLink.get_attribute('href')
    # profileLink = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a').get_attribute('href')
    # go to that profile
    browser.get(profileLink)

    # FOLLOWERS
    # click the followers button
    followersBtn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
    followersBtn.click()
    # browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    # time.sleep(5)
    # div that holds all followers
    listOfFollowers = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
    # listOfFollowers = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]')

    # scroll down the page scrollAmount of times
    for scroll in range(scrollAmount):
        # listOfFollowers.send_keys(Keys.END)  # scroll the page
        browser.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', listOfFollowers)
        time.sleep(1)
    # time.sleep(5)
    # get all 'a' tags
    # aTags = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
    aTags = listOfFollowers.find_elements_by_tag_name('a')
    # go through the aTags list, however many there are.
    for a in aTags:
        # get the profile name
        name = a.get_attribute('title')
        # if a tag is "", skip it and don't add it to the array
        if name == "":
            continue
        # add profile names to the array
        followers.append(name)
    # print out the followers
    print("Followers:", len(followers), "-->", followers)

    # the 'x' button | close the followers div
    browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()

    # FOLLOWING
    # click on the following div
    followingBtn = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')))
    followingBtn.click()
    # browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    # time.sleep(5)
    # div that holds all following accounts
    listOfFollowing = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
    # listOfFollowing = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]')
    # scroll down scrollAmount times
    for y in range(scrollAmount):
        # listOfFollowers.send_keys(Keys.END)  # scroll the page
        browser.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', listOfFollowing)
        time.sleep(1)
    # time.sleep(5)
    # get all 'a' tags | returns a list
    aTags = listOfFollowing.find_elements_by_tag_name('a')
    # go through the 'a' list
    for a in aTags:
        # get profile name
        name = a.get_attribute('title')
        # if name is empty, skip | don't append it to the array
        if name == "":
            continue
        # add names to the array
        following.append(name)
    # print out the following list
    print("Following:", len(following), "-->", following)

    # go through the following list
    for name in following:
        # if the person we are following is NOT in our follower's list
        if name not in followers:
            # add that person to the list
            notFollowingBack.append(name)
    # print out who are following and who are not
    print("These people are not following you back:", len(notFollowingBack), "-->", notFollowingBack)


# EXPLORE
def explore():
    global postMaster
    # time.sleep(3)
    # explore page link
    explore_page = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').get_attribute('href')
    # go to that page
    browser.get(explore_page)
    # time.sleep(5)
    # div that holds all posts
    postMaster = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article')))
    # postMaster = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article')


# HASHTAG
def byHashtag(hash_t):
    global postMaster
    global numOfPosts
    # search box
    # time.sleep(3)
    # search box
    searchBox = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    # put in the hashtag into search box
    searchBox.send_keys(hash_t)
    time.sleep(2)
    # press enter
    searchBox.send_keys(Keys.ENTER)
    time.sleep(2)
    # press enter, we have press enter 2x
    searchBox.send_keys(Keys.ENTER)
    # time.sleep(5)
    # div that holds all the posts
    postMaster = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/article")))
    # postMaster = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article")
    # find out how many posts there are under the hashtag
    numOfPosts = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span')))
    numOfPosts = numOfPosts.get_attribute("innerHTML")
    # numOfPosts = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span').get_attribute("innerHTML")
    numOfPosts = numOfPosts.replace(',', '')
    numOfPosts = int(numOfPosts)
    print("Number of post", numOfPosts)


# if user wants to target a specific hash-tag
if userPrefrence == "1":
    # explore page
    explore()
elif userPrefrence == "2":
    # target specific #hashtag
    byHashtag(hashtag)
else:
    # find out who are following you and who are not.
    isFollowing()

if userPrefrence != "3":
    # scroll the page for a certain amount of time
    postNum = 0
    while 1:
        browser.find_element_by_tag_name('html').send_keys(Keys.END)  # scroll the page
        time.sleep(5)  # sleep for a second
        aTags = postMaster.find_elements_by_tag_name("a")  # get all 'a' tags
        # get links from 'a' tags and put it into an array
        for x in aTags:
            postUrl = x.get_attribute("href")
            # if the link is already in the array, skip
            if postUrl in posts:
                continue
            else:
                posts.append(postUrl)
        # if number of posts is equal to what ever user put in
        if postNum >= scrollAmount:
            # break the loop
            break
        # add 1 each cycle
        postNum = postNum + 1

    print("Posts Targeted:", len(posts))
    print(posts)

    for post in posts:
        # noinspection PyBroadException
        try:
            browser.get(post)  # go to that post
            time.sleep(4)
            # decide if it is an image or video
            # noinspection PyBroadException
            try:
                # noinspection PyBroadException
                try:
                    # IMAGE
                    # 1 image w/o tags
                    imageURL = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[1]/div/div/div[1]/img').get_attribute('src')
                    imageOrVideo = "image"
                except:
                    # IMAGE
                    # noinspection PyBroadException
                    try:
                        # 1 image w/ tagged
                        imageURL = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[1]/div/div/div[1]/div[1]/img').get_attribute('src')
                        imageOrVideo = "image"
                    except:
                        # noinspection PyBroadException
                        try:
                            # if more than 1 image w/ tag
                            imageURL = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[1]/div/div/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/div[1]/img').get_attribute('src')
                            imageOrVideo = "image"
                        except:
                            # if more than 1 image w/o tag
                            imageURL = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[1]/div/div/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/img').get_attribute('src')
                            imageOrVideo = "image"
            except:
                # noinspection PyBroadException
                try:
                    # VIDEO
                    videoURL = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[1]/div/div/div[1]/div/div/video').get_attribute('src')
                    imageOrVideo = "video"
                except:
                    # VIDEO
                    videoURL = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[1]/div/div/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/div/div/video').get_attribute('src')  # more than 1 video w/ tag
                    imageOrVideo = "video"

            time.sleep(0.5)
            # find the user who posted this post.
            user = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/a').get_attribute('innerHTML')
            # add user to users array
            users.append(user)
            # post number and plus one b/c we don't post # 0
            postIndex = posts.index(post) + 1
            # put them into an array
            if imageOrVideo == "image":
                images.append(imageURL)  # add image link to the images array
                videos.append("None")  # append none to videos if it is an image, so index would match
                print("Post number", postIndex, "of", len(posts), "-->", user, "posted an image", imageURL, "at", post)
            else:
                videos.append(videoURL)  # add video link to the videos array
                images.append("None")  # append none to images if it is a video, so index would match
                print("Post number", postIndex, "of", len(posts), "-->", user, "posted a video", videoURL, "at", post)

            browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button').click()  # like
            time.sleep(1)
            cmtBox = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')  # comment box
            time.sleep(0.5)
            cmtBox.click()  # click the comment box
            time.sleep(0.5)
            keyboard.write(userComment)  # write into comment box
            time.sleep(1)
            # noinspection PyBroadException
            try:
                # click the post button
                browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
            except:
                # press enter
                keyboard.press('enter')  # post the comment

            time.sleep(4)
        # if a post doesnt allow users to leave a comment
        # or any other error
        except:
            print("error occured")
            pass

    print("\bAll Users:", users)
    print("All Posts:", posts)
    print("All Images:", images)
    print("All Videos:", videos)
    print("All finished.")
