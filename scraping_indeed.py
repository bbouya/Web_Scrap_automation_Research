import requests 
from bs4 import BeautifulSoup


# User define function 
# Scrape the data 
# And get in string

def getdata(url):
    r = requests.get(url)
    return r.text

# Get Html code 
def html_code(url):
    
    # pass the url
    #into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    
    # return html code 
    return soup

# Filtre job data 
# Find_all function

def job_data(soup):
    
    # Find the Html tag
    # With find()
    # and convert into string
    
    data_str = ""
    for item in soup.find_all('a', class_="jobtitle turnstileLink"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split('\n')
    return(result_1)

#Filtre company_ data using
# Find all function


def company_data(soup):
    # find the html tag
    #with find()
    # and convert into string
       
    data_str = ''
    result = ''
    for item in soup.find_all("div", class_='sjcl'):
        data_str = data_str + item.get_text()
    result_1 = data_str.split('\n')
    
    res = []
    
    for i in range(1, len(result_1)):
        if len(result_1[i])>1:
            res.append(result_1[i])
    return(res)

# Driver nodes/ main function

if __name__ =='__main__':
    
    # Data for Url
    job = 'data+science+internship'
    locatio = 'Noida%2C+Uttar+Pradesh'
    url = "https://in.indeed.com/jobs?q="+job+"&l="+Location

    
    # Pass this URL into the soup^
    # Which will return 
    # Html string
    
    soup = html_code(url)
    
    # Call job and company data
    # and store into it var
    job_res = job_data(soup)
    com_res = company_data(soup)
    
    # Traverse the both data
    temp = 0
    for i in range(1, len(job_res)):
        j = temp 
        for j in range(temp, 2+temp):
            print("Company Name and Address : " + com_res )
            
        temp = j
        print("Job : " + job_res[i])
        print("------------------------------------")