python
   from selenium import webdriver

   driver = webdriver.Chrome()
   driver.get("https://example.com/login")

   driver.find_element_by_name("username").send_keys("testbruker")
   driver.find_element_by_name("password").send_keys("testpassord")
   driver.find_element_by_name("login").click()

   assert "Velkommen" in driver.page_source
   driver.quit()