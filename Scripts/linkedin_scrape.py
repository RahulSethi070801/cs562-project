from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import random
from bs4 import BeautifulSoup

# keywords = ["intern" "summer 2025", "software"]

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service, options=options)

def linkedin_login():
        
    driver.get('https://www.linkedin.com/login')
    time.sleep(random.randint(2, 4))
    
    # Enter login credentials
    driver.find_element(By.ID, 'username').send_keys('rahuulsethii07@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('Rahul070801')
    
    # Click login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(random.randint(3, 5))
    
# https://www.linkedin.com/in/varunkmohan/recent-activity/all/
# https://www.linkedin.com/company/augmentinc/posts/?feedView=all
    
def search_posts():
    search_url = f"https://www.linkedin.com/in/sanjeev-verma-20838655/recent-activity/all/"
    driver.get(search_url)
    time.sleep(random.randint(3, 6))
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(random.randint(2, 4))
       new_height =  driver.execute_script("return document.body.scrollHeight")
       if  new_height == last_height:
           break
       last_height = new_height
        
def scrape_posts():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Find all post elements (adjust class name if necessary)
    posts = soup.find_all('div', class_='feed-shared-update-v2__description-wrapper')
    # 'feed-shared-update-v2__description-wrapper'
    
    scraped_data = []
    
    for post in posts:
        # more_button = post.find('button', class_='feed-shared-inline-show-more-text__see-more-less-toggle')
        # if more_button:
        #     try:
        #         more_button.click()
        #         time.sleep(random.randint(2, 4))
        #     except:
        #         continue
        post_text = post.get_text(strip=True)
        scraped_data.append(post_text)
    
    return scraped_data

def main():
    linkedin_login()
    
    search_posts()
    
    posts_content = scrape_posts()
    
    with open('ceo_codeium_varun_posts.txt', 'w', encoding='utf-8') as file:
        for i, post in enumerate(posts_content, start=1):
            file.write(f"Post {i}: {post}\n\n")
    
    # for i, post in enumerate(posts_content[:1000], start=1):
    #     with open('scraped_posts.txt', 'w', encoding='utf-8') as file:
    #         for i, post in enumerate(posts_content[:50], start=1):
    #             file.write(f"Post {i}: {post}\n\n")

if __name__ == "__main__":
    main()
    driver.quit()