from selenium import webdriver

def automated(query):
    #define the location with your chrome driver is installed
    driver = webdriver.Chrome(executable_path=r'C:\Users\rajku\Desktop\chromedriver.exe')
    driver.get('https://www.python.org/')
    driver.find_element_by_id('id-search-field').send_keys(query)

    element = driver.find_element_by_id('submit')
    element.click()
    links = driver.find_elements_by_xpath('//h3//a')

    print('Resulting links for this query:')
    for link in links:
        href = link.get_attribute('href')
        results = print(href)
    return results

automated('classes')

