import natnetclient as natnet
import numpy as np
import os
print("1234")
client = natnet.NatClient()
while(True):
    center = client.rigid_bodies["Triangle"].position
    position = center  # np.array(client.rigid_bodies["TestBody"].position) - center
    # orientation_n = np.array(client.rigid_bodies["Triangle"].quaternion)
    # os.system("cls")
    print(position) #,orientation_n)
