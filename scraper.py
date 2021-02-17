from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#url that needs to be scraped
url = 'https://www.youtube.com/channel/UCmh5gdwCx6lN7gEC20leNVA'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

#first upload on the channel
driver.find_element_by_xpath('//*[@id="video-title"]').click()
