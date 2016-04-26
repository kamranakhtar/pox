import sqlite3
class DBManager(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        #print "connection created"
        self.conn.execute("CREATE table OF_table\
    (Switch_Port, MAC_src, MAC_dst, Eth_type, VLAN_ID, VLAN_priority, IP_Src, IP_Dst, IP_Prot, IP_tos, TCP_sport,\
    TCP_dport, Action, idle_timeout, hard_timeout, buffer_id, priority)")
        #print "table created"
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query1(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def __del__(self):
        self.conn.close()