
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
		
		for row in rule:
			if test==0:
				token = row[0].split(",")
				# Write here 
				#flow deployment instructions that deploy flow rules from firewall-policies file
				# token.pop(1) can be used for getting a mac address in sequence first MAC_src and then MAC_dst
				
				
				
			test=0
			
	# Write here
	# a flow deployment instructions that deploy flow rule that flood the packets, for basic Hub functionality
	
	
	

def _handle_ConnectionUp (event):
	firewall(event)


def launch ():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    log.info("Firewall running.")

