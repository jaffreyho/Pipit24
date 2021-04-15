import os
import sys
import argparse

from SCPI_Client import SCPI_Client

class CHANNEL_CTRL_OBJECT(object):

	IC_num: int
	mode: int
	module: int

	channel_1_switch = 0
	channel_2_switch = 0
	channel_3_switch = 0
	channel_4_switch = 0
	channel_5_switch = 0
	channel_6_switch = 0
	channel_7_switch = 0
	channel_8_switch = 0

	channel_1_phase_step = 0
	channel_2_phase_step = 0
	channel_3_phase_step = 0
	channel_4_phase_step = 0
	channel_5_phase_step = 0
	channel_6_phase_step = 0
	channel_7_phase_step = 0
	channel_8_phase_step = 0

	channel_1_gain_step = 0
	channel_2_gain_step = 0
	channel_3_gain_step = 0
	channel_4_gain_step = 0
	channel_5_gain_step = 0
	channel_6_gain_step = 0
	channel_7_gain_step = 0
	channel_8_gain_step = 0
	channel_com1_gain_step = 0
	channel_com2_gain_step = 0

	def __init__(self):
		self.IC_num = 2
		self.mode = 1
		self.chain_th = 1

	def serial_mode(self):
		cmd = "MODULE_CTRL_ " + str(self.IC_num) + \
			"," + str(self.mode) + \
			"," + str(self.chain_th) + \
			"," + str(self.channel_1_switch) + \
			"," + str(self.channel_2_switch) + \
			"," + str(self.channel_3_switch) + \
			"," + str(self.channel_4_switch) + \
			"," + str(self.channel_1_phase_step) + \
			"," + str(self.channel_2_phase_step) + \
			"," + str(self.channel_3_phase_step) + \
			"," + str(self.channel_4_phase_step) + \
			"," + str(self.channel_1_gain_step) + \
			"," + str(self.channel_2_gain_step) + \
			"," + str(self.channel_3_gain_step) + \
			"," + str(self.channel_4_gain_step) + \
			"," + str(self.channel_com1_gain_step) + \
			"," + str(self.channel_1_switch) + \
            "," + str(self.channel_2_switch) + \
            "," + str(self.channel_3_switch) + \
            "," + str(self.channel_4_switch) + \
            "," + str(self.channel_1_phase_step) + \
            "," + str(self.channel_2_phase_step) + \
            "," + str(self.channel_3_phase_step) + \
            "," + str(self.channel_4_phase_step) + \
            "," + str(self.channel_1_gain_step) + \
            "," + str(self.channel_2_gain_step) + \
            "," + str(self.channel_3_gain_step) + \
            "," + str(self.channel_4_gain_step) + \
            "," + str(self.channel_com2_gain_step) + \
			" \n\r"

		print("Send: \'%s\'" %cmd)
		return cmd

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	parser.add_argument("--mode", help="Mode : 1 - TX_CTRL , 2 - RX_CTRL", type=int)

	parser.add_argument("--chip1_ch1_switch", help="Channel_1 switch : 0 - on , 1 - off", type=int)
	parser.add_argument("--chip1_ch2_switch", help="Channel_2 switch : 0 - on , 1 - off", type=int)
	parser.add_argument("--chip1_ch3_switch", help="Channel_3 switch : 0 - on , 1 - off", type=int)
	parser.add_argument("--chip1_ch4_switch", help="Channel_4 switch : 0 - on , 1 - off", type=int)
	parser.add_argument("--chip1_ch1_phase", help="Channel_1 phase step : in range(0,63)", type=int)
	parser.add_argument("--chip1_ch2_phase", help="Channel_2 phase step : in range(0,63)", type=int)
	parser.add_argument("--chip1_ch3_phase", help="Channel_3 phase step : in range(0,63)", type=int)
	parser.add_argument("--chip1_ch4_phase", help="Channel_4 phase step : in range(0,63)", type=int)
	parser.add_argument("--chip1_ch1_gain", help="Channel_1 gain step : in range(0,15)", type=int)
	parser.add_argument("--chip1_ch2_gain", help="Channel_2 gain step : in range(0,15)", type=int)
	parser.add_argument("--chip1_ch3_gain", help="Channel_3 gain step : in range(0,15)", type=int)
	parser.add_argument("--chip1_ch4_gain", help="Channel_4 gain step : in range(0,15)", type=int)
	parser.add_argument("--chip1_com_gain", help="Channel_com gain step : in range(0,15)", type=int)

	parser.add_argument("--chip2_ch1_switch", help="Channel_1 switch : 0 - on , 1 - off", type=int)
	parser.add_argument("--chip2_ch2_switch", help="Channel_2 switch : 0 - on , 1 - off", type=int)
	parser.add_argument("--chip2_ch3_switch", help="Channel_3 switch : 0 - on , 1 - off", type=int)
	parser.add_argument("--chip2_ch4_switch", help="Channel_4 switch : 0 - on , 1 - off", type=int)
	parser.add_argument("--chip2_ch1_phase", help="Channel_1 phase step : in range(0,63)", type=int)
	parser.add_argument("--chip2_ch2_phase", help="Channel_2 phase step : in range(0,63)", type=int)
	parser.add_argument("--chip2_ch3_phase", help="Channel_3 phase step : in range(0,63)", type=int)
	parser.add_argument("--chip2_ch4_phase", help="Channel_4 phase step : in range(0,63)", type=int)
	parser.add_argument("--chip2_ch1_gain", help="Channel_1 gain step : in range(0,15)", type=int)
	parser.add_argument("--chip2_ch2_gain", help="Channel_2 gain step : in range(0,15)", type=int)
	parser.add_argument("--chip2_ch3_gain", help="Channel_3 gain step : in range(0,15)", type=int)
	parser.add_argument("--chip2_ch4_gain", help="Channel_4 gain step : in range(0,15)", type=int)
	parser.add_argument("--chip2_com_gain", help="Channel_com gain step : in range(0,15)", type=int)
	args = parser.parse_args()

	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)

	channel_ctrl = CHANNEL_CTRL_OBJECT()

	channel_ctrl.mode = args.mode
	channel_ctrl.module = 0
	channel_ctrl.channel_1_switch = args.chip1_ch1_switch
	channel_ctrl.channel_2_switch = args.chip1_ch2_switch
	channel_ctrl.channel_3_switch = args.chip1_ch3_switch
	channel_ctrl.channel_4_switch = args.chip1_ch4_switch
	channel_ctrl.channel_1_phase_step = args.chip1_ch1_phase
	channel_ctrl.channel_2_phase_step = args.chip1_ch2_phase
	channel_ctrl.channel_3_phase_step = args.chip1_ch3_phase
	channel_ctrl.channel_4_phase_step = args.chip1_ch4_phase
	channel_ctrl.channel_1_gain_step = args.chip1_ch1_gain
	channel_ctrl.channel_2_gain_step = args.chip1_ch2_gain
	channel_ctrl.channel_3_gain_step = args.chip1_ch3_gain
	channel_ctrl.channel_4_gain_step = args.chip1_ch4_gain
	channel_ctrl.channel_com1_gain_step = args.chip1_com_gain

	channel_ctrl.channel_5_switch = args.chip2_ch1_switch
	channel_ctrl.channel_6_switch = args.chip2_ch2_switch
	channel_ctrl.channel_7_switch = args.chip2_ch3_switch
	channel_ctrl.channel_8_switch = args.chip2_ch4_switch
	channel_ctrl.channel_5_phase_step = args.chip2_ch1_phase
	channel_ctrl.channel_6_phase_step = args.chip2_ch2_phase
	channel_ctrl.channel_7_phase_step = args.chip2_ch3_phase
	channel_ctrl.channel_8_phase_step = args.chip2_ch4_phase
	channel_ctrl.channel_5_gain_step = args.chip2_ch1_gain
	channel_ctrl.channel_6_gain_step = args.chip2_ch2_gain
	channel_ctrl.channel_7_gain_step = args.chip2_ch3_gain
	channel_ctrl.channel_8_gain_step = args.chip2_ch4_gain
	channel_ctrl.channel_com2_gain_step = args.chip2_com_gain

	client = SCPI_Client("192.168.100.111")

	if client.Init_SCPI_client() == False:
		os.system("pause")
		sys.exit()

	CMD = channel_ctrl.serial_mode()
	recv = client.SendCmdThenWaitRSP(CMD, 0)
	print(recv)



