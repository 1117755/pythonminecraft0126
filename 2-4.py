from mcpi.minecraft import Minecraft
qq=Minecraft.create()
x,y,z=qq.player.getTilePos()

long=10
big=8
high=7

block=7
air=0

qq.setBlocks(x,y,z,x+long,y+high,z+big,block)
qq.setBlocks(x+1,y+1,z+1,x+long-1,y+high-1,z+big-1,air)
