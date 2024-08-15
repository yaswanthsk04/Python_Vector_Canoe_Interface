# Python_Vector_Canoe_Interface
# Readme

This project was developed as a Werkstudent project. This project mainly focuses on developing a Python based GUI to control the Enviornmental and System Variables in CANoe. 

Ususlly, when a tester or a Developer wants to test some feature, they will have to set some necessary precoditions for the ECU via simulation. This will be done by manually inputing the values into CANoe.

My task was to develop a GUI which posses a preset of various pre-defined conditions.

For example if preseet 1 is selected in the GUI, the following will automatically be set in the CANoe and the data will be transmitted to the ECU via XRP & CAN.
  1. Ignition On
  2. Engine Speed 4500 RPM
  3. Brake Switch Off.

#REQUIREMENTS:
1.	Python (Version>3.6)
2.	Py-Win32 Library (Version>223)
3.	CANoe Library 

#INSTALLATION INSTRUCTIONS:
1.	Python:
Link to Download Python: https://www.python.org/downloads/
2.	Py-Win32 Library:
Pip Code to Install PY-Win32 Library: pip install pywin32
Exe Download link: https://github.com/mhammond/pywin32/releases
3.	CANoe Library:
Pip Code to Install CANoe Library: pip install Python-CANoe

#Methodology:
	Vector Tools CANoe provide the users with WIN32 COM port to access the software.  Using this COM port we can call CANoe functions from PYTHON scripts.

#IMPLEMENTATION:
	CANoe Library Provide various functions that can be used to call specific functions in CANoe such as Read, Write System and Environmental Variables. 
1.	The Function to read Environmental Variables:
get_EnvVar (variable_name)

2.	The function to write Environmental Variables:
set_EnvVar (variable_name, value_to_be_set)

3.	The function to read System variables:
get_SysVar (namespace_name, systemvariable_name)
4.	The function to Write System Variables:
	set_SysVar (namespace_name, systemvarible_name, value_to_be_set)

5.	The function to Read Signal Value:
get_SigVal (channel_number, message_name, signal_name, bus_type)

A conceptual working demo can be seen here: https://drive.google.com/file/d/11jyu9oQ1Z_KTbQMc5r-SE10qCPjTwyVn/view?usp=sharing
