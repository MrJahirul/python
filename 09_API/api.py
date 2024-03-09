import requests



def apiRequest():
    url="https://api.freeapi.app/api/v1/public/cats/cat/random"
    response=requests.get(url)
    data=response.json()
    
    if data["success"] and "data" in data:
        user_data=data["data"]
        user_name=user_data["name"]
        user_origin=user_data["origin"]
        return user_name,user_origin
    else:
        raise Exception("Data Not Found")

def main():
    try:
        user_name,user_origin=apiRequest()
        print(f"UserName: {user_name}\nUserOrigin: {user_origin}")
    except Exception as e:
        print(str(e))
    

if __name__=="__main__":
    main()