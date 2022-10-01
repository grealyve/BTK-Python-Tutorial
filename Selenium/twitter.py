from twitterUser import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(2)
        passwordInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

    def search(self):
        # searchInput = self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        # searchInput.send_keys(hashtag)
        # time.sleep(2)
        # searchInput.send_keys(Keys.ENTER)
        # time.sleep(2)

        results = []

        texts = self.browser.find_elements_by_xpath("//article[@data-testid='tweet']/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
        time.sleep(2)
        print("count: "+ str(len(texts)))

        for i in texts:
            results.append(i.text)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 3:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter += 1

            texts = self.browser.find_elements_by_xpath("//article[@data-testid='tweet']/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
            time.sleep(2)
            print("count: " + str(len(texts)))

            for i in texts:
                results.append(i.text)

        # with open("tweets.txt","w",encoding="UTF-8") as file:
        #     count = 1
        #     for item in results:
        #         file.write(f"{count}-{item}\n")
        #         count += 1

        count = 1
        for item in results:
            print(f"{count}-{item}")
            count+=1
            print("*******************************")

        # texts = self.browser.find_elements_by_xpath("//article[@data-testid='tweet']/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
        # for x in texts:
        #     print("************************")
        #     print(x.text)



twitter = Twitter(username, password)
twitter.signIn()
time.sleep(5)
twitter.search()