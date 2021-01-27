from mcpi.minecraft import Minecraft
qq=Minecraft.create()
import random
while True:
    x,y,z=qq.player.getTilePos()
    ii = random.randrange(0,9)
  
    qq.setBlock(x,y,z-1,38,iie)
    