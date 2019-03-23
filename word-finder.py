import sys
from selenium import webdriver
from talk import Talk

# Parse the arguments first
f = open(str(sys.argv[1]) + str(sys.argv[2]) + str(sys.argv[3]) + '.txt', "w")
url = 'https://www.lds.org/general-conference/' \
      + str(sys.argv[2])                        \
      + '/'                                     \
      + str(sys.argv[3])                        \
      + '?lang=eng'

# get the dynamic list of words to search for
words = []
if (len(sys.argv) == 5):
  words.append(sys.argv[4])
elif (len(sys.argv) > 5):
  for i in range(len(sys.argv) - 4, len(sys.argv)):
    words.append(sys.argv[i])

# Initialize talks list
talks = []

# Initialize browser
browser = webdriver.Firefox()
browser.get(url)

# Get list of talks
elem = browser.find_elements_by_class_name("lumen-tile__link");
for e in elem:
    speaker = e.find_element_by_class_name("lumen-tile__content").get_attribute('innerHTML')
    title = e.find_element_by_class_name("lumen-tile__title").find_element_by_tag_name('div').get_attribute('innerHTML')
    link = e.get_attribute('href')
    talks.append(Talk(speaker, title, link))

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
