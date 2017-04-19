from __future__ import division
import os
from PIL import Image
import re
import math



# current working directory
cwd = os.getcwd()

print cwd

count = 0

widths = [320, 480, 640, 768, 800, 960, 1024, 1136, 1280, 1366, 1440, 1536, 1600, 1680, 1920, 2048, 2560, 2880]

depths = [0.5, 1.5, 2, 3]

ratio = 0

heights = []

def getImage(dirname, filename):

  current = os.path.join(dirname, filename)

  image = Image.open(current)

  width = image.size[0]

  height = image.size[1]

  print "width ", width 

  print "height ", height 

  ratio = height / width

  del heights[:]

  for i in widths:

    heights.append(int(math.ceil(i * ratio)))

  print ratio

  print heights

  return ratio
  

def resizeImage(dirname, filename, ratio):

  current = os.path.join(dirname, filename)

  internalCount = 0

  print current

  print "opening ", current

  image = Image.open(current)

  for i in widths:

    print i, " x ", int(math.ceil(i * ratio))

    print "looping through widths"

    if (i != 2880):

      internalCount = internalCount + 1

      temp = image.copy().resize((i, int(math.ceil(i * ratio))), Image.ANTIALIAS)

      outputname = re.sub(r"_2880w\.jpg", "_" + str(i) + "w.jpg" , current)

      if filename != outputname:

        try:

          print "saving ", outputname

          temp.save(outputname, "JPEG", quality=100)

          print "saved ", internalCount, " files"

        except IOError:

          print "cannot convert", outputname

      # depths

      for depth in depths:

        print "looping through depths"

        print "depth = ", depth

        internalCount = internalCount + 1

        depthWidth = int(math.ceil(i * depth))

        depthHeight = int(math.ceil(math.ceil(i * ratio)) * depth)

        print "depthWidth = ", depthWidth, " x depthHeight = ", depthHeight

        tempDepth = image.copy().resize((depthWidth, depthHeight), Image.ANTIALIAS)

        depthOutputname = re.sub(r"_2880w\.jpg", "_" + str(i) + "w@" + re.sub(r"\." , ",", str(depth)) + "x.jpg" , current)

        if filename != depthOutputname:

          try:

            print "saving ", depthOutputname

            tempDepth.save(depthOutputname, "JPEG", quality=100)

            print "saved ", internalCount, " files"

          except IOError:

            print "cannot convert", depthOutputname

     

# '.' = start in the current directory
for (dirname, dirs, files) in os.walk('.'):

  for filename in files:

    if filename.endswith('_2880w.jpg'):

      count = count + 1

      ratio = getImage(dirname, filename)

      resizeImage(dirname, filename, ratio)





print 'Files: ', count

