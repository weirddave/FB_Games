from sikuli import *

Dawn_of_the_Dragons = "1371058319396.png"
DotD_Raid_Btn = "DotD_Raid_Btn.png"
DOTD_Active_Raids_Btn = "DotD_Active_Raids_Btn.png"
DOTD_Engage = "DotD_Engage_Raid_Btn.png"
DOTD_20 = "DotD_Attack_20_Btn.png"
DOTD_close = "DotD_Close_Popup_Btn.png"
DOTD_Quest = "DotD_Quest_Btn.png"
DOTD_QesstAttack = "DotD_Quest_Attack_Btn.png"
DOTD_AmbushFlee = "1371392032885.png"
DOTD_AmbushAttack = "DotD_Ambush_Attack_Btn.png"
DOTD_AmbushAttackHover = "DotD_Ambush_Attack_Hover_Btn.png"

def run(timeout):
    if exists(Dawn_of_the_Dragons, timeout):
        click(Dawn_of_the_Dragons)
        print("Dawn of the Dragons Clicked")
        if exists(DotD_Raid_Btn, timeout):
            click(DotD_Raid_Btn)
            print("DotD Raid Clicked")
            if exists(DOTD_Active_Raids_Btn, timeout):
                click(DOTD_Active_Raids_Btn)
                print("DotD Active Clicked")
                if exists(DOTD_Engage, timeout):
                    click(DOTD_Engage)
                    print("DotD Engage Clicked")
                    if exists(DOTD_20, timeout):
                        click(DOTD_20)
                        print("DotD 20 Clicked")
                        if exists(DOTD_close, timeout):
                            click(DOTD_close)
                            print("DotD Close Clicked")
        if exists(DOTD_Quest, timeout):
            click(DOTD_Quest)
            print("DotD Quest Clicked")
            if exists(DOTD_QesstAttack, timeout):
                click(DOTD_QesstAttack)
                print("DotD Quest Attack Clicked")
                if exists(DOTD_close, timeout):
                    click(DOTD_close)
                else:
                    if exists(DOTD_AmbushAttack, timeout):
                        click(DOTD_AmbushAttack)
                        print("DotD Ambush Attack Clicked")
                        while exists(DOTD_AmbushAttackHover, timeout):
                            click(DOTD_AmbushAttackHover)
                            print("DotD Ambush Attack Hover Clicked")
