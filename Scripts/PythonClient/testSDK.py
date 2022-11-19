import NatNetClient as libSDK
import MoCapData as data
import time

client = libSDK.NatNetClient()
client.set_server_address("127.0.0.1")

def procceed_rigid( new_id, position, rotation ):
    print(  new_id," ",position," ",rotation )

client.rigid_body_listener = procceed_rigid
client.run()
# print(type(data.RigidBodyData.get_rigid_body_count())) 
time.sleep(10)
client.shutdown()