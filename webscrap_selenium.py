from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
#driver = webdriver.Chrome("./chromedriver")
driver = webdriver.Chrome()

df = pd.DataFrame(columns=["Title","Location","Company","Salary","Sponsored","Description"])

for i in range(0,500,10):
	driver.get('https://www.indeed.co.in/jobs?q=artificial%20intelligence&l=India&start='+str(i))
	jobs = []
	driver.implicitly_wait(4)
	

	for job in driver.find_elements_by_class_name('result'):

		soup = BeautifulSoup(job.get_attribute('innerHTML'),'html.parser')
		texto = soup.text
		print(texto)
		try:
			title = soup.find("h1",class_="jobsearch-JobComponent icl-u-xs-mt--sm").text.replace("\n","").strip()
			
		except:
			title = 'None'

		try:
			location = soup.find(class_="location").text
		except:
			location = 'None'

		try:
			company = soup.find(class_="company").text.replace("\n","").strip()
		except:
			company = 'None'

		try:
			salary = soup.find(class_="salary").text.replace("\n","").strip()
		except:
			salary = 'None'

		try:
			sponsored = soup.find(class_="sponsoredGray").text
			sponsored = "Sponsored"
		except:
			sponsored = "Organic"				

		txtt = job.text
        
        #print()
		sum_div = job.find_element_by_xpath('./div')
        
		try:
			sum_div.click()
		except:
			close_button = driver.find_elements_by_class_name('popover-x-button-close')[0]
			close_button.click()
			sum_div.click()	
		
		job_text = driver.page_source
		print(job_text)
		print(txtt)
		job_desc = driver.find_element_by_id('jobDescriptionText').text

		df = df.append({'Title':title,'Location':location,"Company":company,"Salary":salary,
						"Sponsored":sponsored,"Description":job_desc},ignore_index=True)

		print("Got these many results:",df.shape)


df.to_csv("ai.csv",index=False)	