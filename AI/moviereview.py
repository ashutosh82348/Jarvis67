from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyttsx3 as pys
    

def review(text,self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(url="https://www.google.com")
    input=self.driver.find_element(By.XPATH,"//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
    input.click()
    input.send_keys(text+" movie reviews")
    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]"))).click()
    try:
        elems = self.driver.find_elements_by_xpath("//*[@id='rso']/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/a/span[1]")[1].text
        print(elems)
        return elems
    except Exception:
        print("Error")
        return None
        
    print("Done")
# bot = Movie()
# bot.movie_review("Ghost Rider")