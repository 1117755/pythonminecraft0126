from mcpi.minecraft import Minecraft
qq=Minecraft.create()

x,y,z=qq.player.getTilePos()
qq.setBlock(x,y,z+1,7)
qq.setBlock(x,y,z-1,7)
qq.setBlock(x-1,y,z,7)
qq.setBlock(x+1,y,z,7)
qq.setBlock(x+1,y,z+1,7)
qq.setBlock(x-1,y,z+1,7)
qq.setBlock(x+1,y,z-1,7)
qq.setBlock(x-1,y,z-1,7)