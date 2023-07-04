import tinytuya
import argparse
#==================================================================================================
MainLight = tinytuya.OutletDevice() # You need to put your own device ID, IP and key here
Light2 = tinytuya.OutletDevice() 
#==================================================================================================
MainLight.set_version(3.3)
Light2.set_version(3.3)
#==================================================================================================
def get_all():
    s1 = MainLight.status()
    s2 = Light2.status()
    s1_string = f"Power Usage: {s1['dps']['18']}mA\nVoltage: {str(s1['dps']['20'])[:-1]}.{str(s1['dps']['20'])[-1]}V\nCurrent: {str(s1['dps']['19'])[:-1]}.{str(s1['dps']['19'])[-1]}W"
    s2_string = f"Power Usage: {s2['dps']['18']}mA\nVoltage: {str(s2['dps']['20'])[:-1]}.{str(s2['dps']['20'])[-1]}V\nCurrent: {str(s2['dps']['19'])[:-1]}.{str(s2['dps']['19'])[-1]}W"
    return s1_string, s2_string
#==================================================================================================
def get_status_of_all(): return MainLight.status()['dps']['1'], Light2.status()['dps']['1']
#==================================================================================================
def switch_light1():
    if MainLight.status()['dps']['1'] == True:
        MainLight.set_status(False)
    else:
        MainLight.set_status(True)
#==================================================================================================
def switch_light2():
    if Light2.status()['dps']['1'] == True:
        Light2.set_status(False)
    else:
        Light2.set_status(True)
    
