from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.addresses import IPAddr,EthAddr
log = core.getLogger()
from pox.sqlclass import DBManager


def sql_flow(event,query):
    dbmgr = DBManager(":memory:")
    #dbmgr = DBManager("testdb.db")
    #dbmgr.query("INSERT INTO person VALUES ('kamran','ali',30)")
    #dbmgr.query("INSERT INTO person VALUES ('yousaf','akhtar',50)")
    #dbmgr.query('INSERT INTO OF_table (MAC_src, MAC_dst, Action) VALUES ("00:00:00:00:00:05","00:00:00:00:00:01", "drop" )')
    
    dbmgr.query1(query)
    
    for row in dbmgr.query1("SELECT * FROM OF_table"):
        msg = of.ofp_flow_mod()
        if row[0]!=None:
            msg.match.in_port =int(row[0]) # 2
        if row[1]!=None:
            msg.match.dl_src = EthAddr(row[1]) # EthAddr("01:02:03:04:05:06")
        if row[2]!=None:
            msg.match.dl_dst = EthAddr(row[2]) # EthAddr("01:02:03:04:05:06")
        if row[3]!=None:
            msg.match.dl_type = int(row[3])# 0x800    
        if row[4]!=None:    
            msg.match.dl_vlan = int(row[4])# 10
        if row[5]!=None:
            msg.match.dl_vlan_pcp = int(row[5])# 100 value may vary from 0~255
        if row[6]!=None:
            msg.match.nw_src = IPAddr(row[6]) # "192.168.66.0/24"
        if row[7]!=None:
            msg.match.nw_dst = IPAddr(row[7]) # "192.168.66.0/24"
        if row[8]!=None:
            msg.match.nw_proto = int(row[8]) # 6 is for tcp
        if row[9]!=None:
            msg.match.nw_tos = int(row[9])# 3 # quality of service class
        if row[10]!=None:
            msg.match.tp_src = int(row[10])# 80
        if row[11]!=None:
            msg.match.tp_dst = int(row[11])# 80
        if row[12]!=None:
            if row[12] == "flood" or row[12] == "FLOOD":
                msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
            elif row[12] == "drop" or row[12]== "DROP":
                pass
            else:
                msg.actions.append(of.ofp_action_output(port = int(row[12])))
        if row[13]==None:
            msg.idle_timeout = 1000
        else:
            msg.idle_timeout = int(row[13])# 1000 int
        if row[14]==None:
            msg.hard_timeout = 1000
        else:
            msg.hard_timeout = int(row[14])# 0 int
        if row[15]!=None:
            msg.buffer_id = int(row[15])# 2870 int
        if row[16]!=None:
            msg.priority = int(row[16])# uint16_t priority, Priority level of flow entry 0 is highest priority
                    
        event.connection.send(msg)
        #print "Flow is being deployed"
        log.info("SQL Flow Mode Query from sql module %s", dpidToStr(event.dpid))

