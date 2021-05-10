from selenium import webdriver

#The addressify website does not allow any user to enter in
# an address into the site. To use addressify you must create an API call. I don't know if
# you knew this or not or maybe I misunderstood the question. But it was clear that i could not
# simply enter an address into the search bar of addressify.

# So as an alternative, to show you that I have the skills to make an automated webBot system,
# I used the official python website as a replacement and created a function that automatically
# takes the user's query and prints the results of the page that follow.


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

