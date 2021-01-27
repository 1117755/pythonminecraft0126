from mcpi.minecraft import Minecraft
qq=Minecraft.create()

import random,time
while True:
    x,y,z=qq.player.getTilePos()

    color=random.randrange(0,16)
    qq.setBlocks(x+10,y,z+10,x-10,y,z-10,95,color)
    time.sleep(3)