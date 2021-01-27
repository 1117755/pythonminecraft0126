from mcpi.minecraft import Minecraft
qq=Minecraft.create()
whilrue:
    x,y,z=qq.player.getTilePos()
    block1=qq.getBlock(x,y-1,z)
    block2=qq.getBlock(x+1,y-1,z)
    block3=qq.getBlock(x-1,y-1,z)
    block4=qq.getBlock(x,y-1,z+1)
    block5=qq.getBlock(x,y-1,-1)
    if block1== 8 or block1 == 9 or block2 == 9 or block2 == 8 or block3 == 8 or block3 == 9 or block3 == 8 or block4 == 9 or block5 == 8 or block5 ==9:
        qq.setBlock(x,y-1,z,79)
        qq.setBlock(x,y-1,z+1,79)
        qq.setBlock(x,y-1,z-1,79)
        qq.setBlock(x-1,y-1,z,79)
        qq.setBlock(x+1,y-1,z,79)
    