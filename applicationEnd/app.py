import affnine_client as client
import threading


def data_fetch(listener_obj):
        while (True):
                data=listener_obj.data_()
                print("\n")
                print(data)
                print("\n")

def main():
    client.starter("127.0.0.1",8080,101)
    listener_obj=client.listener()
    data_fetch_thread = threading.Thread(name='data_fetch', target=data_fetch, args=[listener_obj,])
    data_fetch_thread.start()
    sender_obj=client.sender()
    while(True):
        Mac_Address=input("Enter  Target Mac address")
        Topic=input("Enter the Topic Name")
        Msg=input("Enter the Message")
        sender_obj.sender_(Mac_Address,Topic,Msg)



##################################
if __name__ == "__main__":main()##
##################################
