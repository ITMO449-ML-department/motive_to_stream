import natnetclient as natnet
import numpy as np
client = natnet.NatClient(client_ip='127.0.0.1', data_port=1511, comm_port=1510)

while(True):
    center = np.array(client.rigid_bodies["RigidBody_1"].position)
    position = np.array(client.rigid_bodies["RigidBody_2"].position) - center
    print(position)