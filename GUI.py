import CANoe
import time
import PySimpleGUI as sg
app=CANoe.CANoe()
app.Interactive = False
app.open_simulation("rbei_test.cfg")
app.start_Measurement()

sg.theme('SandyBeach')
sg.popup('Current Value of Power Mode is: ', str(app.get_EnvVar("EnvPowerMode")))
layout = [
    [sg.Text('Please enter Power mode Value')],
    [sg.Text('Power Mode', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
  
window = sg.Window('Python-Canoe', layout)
event, values = window.read()
x=int(values.get(0))
window.close()
print("The Power Mode is:" + str(app.get_EnvVar("EnvPowerMode")))
app.set_EnvVar("EnvPowerMode",x);
print("The Updated Power mode is:" + str(app.get_EnvVar("EnvPowerMode")))
app.stop_Measurement()

