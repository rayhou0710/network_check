import subprocess as sp
import sys
import time
import string
import os
import call

def Ping ():
    call.call("logger ping.py started")
    output = call.call("ping -c4 www.google.com")            
    print output
    
    f=open('log.txt','a')
    f.write(output)

    rate= output.find('received')
    if rate >2:
        pack=rate-2
        p1=output[pack]
        p=int(p1)
        
    else:
        p=0
    #print p
    if p<3:

        restart =call.call("sudo service network-manager restart")
	time.sleep(30)
	call.call("logger network manager restarted by ping.py");
	print ("network-manager restarted")
                   
    f.close()
   
      
if __name__ == '__main__':
    main()
