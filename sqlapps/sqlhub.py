from pox.core import core
from pox.sql import sql_flow
log = core.getLogger()

def _handle_ConnectionUp (event):
	sql_query = "INSERT INTO OF_table(Action) VALUES ('flood')"
	sql_flow(event,sql_query)
	
def launch ():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    log.info("Hub running.")

