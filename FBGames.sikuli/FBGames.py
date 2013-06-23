runhours = 0.01
intervalmins = 5

FB_Tab = "FB_Tab_Logo.png"
FB_Logo = "FB_Logo.png"

timeout = 10
waitsecs = intervalmins *60
count = runhours*60 / intervalmins

Settings.ObserveScanRate = 0.5
setFindFailedResponse(SKIP)
Settings.ActionLogs = False
Settings.MinSimilarity = 0.9
import DotD
import LoaTS
import time
#Settings.OcrTextSearch = True
#Settings.OcrTextRead = True

Region(1,1,1250,1070)
oldtime = time.clock()

while (count>0):
    count = count -1
    print(time.asctime())
    if exists(FB_Tab, timeout):
        try:
            click(FB_Tab)
            if exists(FB_Logo, timeout):
                click(FB_Logo)
                DotD.run(timeout)
                if exists(FB_Logo, timeout):
                    click(FB_Logo)
                else:
                    print("No FB Logo after DotD!")
                LoaTS.run(timeout)
                if exists(FB_Logo, timeout):
                    click(FB_Logo)
                else:
                    print("No FB Logo after LoaTS!")
            else:
                print("No FB Logo after DotD!")
        except:
            pass
    timediff = int(time.clock() - oldtime)
    print (timediff)
    if (timediff < waitsecs) and (count>0):
        wait (waitsecs - timediff)
    oldtime = oldtime + waitsecs
print ("clean exit")




#        print("["+Region(343,256,13,17).text()+"]")
#        print("["+Region(331,239,63,15).text()+"]")

