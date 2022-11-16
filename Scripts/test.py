import natnetclient as natnet
import numpy as np
client = natnet.NatClient(client_ip='127.0.0.1', data_port=1511, comm_port=1510)
print(client.ping())

while(True):
    ms = client.unidentified_markers
    if len(ms) > 0:
        markers = np.zeros((len(ms),3))
        for i in range(len(ms)):
            markers[i] = np.array(ms[i].position[:3])
        print(markers)