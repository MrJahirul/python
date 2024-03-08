import json

def load_list():
    try:
        with open('videos.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 

#for saving data 
def savedata_helper(videos):
    with open('videos.txt','w') as file: 
        json.dump(videos,file)
def show_list(videos):
    print("\n")
    print("*"*50)
    for index,videos in enumerate(videos,start=1):
        print(f"{index}.  Name: {videos['Name']} | Duration: {videos['time']}")
    print("\n")
    print("*"*50)
def add_video(videos):
    name=input("Video Name: ")
    time=input("Video Length: ")
    videos.append({'Name':name ,'time':time})
    savedata_helper(videos) 
def update_list(videos):
    show_list(videos)
    index=int(input("Enter Your Index: "))
    name=input("Enter New Name: ")
    time=input("Enter New Time: ")
    #videos[index-1]={'name':name,'time':time}
    videos[index-1]['Name']=name
    videos[index-1]['time']=time
    savedata_helper(videos)
def delete_video(videos):
    show_list(videos)
    index=int(input("Enter Your Index: "))
    videos.pop(index)
    savedata_helper(videos)

def main():
    videos=load_list() #load data from file
    

    while True:
        print("→ YouTube Updater | Chhose Your Option ←" )
        print("1. For Show Your List")
        print("2. For Add Video List")
        print("3. For Update Your List")
        print("4. For Delete Video From Your List")
        print("5. For Exit The App")

        choice=input("Enter Your Option: ")
        match choice:
            case '1':
                show_list(videos)
            case '2':
                add_video(videos)
            case '3':
                update_list(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Choose Vadlid Option")


if __name__=="__main__":
    main()




    
