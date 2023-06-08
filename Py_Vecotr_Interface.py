import CANoe
import sys
import time as t
from datetime import *

app=CANoe.CANoe()
app.Interactive = False
app.open_simulation("CANoe_Gen40_v12.cfg")
app.start_Measurement()

x = app.get_SysVar("CANPANEL","ONOFF")
if x !=1:
    app.set_SysVar("CANPANEL","ONOFF",1)
    t.sleep(0.1)
print("Ignition:" + str(app.get_SysVar("CANPANEL","ONOFF")))

app.set_SysVar("EEC1","EngSpeed",500.000)
print("The Engine Speed is set to 500 RPM")
app.set_SysVar("CCVS1","WheelBasedVehicleSpeed",10.000)
print("The Vehicle Speed is set to 10 km/h")
print("NOw...Reading the System State")
#SysState = app.application.GetBus("CAN").GetSignal(1,"EPSO1","SysState")
print("The System State is:" + str(app.get_SigVal(1,"EPSO1","SysState","CAN")))
SysState=app.get_SigVal(1,"EPSO1","SysState","CAN")
status="NA"
if SysState == 5.0:
    status=("Pass")
    print("Test Case Passed")
else:
    status=("Fail")
    print("Test Case Failed")

with open("Log/Log.csv", 'a') as log:
    log.write("{0},{1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),str(status)))
    print("Writing LOG File Completed")
    
app.stop_Measurement()
