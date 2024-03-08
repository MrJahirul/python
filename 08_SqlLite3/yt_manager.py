import sqlite3


conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()


#Creating Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        duration TEXT NOT NULL
    )           
               
''')

def show_list():
    print("*"*50)
    cursor.execute("SELECT * FROM videos") #Here curssor hold output value
    for item in cursor.fetchall(): #fetchall() show all value
        print(item)
    print("\n")
    print("*"*50)
def add_video(name, duration):
    cursor.execute("INSERT INTO videos (name,duration) VALUES (?,?)",(name,duration))
    conn.commit()
def update_video(video_id,name,duration):
    cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?", (name, duration, video_id))
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()
    
    

def main():
    while True:
        print("\n ***** YT VIDEO MANAGER *****")
        print("1. Show List")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit App")

        choice=input("Enter Your Option: ")

        match choice:
            case '1':
                show_list()
            case '2':
                name=input("Enter Your Video Name: ")
                duration=input("Enter Your Video Duration: ")
                add_video(name, duration)
            case '3':
                video_id=int(input("Enter Your Video ID: "))
                name=input("Enter Your Video New Name: ")
                duration=input("Enter Your Video Duration: ")
                update_video(video_id,name,duration)
            case '4':
                video_id=int(input("Enter Vaideo ID: "))
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Enter Valid Option")

if __name__=="__main__":
    main()
            
        
            
    