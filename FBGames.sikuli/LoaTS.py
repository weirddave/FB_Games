from sikuli import *

LoaTS = "1371392378102.png"
LoaTS_ClosePopup = "1371392881008.png"
LoaTS_Raid_Btn = "1371392474074.png"
LoaTS_Active_Btn = "1371394019529.png"
LoaTS_Engage_Btn = "1371394054844.png"
LoaTS_20 = "1371394089787.png"
LoaTS_X1 = "1371394138504.png"
LoaTS_Mission_Btn = "1371394205529.png"
LoaTS_Engage2 = "1371394266035.png"
LoaTS_X2 = "1371394987182.png"
LoaTS_Bank = "1371394343709.png"

def run(timeout):
    if exists(LoaTS, timeout):
        click(LoaTS)
        print("LoaTS Clicked")
        if exists(LoaTS_ClosePopup, timeout):
            click(LoaTS_ClosePopup)
            print("LoaTS closed popup")
        if exists(LoaTS_Raid_Btn, timeout):
            click(LoaTS_Raid_Btn)
            print("LoaTD Raid Clicked")
            if exists(LoaTS_Active_Btn, timeout):
                click(LoaTS_Active_Btn)
                print("LoaTD Active Clicked")
                if exists(LoaTS_Engage_Btn, timeout):
                    click(LoaTS_Engage_Btn)
                    print("LoaTD Engage Clicked")
                    if exists(LoaTS_20, timeout):
                        click(LoaTS_20)
                        print("LoaTD 20 Clicked")
                        if exists(LoaTS_X1, timeout):
                            click(LoaTS_X1)
                            print("LoaTD close Clicked")
        if exists(LoaTS_Mission_Btn, timeout):
            click(LoaTS_Mission_Btn)
            print("LoaTD Mission Clicked")
            if exists(LoaTS_Engage2, timeout):
                click(LoaTS_Engage2)
                print("LoaTD Engage Clicked")
                if exists(LoaTS_X2, timeout):
                    click(LoaTS_X2)
                    print("LoaTD close Clicked")
        if exists(LoaTS_Bank, timeout):
            click(LoaTS_Bank)
            print("LoaTD Banked")
