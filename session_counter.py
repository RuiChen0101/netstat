import psutil
import time
import connect_data_decoder as cdd
from datetime import datetime

result_file = open("./session",'w')

while True:
    connects=psutil.net_connections()
    result_file.write("----------------"+str(datetime.now().time())+"----------------\n")
    result_file.write("pid    local_address    local_port  remote_address   remote_port  status\n")
    for connect in connects :
        pid = cdd.get_pid(connect)
        ladd = cdd.get_local_address(connect)
        lport = cdd.get_local_port(connect)
        radd = cdd.get_remote_address(connect)
        rport = cdd.get_remote_port(connect)
        stat = cdd.get_status(connect)
        if radd=='127.0.0.1' or stat!='ESTABLISHED':
            continue
        result_file.write('%-5s  %-15.15s  %-5s       %-15.15s  %-5s        %s'%(pid, ladd,lport,radd,rport,stat)+'\n')

    time.sleep(1)

result_file.close()
