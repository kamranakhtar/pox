
from pox.core import core
from pox.sql import sql_flow
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
log = core.getLogger()



def _handle_ConnectionUp (event):
	log.info("Normal Switching")
	query = "INSERT INTO OF_table (MAC_dst, Action) VALUES ('00:11:22:33:44:55', '6' )"
	sql_flow(event,query)
	
	log.info("Flow Switching")
	query = "INSERT INTO OF_table (Switch_Port, MAC_src, MAC_dst, Eth_type, VLAN_ID, VLAN_priority, IP_Src, IP_Dst, IP_Prot, IP_tos, TCP_sport, TCP_dport, Action) VALUES ('3', '00:11:22:33:44:66', '00:11:22:33:44:55', '2048', '10', '100', '192.168.66.2', '192.168.66.3', '6', '3', '1254', '80', '6' )"
	sql_flow(event,query)
	
	log.info("Port Based Firewall")
	query = "INSERT INTO OF_table (TCP_dport, Action, priority) VALUES ('80', 'drop','20' )"
	sql_flow(event,query)
	
	log.info("Basic HUB")
	query = 'INSERT INTO OF_table(Action) VALUES ("flood" )'
	sql_flow(event,query)
	
def launch ():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    log.info("Normal Switching, Flow Switching and Firewall Example.")

