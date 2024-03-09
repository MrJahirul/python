import random

import requests

def ind_stock_market():
    url='https://api.freeapi.app/api/v1/public/stocks?page=1&limit100&inc=Name%2CCurrentPrice&query=tata'
    response=requests.get(url)
    data=response.json() 
    
    if data["success"] and "data" in data:
        return data["data"]["data"]
    else:
        raise Exception("Stock Not Found")
    


def main():
    try:
        stock = random.choice(ind_stock_market())
        print(f"Stock Name:{stock["Name"]}\nStock Prize:{stock["CurrentPrice"]}")
        
    except Exception as e:
        print(str(e))
        
if __name__=="__main__":
    main()