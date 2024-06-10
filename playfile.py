#can (hopefully) be imported to play the output .mp3 file
#be sure to install the playsound3 package
from playsound3 import playsound
class reader:
  def playFile(filepath):
    playsound(filepath)
