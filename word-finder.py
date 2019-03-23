import sys
from selenium import webdriver
from talk import Talk

url = 'https://www.lds.org/general-conference/' \
      + str(sys.argv[1])                        \
      + '/'                                     \
      + str(sys.argv[2])                        \
      + '?lang=eng'

browser = webdriver.Firefox()
browser.get(url)

talks = []
f = open('invitations.txt', "w")

elem = browser.find_elements_by_class_name("lumen-tile__link");
for e in elem:
    speaker = e.find_element_by_class_name("lumen-tile__content").get_attribute('innerHTML')
    title = e.find_element_by_class_name("lumen-tile__title").find_element_by_tag_name('div').get_attribute('innerHTML')
    link = e.get_attribute('href')
    talks.append(Talk(speaker, title, link))

words = ["invite", "invitation"]
for t in talks:
    f.write(t.toString())
    browser.get(t.link)
    body = browser.find_element_by_class_name("body-block")
    paragraphs = body.find_elements_by_tag_name("p")
    for p in paragraphs:
        for w in words:
            if (p.text.find(w) != -1):
                f.write(p.text + '\n')
    f.write('\n')
f.close()


