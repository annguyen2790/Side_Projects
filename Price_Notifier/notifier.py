import bs4
import requests
from bs4 import BeautifulSoup
import smtplib
import time
def checkPrice():
    #URL of the product wanted 
    URL = 'https://www.amazon.com/gp/product/B07RF2123Z/ref=s9_acss_bw_cg_PCLTMC_2b1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=C2EYPD896DK1G7KM0PS3&pf_rd_t=101&pf_rd_p=e5059426-911c-49a1-830e-fa1d8c1fc535&pf_rd_i=565108'
    #Headers used for requests function call to identify OS and web browser 

    headers = {"User-Agent" :   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36' }

    page_request = requests.get(URL, headers=headers)

    contents = page_request.content

    soup = BeautifulSoup(contents, 'html.parser') #make a soup object 
    soup1 = BeautifulSoup(soup.prettify(), 'html.parser') #make a second soup object with all the HTML parsed correctly from the first soup object
    #print(soup.prettify())
    title = soup1.find(id='productTitle').get_text().strip()
    #print(title)
    price_in_text = soup1.find(id='priceblock_ourprice').get_text()
    price = float(price_in_text[1:7])
    print(price)
    #send_email
    return price

def sent_email(password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mazhurt@gmail.com', password)
    msg = 'Price Fell!'
    server.sendmail(
        'mazhurt@gmail.com',
        'annguyen2790111@gmail.com',
        msg
    )
    print('Email has been sent!')
    server.quit()
    
    
    


    
if __name__ == "__main__":
    #email = input("Enter your email: ")
    password = raw_input("Enter your password: ")
    price = checkPrice()
    while(True):
        if price > 450:
            sent_email(password)
            time.sleep(86400)
        else:
            break
