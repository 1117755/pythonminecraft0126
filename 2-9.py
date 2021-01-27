from mcpi.minecraft import Minecraft
qq=Minecraft.create()

x,y,z=qq.player.getTilePos()
qq.setSign(x,y,z+1,63,0,"我愛猿創力","也愛python")
