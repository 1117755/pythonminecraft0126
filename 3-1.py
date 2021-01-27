from mcpi.minecraft import Minecraft
qq=Minecraft.create()

while True:
    hits=qq.events.pollBlockHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        blocek=qq.getBlock(x,y,z)
        qq.postToChat("你打到了"+str(block))

























































