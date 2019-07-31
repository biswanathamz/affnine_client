########################
import select 
import socket 
import sys 
#from _thread import *
import threading
import json
buffer_size=1024
sock_list=[]
sock_addr_list=[]
devices={"mac":"addr"}
thread_closer={"addr":"1"}
########################
lc= threading.Lock()
#print
########################
########################################################################################
def add_mac(data,addr,sock):
  global devices
  global sock_list
  global sock_addr_list
  global thread_closer
  mac=str(data["mac"])
  # mac_secret=str(data["mac_secret"])
  var_counter=0
  var_key=0
  #
  # check mac_secret of mac in database if -> check=1 else check=0 
  # chech=check_mac_secret()
  #print(mac)
  #print(mac_secret)
  check=1

  if(str(check)==str(1)):
    for key in devices:
      if(str(devices[key])==mac):
        for i in sock_addr_list:
          var_counter=var_counter+1
          if(str(key)==str(i)):
            #print(key)
            #print(i)
            #print(sock_addr_list[var_counter-1])
            var_key=(sock_addr_list[var_counter-1])
            del sock_addr_list[var_counter-1]
            del sock_list[var_counter-1]
            thread_closer[str(i)]="0"
            #print(thread_closer[str(addr)])
            #return(0)
            var_counter=0
            break
        del devices[str(var_key)]
        break
  elif(str(check)==str(0)):
    data={"conn_check":"..."}
    data=json.dumps(data)
    sock.sendall(data.encode('utf-8'))
  sock_list.append(sock)
  sock_addr_list.append(addr)
  devices[str(addr)]=str(data["mac"])
  # data={"conn_check":"ok"}
  # data=json.dumps(data)
  # server_send_using_mac(data,mac)
  print("connected to :", addr[0], ':', addr[1])
  #....................................................................................
def server_send_using_addr(data,addr):
    global sock_list
    global sock_addr_list
    global devices
    data=json.dumps(data)
    var_counter=0
    for i in sock_addr_list:
      var_counter=var_counter+1
      if(i==addr):
        var_sock=sock_list[var_counter-1]
        var_sock.sendall(data.encode('utf-8'))
         
  #....................................................................................
def server_send_using_mac(data,mac):
    global sock_list
    global sock_addr_list
    global devices
    mac=str(mac)
    #data=json.dumps(data)
    var_counter=0
    for key in devices:
      if(devices[key]==mac):
        for i in sock_addr_list:
          var_counter=var_counter+1
          if(str(i)==str(key)):
            var_sock=sock_list[var_counter-1]
            var_sock.sendall(data.encode('utf-8'))
             
  #...................................................................................
# def message(data,addr):
#     global sock_list
#     global sock_addr_list
#     global devices
#     #print("Message : ",data["Message"],"from : ",str(addr))
#     reply_data={"Message":"Hello Client"}
#     server_send_using_addr(reply_data,addr)
     
  #...................................................................................
def sock(host,port,backlog,buffer_size):     #d
    global devices
    sock.buffer_size=buffer_size
    sock.input=0
    sock.server=0
    
    sock.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.server.bind((host,port)) 
    print("Socket binded to port",port)
    sock.server.listen(backlog)
    print("Socket is listening")
#...........................................................................................
def add_client():                           #d
  # a forever loop untill client wants to exit
  while True:
    global sock_list
    global sock_addr_list
    global thread_closer
    c, addr=sock.server.accept() #Establish connection with clients
    return(c,addr)
  
###########################################################################################
def client_send(client,data):             #d
    data=json.dumps(data)
    client.sendall(data.encode('utf-8'))
def client_recieve(sock):
    global buffer_size
    raw_data=sock.recv(buffer_size)
    data=raw_data.decode()
    data=json.loads(data)
    return(data)
def client_connection(ip,port):           #d
    s = socket.socket()
    s.connect((ip, port))
    return(s)

#..........................................................................................
