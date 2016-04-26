
from pox.core import core
from pox.sql import sql_flow
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
import csv


log = core.getLogger()

def firewall(event):
	
	log.info("Firewall Policies")
	with open('/home/ubuntu/pox/sqlapps/firewall-policies.csv', 'rb') as csvfile:
		rule = csv.reader(csvfile, delimiter=' ', quotechar='|')
		test=1
		#cord(event)
		for row in rule:
			if test==0:
				token = row[0].split(",")
				query = """INSERT INTO OF_table (MAC_src, MAC_dst, Action, priority) VALUES ('"""+ token.pop(1)+"""' , '"""+token.pop(1)+"""', "drop", "20")"""
				sql_flow(event,query)
			test=0
			
	query = 'INSERT INTO OF_table(Action, priority) VALUES ("flood", "10")'
	sql_flow(event,query)

def _handle_ConnectionUp (event):
	firewall(event)


def launch ():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    log.info("Firewall running.")

