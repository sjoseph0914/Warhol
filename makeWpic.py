def decreaseRed(pic):
  for p in getPixels(pic):
    value=getRed(p)
    setRed(p,value*.2) 
    
def grayscale(pic):
  for p in getPixels(pic):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p,makeColor(intensity,intensity,intensity))
    
def darken(pic):
  for p in getPixels(pic):
    color=getColor(p)
    color=makeDarker(color)
    setColor(p,color)
    
def makeWpic():
  fname=pickAFile()
  pic=makePicture(fname)
  p=duplicatePicture(pic)  
  wPic=makeEmptyPicture((2*getWidth(pic)),(2*getHeight(pic)))
  w=getWidth(pic) 
  h=getHeight(pic) 
  copyInto(pic,wPic,0,0)
  darken(p)
  copyInto(p,wPic, w,0)
  grayscale(pic)
  copyInto(pic,wPic,0,h)  
  decreaseRed(p)
  copyInto(p,wPic,w,h)  
  show(wPic)