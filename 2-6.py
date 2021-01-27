from mcpi.minecraft import Minecraft
qq=Minecraft.create()
x,y,z=qq.player.getTilePos()
 
answer=int(input('請問你要放 麽方塊:'))
qq.setBlock(x+1,y,z,answer)