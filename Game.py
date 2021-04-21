from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

game_url = "chrome://dino"
chrome_driver_path = "C:/Users/Utilisateur/anaconda3/Lib/site-packages/chromedriver/chromedriver.exe"

class Game:
    def __init__(self,custom_config=True):
        chrome_options = Options()
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--mute-audio")
        self._driver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)
        self._driver.set_window_position(x=-10,y=0)
        
        try :
            self._driver.get('chrome://dino')
        except WebDriverException : pass

        self.press_up ()
        
        self._driver.execute_script("Runner.config.ACCELERATION=0")
    def get_crashed(self):
        return self._driver.execute_script("return Runner.instance_.crashed")
    def get_playing(self):
        return self._driver.execute_script("return Runner.instance_.playing")
    def restart(self):
        self._driver.execute_script("Runner.instance_.restart()")
    def press_up(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)
    def get_score(self):
        score_array = self._driver.execute_script("return Runner.instance_.distanceMeter.digits")
        score = ''.join(score_array) # the javascript object is of type array with score in the formate[1,0,0] which is 100.
        return int(score)
    def pause(self):
        return self._driver.execute_script("return Runner.instance_.stop()")
    def resume(self):
        return self._driver.execute_script("return Runner.instance_.play()")
    def end(self):
        self._driver.close()