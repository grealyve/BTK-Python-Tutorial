from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        # self.browserProfile = webdriver.FirefoxOptions()
        # self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages":"en,en_US"})
        # self.browser = webdriver.Firefox("firefoxdriver.exe", firefox_options=self.browserProfile)
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        self.browser.get("https://www.instagram.com/joseph_y.l/")
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)

        dialog =self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(3)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        followeerList = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followeerList.append(link)

        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in followeerList:
                file.write(item + "\n")


    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)

        # followButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text == "Follow":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten Takiptesin!")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)

        followButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/span")
        followButton.click()
        time.sleep(2)
        unfButton = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
        unfButton.click()



instagram = Instagram(username, password)
instagram.signIn()
instagram.getFollowers()
# instagram.followUser("siber_dunya")

# list = ["siber_dunya",""]
# for user in list:
#     instagram.followUser(user)
#     time.sleep(3)

# instagram.unFollowUser("siber_dunya")