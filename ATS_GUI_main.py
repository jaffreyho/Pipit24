from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import ATS_GUI_ui as ui

import sys
#import time

#from PyQt5 import QtWidgets, uic

from SCPI_Client import SCPI_Client
from SCPI_Init import INIT_SCPI_OBJECT
from SCPI_MODE_SWITCH import MODE_SWITCH_OBJECT
from SCPI_TRX_Control import CHANNEL_CTRL_OBJECT
from SCPI_Object import SCPI_INTERFACE_OBJECT
from SCPI_MODE_SWITCH import MODE_SWITCH_OBJECT

# add modules path
sys.path.append('..\\SCPI_Core')

class Main(QMainWindow, ui.Ui_MainWindow):
      
	def __init__(self):
			
			super().__init__()
			self.setupUi(self)

            #Initial_Button Check
			
			self.initial_btn = self.findChild(QtWidgets.QPushButton, 'initial_btn')
			self.initial_btn.clicked.connect(self.initial_btn_event)

			self.Mode_Select = self.findChild(QtWidgets.QComboBox, 'Mode_Select')
			self.Mode_Select.currentIndexChanged.connect(self.mode_comboBox_event)

			# Basic_Tab : TX Channel Control block

			self.TX_CH1_Enable = self.findChild(QtWidgets.QCheckBox, 'TX_CH1_Enable')
			self.TX_CH1_Enable.stateChanged.connect(self.tx_ch1_dis_event)

			self.TX_CH2_Enable = self.findChild(QtWidgets.QCheckBox, 'TX_CH2_Enable')
			self.TX_CH2_Enable.stateChanged.connect(self.tx_ch2_dis_event)

			self.TX_CH3_Enable = self.findChild(QtWidgets.QCheckBox, 'TX_CH3_Enable')
			self.TX_CH3_Enable.stateChanged.connect(self.tx_ch3_dis_event)

			self.TX_CH4_Enable = self.findChild(QtWidgets.QCheckBox, 'TX_CH4_Enable')
			self.TX_CH4_Enable.stateChanged.connect(self.tx_ch4_dis_event)

			self.TX_CH1_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_CH1_Gain')
			self.TX_CH1_Gain.valueChanged.connect(self.tx_ch1_gain_event)

			self.TX_CH2_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_CH2_Gain')
			self.TX_CH2_Gain.valueChanged.connect(self.tx_ch2_gain_event)

			self.TX_CH3_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_CH3_Gain')
			self.TX_CH3_Gain.valueChanged.connect(self.tx_ch3_gain_event)

			self.TX_CH4_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_CH4_Gain')
			self.TX_CH4_Gain.valueChanged.connect(self.tx_ch4_gain_event)

			self.TX_COM_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_COM_Gain')
			self.TX_COM_Gain.valueChanged.connect(self.tx_com_gain_event)

			self.TX_CH1_Phase = self.findChild(QtWidgets.QSpinBox, 'TX_CH1_Phase')
			self.TX_CH1_Phase.valueChanged.connect(self.tx_ch1_phase_event)

			self.TX_CH2_Phase = self.findChild(QtWidgets.QSpinBox, 'TX_CH2_Phase')
			self.TX_CH2_Phase.valueChanged.connect(self.tx_ch2_phase_event)

			self.TX_CH3_Phase = self.findChild(QtWidgets.QSpinBox, 'TX_CH3_Phase')
			self.TX_CH3_Phase.valueChanged.connect(self.tx_ch3_phase_event)

			self.TX_CH4_Phase = self.findChild(QtWidgets.QSpinBox, 'TX_CH4_Phase')
			self.TX_CH4_Phase.valueChanged.connect(self.tx_ch4_phase_event)

			self.TX_CH5_Enable = self.findChild(QtWidgets.QCheckBox, 'TX_CH5_Enable')
			self.TX_CH5_Enable.stateChanged.connect(self.tx_ch5_dis_event)

			self.TX_CH6_Enable = self.findChild(QtWidgets.QCheckBox, 'TX_CH6_Enable')
			self.TX_CH6_Enable.stateChanged.connect(self.tx_ch6_dis_event)

			self.TX_CH7_Enable = self.findChild(QtWidgets.QCheckBox, 'TX_CH7_Enable')
			self.TX_CH7_Enable.stateChanged.connect(self.tx_ch7_dis_event)

			self.TX_CH8_Enable = self.findChild(QtWidgets.QCheckBox, 'TX_CH8_Enable')
			self.TX_CH8_Enable.stateChanged.connect(self.tx_ch8_dis_event)

			self.TX_CH5_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_CH5_Gain')
			self.TX_CH5_Gain.valueChanged.connect(self.tx_ch5_gain_event)

			self.TX_CH6_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_CH6_Gain')
			self.TX_CH6_Gain.valueChanged.connect(self.tx_ch6_gain_event)

			self.TX_CH7_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_CH7_Gain')
			self.TX_CH7_Gain.valueChanged.connect(self.tx_ch7_gain_event)

			self.TX_CH8_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_CH8_Gain')
			self.TX_CH8_Gain.valueChanged.connect(self.tx_ch8_gain_event)

			self.TX_COM_Gain = self.findChild(QtWidgets.QSpinBox, 'TX_COM_Gain')
			self.TX_COM_Gain.valueChanged.connect(self.tx_com_gain_event)

			self.TX_CH5_Phase = self.findChild(QtWidgets.QSpinBox, 'TX_CH5_Phase')
			self.TX_CH5_Phase.valueChanged.connect(self.tx_ch5_phase_event)

			self.TX_CH6_Phase = self.findChild(QtWidgets.QSpinBox, 'TX_CH6_Phase')
			self.TX_CH6_Phase.valueChanged.connect(self.tx_ch6_phase_event)

			self.TX_CH7_Phase = self.findChild(QtWidgets.QSpinBox, 'TX_CH7_Phase')
			self.TX_CH7_Phase.valueChanged.connect(self.tx_ch7_phase_event)

			self.TX_CH8_Phase = self.findChild(QtWidgets.QSpinBox, 'TX_CH8_Phase')
			self.TX_CH8_Phase.valueChanged.connect(self.tx_ch8_phase_event)
				
	def TRX_Channel_Ctrl_Event(self, user_delay, mode, module):
			
				if mode == 1:
					if self.TX_CH1_Enable.isChecked() == True:
						#turn off
						ch1_switch = 1
					else:
						#turn on
						ch1_switch = 0
					if self.TX_CH2_Enable.isChecked() == True:
						ch2_switch = 1
					else:
						ch2_switch = 0
					if self.TX_CH3_Enable.isChecked() == True:
						ch3_switch = 1
					else:
						ch3_switch = 0
					if self.TX_CH4_Enable.isChecked() == True:
						ch4_switch = 1
					else:
						ch4_switch = 0
					if self.TX_CH5_Enable.isChecked() == True:
						ch5_switch = 1
					else:
						ch5_switch = 0
					if self.TX_CH6_Enable.isChecked() == True:
						ch6_switch = 1
					else:
						ch6_switch = 0
					if self.TX_CH7_Enable.isChecked() == True:
						ch7_switch = 1
					else:
						ch7_switch = 0
					if self.TX_CH8_Enable.isChecked() == True:
						ch8_switch = 1
					else:
						ch8_switch = 0

				ch1_gain = self.TX_CH1_Gain.value()
				ch2_gain = self.TX_CH2_Gain.value()
				ch3_gain = self.TX_CH3_Gain.value()
				ch4_gain = self.TX_CH4_Gain.value()
				ch5_gain = self.TX_CH5_Gain.value()
				ch6_gain = self.TX_CH6_Gain.value()
				ch7_gain = self.TX_CH7_Gain.value()
				ch8_gain = self.TX_CH8_Gain.value()
				com_gain = self.TX_COM_Gain.value()

				ch1_phase = self.TX_CH1_Phase.value()
				ch2_phase = self.TX_CH2_Phase.value()
				ch3_phase = self.TX_CH3_Phase.value()
				ch4_phase = self.TX_CH4_Phase.value()
				ch5_phase = self.TX_CH5_Phase.value()
				ch6_phase = self.TX_CH6_Phase.value()
				ch7_phase = self.TX_CH7_Phase.value()
				ch8_phase = self.TX_CH8_Phase.value()

				obj = SCPI_INTERFACE_OBJECT()
				obj.TRX_channel_ctrl(user_delay, mode, module, ch1_switch, ch2_switch, ch3_switch, ch4_switch,
										ch1_phase, ch2_phase, ch3_phase, ch4_phase, ch1_gain, ch2_gain, ch3_gain, ch4_gain, com_gain, ch5_switch, ch6_switch, ch7_switch, ch8_switch, ch5_phase, ch6_phase, ch7_phase, ch8_phase, ch5_gain, ch6_gain, ch7_gain, ch8_gain, com_gain)


	def initial_btn_event(self):
            obj = SCPI_INTERFACE_OBJECT()
            obj.Initial_ctrl()

	def mode_comboBox_event(self):
            obj = SCPI_INTERFACE_OBJECT()
            obj.Mode_Switch_ctrl(self.Mode_Select.currentIndex())
            print('Mode_Switch_event ' + str(self.Mode_Select.currentIndex()))
        
	def tx_ch1_dis_event(self):
		    self.TRX_Channel_Ctrl_Event(0, 1, 0)
		    #print('tx_ch1_dis_event')

	def tx_ch2_dis_event(self):
		    self.TRX_Channel_Ctrl_Event(0, 1, 0)
		    #print('tx_ch2_dis_event')

	def tx_ch3_dis_event(self):
		    self.TRX_Channel_Ctrl_Event(0, 1, 0)
		    #print('tx_ch3_dis_event')

	def tx_ch4_dis_event(self):
		    self.TRX_Channel_Ctrl_Event(0, 1, 0)
		    #print('tx_ch4_dis_event')

	def tx_ch5_dis_event(self):
		    self.TRX_Channel_Ctrl_Event(0, 1, 0)
		    #print('tx_ch5_dis_event')

	def tx_ch6_dis_event(self):
		    self.TRX_Channel_Ctrl_Event(0, 1, 0)
		    #print('tx_ch6_dis_event')

	def tx_ch7_dis_event(self):
		    self.TRX_Channel_Ctrl_Event(0, 1, 0)
		    #print('tx_ch7_dis_event')

	def tx_ch8_dis_event(self):
		    self.TRX_Channel_Ctrl_Event(0, 1, 0)
		    #print('tx_ch8_dis_event')
        
	def tx_ch1_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch1_gain_event')

	def tx_ch2_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch2_gain_event')

	def tx_ch3_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch3_gain_event')

	def tx_ch4_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch4_gain_event')

	def tx_ch5_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch5_gain_event')

	def tx_ch6_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch6_gain_event')

	def tx_ch7_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch7_gain_event')

	def tx_ch8_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch8_gain_event')

	def tx_com_gain_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_com_gain_event')

	def tx_ch1_phase_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch1_phase_event')

	def tx_ch2_phase_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch2_phase_event')

	def tx_ch3_phase_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch3_phase_event')

	def tx_ch4_phase_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch4_phase_event')

	def tx_ch5_phase_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch5_phase_event')

	def tx_ch6_phase_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch6_phase_event')
        
	def tx_ch7_phase_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch7_phase_event')

	def tx_ch8_phase_event(self):
			self.TRX_Channel_Ctrl_Event(0, 1, 0)
			#print('tx_ch8_phase_event')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

   

   

   