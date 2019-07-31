import affnine as afn
import select 
import socket 
import sys 
import threading
import json
import time
#...........................................
connection_var=1
global mac
global sock
#............................................
#............................................


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#..............................................
#......>>>server_listen_Function<<<............
#..............................................
#....Comments >>>

#..............................................
class listener():
    def __init__(self):
        server_listen_thread = threading.Thread(name='server_listen', target=self.server_listen)
        server_listen_thread.start()
        Var_Connection_Check="Am i connected"
        Var_Connection_Check={"Note":str(Var_Connection_Check),"type":"Connection_check","status":"010"}
        afn.client_send(sock,Var_Connection_Check)
        self.data=""
        self.data_flag="0"
    def server_listen(self):
        global connection_var
        global sock
        global data_checker_var
        while (str(connection_var)==str(1)):
            data=afn.client_recieve(sock)
            if data:
                if (str(connection_var)==str(1)):
                    try:
                        if (data["type"]=="Connection_check"):
                            if(data["status"]=="101"):
                                pass
                        if (data["type"]=="msg"):
                            pass
                        self.data=data
                        self.data_flag="1"
                    except:
                        pass
    def data_(self):
        while(self.data_flag == "0"):
            pass
        self.data_flag="0"
        return self.data


#..............................................

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#..............................................
#............>>>Sender_Function<<<.............
#..............................................
#....Comments >>>

#..............................................
class sender:
    def __init__(self):
        global mac,sock
        self.mac=mac
        self.sock=sock
    def sender_(self,Target_Mac_Address,Topic,Msg):
        data={"type":"msg","topic":str(Topic),"target_mac_address":str(Target_Mac_Address),"source_mac_address":str(self.mac),"msg":str(Msg)}
        afn.client_send(self.sock,data)
#..............................................

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#..............................................
#............>>>Starter_Function<<<............
#..............................................
#....Comments >>>

#..............................................

def starter(ip,port,mac_):
    global sock 
    global mac
    mac=mac_
    connection_creator_obj=connection_creator(ip,port,mac)
    connection_creator_obj.connection_create()

#.............................................

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#..............................................
#............>>>Creator_Function<<<............
#..............................................
#....Comments >>>

#..............................................

class connection_creator():
    def __init__(self,ip,port,mac):
        self.ip=ip
        self.port=port
        self.mac=mac
        self.conn_create_var={"type":"Create_Connection","mac":str(mac)}
    def connection_create(self):
        global sock
        sock=afn.client_connection(self.ip,self.port)
        afn.client_send(sock,self.conn_create_var)
#.............................................