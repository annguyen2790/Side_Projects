import bs4
import requests

#URL of the product wanted 
URL = "https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844?pf_rd_p=dd4f5b57-ba5b-418b-a348-64ec62df14cc&pd_rd_wg=06bmi&pf_rd_r=KK0D5A466X1SM48PE4YM&ref_=pd_gw_cr_simh&pd_rd_w=9pCZy&pd_rd_r=bdd8fa57-eaf6-4824-9902-02a30b50617c"

#Headers used for requests function call to identify OS and web browser 

headers = {'User-Agent' :   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36' }

page_request = requests.get(URL, headers = headers)

print(page_request)
 

