'''
**********************************************************************
* Filename    : tables.py
* Description : Charactor tables and pictures table for 8*8 dot matrix
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-10-18    New release
**********************************************************************
'''

charactors = {
	"A" : [
		0b00000000,
		0b00011000,
		0b00100100,
		0b00100100,
		0b00111100,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"a" : [
		0b00000000,
		0b00000000,
		0b00011100,
		0b00100100,
		0b00100100,
		0b00011100,
		0b00000000,
		0b00000000,
	],
	"B" : [
		0b00000000,
		0b00111000,
		0b00100100,
		0b00111000,
		0b00100100,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"b" : [
		0b00000000,
		0b00100000,
		0b00111000,
		0b00100100,
		0b00100100,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"C" : [
		0b00000000,
		0b00011000,
		0b00100000,
		0b00100000,
		0b00100000,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"c" : [
		0b00000000,
		0b00000000,
		0b00011000,
		0b00100000,
		0b00100000,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"D" : [
		0b00000000,
		0b00111000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"d" : [
		0b00000000,
		0b00000100,
		0b00011100,
		0b00100100,
		0b00100100,
		0b00011100,
		0b00000000,
		0b00000000,
	],
	"E" : [
		0b00000000,
		0b00111000,
		0b00100000,
		0b00111000,
		0b00100000,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"e" : [
		0b00000000,
		0b00000000,
		0b00011000,
		0b00101100,
		0b00110000,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"F" : [
		0b00000000,
		0b00111000,
		0b00100000,
		0b00111000,
		0b00100000,
		0b00100000,
		0b00000000,
		0b00000000,
	],
	"f" : [
		0b00000000,
		0b00001000,
		0b00010000,
		0b00111000,
		0b00010000,
		0b00010000,
		0b00000000,
		0b00000000,
	],
	"G" : [
		0b00000000,
		0b00011100,
		0b00100000,
		0b00101100,
		0b00100100,
		0b00011100,
		0b00000000,
		0b00000000,
	],
	"g" : [
		0b00000000,
		0b00000000,
		0b00011100,
		0b00100100,
		0b00100100,
		0b00011100,
		0b00000100,
		0b00011000,
	],
	"H" : [
		0b00000000,
		0b00100100,
		0b00100100,
		0b00111100,
		0b00100100,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"h" : [
		0b00000000,
		0b00100000,
		0b00111000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"I" : [
		0b00000000,
		0b00111000,
		0b00010000,
		0b00010000,
		0b00010000,
		0b00111000,
		0b00000000,
		0b00000000,
		0b00000000,
	],
	"i" : [
		0b00000000,
		0b00100000,
		0b00000000,
		0b00100000,
		0b00100000,
		0b00100000,
		0b00000000,
		0b00000000,
		0b00000000,
	],
	"J" : [
		0b00000000,
		0b00001100,
		0b00000100,
		0b00000100,
		0b00100100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"j" : [
		0b00000000,
		0b00000100,
		0b00000000,
		0b00000100,
		0b00000100,
		0b00000100,
		0b00001000,
		0b00000000,
	],
	"K" : [
		0b00000000,
		0b00100100,
		0b00101000,
		0b00110000,
		0b00101000,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"k" : [
		0b00000000,
		0b00100000,
		0b00100100,
		0b00101000,
		0b00111000,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"L" : [
		0b00000000,
		0b00100000,
		0b00100000,
		0b00100000,
		0b00100000,
		0b00111100,
		0b00000000,
		0b00000000,
	],
	"l" : [
		0b00000000,
		0b00110000,
		0b00010000,
		0b00010000,
		0b00010000,
		0b00010000,
		0b00000000,
		0b00000000,
	],
	"M" : [
		0b00000000,
		0b00100010,
		0b00110110,
		0b00101010,
		0b00100010,
		0b00100010,
		0b00000000,
		0b00000000,
	],
	"m" : [
		0b00000000,
		0b00000000,
		0b00111100,
		0b00101010,
		0b00101010,
		0b00101010,
		0b00000000,
		0b00000000,
	],
	"N" : [
		0b00000000,
		0b00100100,
		0b00110100,
		0b00101100,
		0b00100100,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"n" : [
		0b00000000,
		0b00000000,
		0b00111000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"O" : [
		0b00000000,
		0b00011000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"o" : [
		0b00000000,
		0b00000000,
		0b00011000,
		0b00100100,
		0b00100100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"P" : [
		0b00000000,
		0b00111000,
		0b00100100,
		0b00111000,
		0b00100000,
		0b00100000,
		0b00000000,
		0b00000000,
	],
	"p" : [
		0b00000000,
		0b00000000,
		0b00111000,
		0b00100100,
		0b00111000,
		0b00100000,
		0b00100000,
		0b00000000,
	],
	"Q" : [
		0b00000000,
		0b00011000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00011000,
		0b00000100,
		0b00000000,
	],
	"q" : [
		0b00000000,
		0b00000000,
		0b00011100,
		0b00100100,
		0b00011100,
		0b00000100,
		0b00000100,
		0b00000000,
	],
	"R" : [
		0b00000000,
		0b00111000,
		0b00100100,
		0b00100100,
		0b00111000,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"r" : [
		0b00000000,
		0b00000000,
		0b00101000,
		0b00110000,
		0b00100000,
		0b00100000,
		0b00000000,
		0b00000000,
	],
	"S" : [
		0b00000000,
		0b00011100,
		0b00100000,
		0b00011000,
		0b00000100,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"s" : [
		0b00000000,
		0b00000000,
		0b00011100,
		0b00110000,
		0b00001100,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"T" : [
		0b00000000,
		0b00111000,
		0b00010000,
		0b00010000,
		0b00010000,
		0b00010000,
		0b00000000,
		0b00000000,
	],
	"t" : [
		0b00000000,
		0b00010000,
		0b00111000,
		0b00010000,
		0b00010000,
		0b00001000,
		0b00000000,
		0b00000000,
	],
	"U" : [
		0b00000000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"u" : [
		0b00000000,
		0b00000000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00011100,
		0b00000000,
		0b00000000,
	],
	"V" : [
		0b00000000,
		0b00100100,
		0b00100100,
		0b00101000,
		0b00101000,
		0b00010000,
		0b00000000,
		0b00000000,
	],
	"v" : [
		0b00000000,
		0b00000000,
		0b00100100,
		0b00100100,
		0b00101000,
		0b00010000,
		0b00000000,
		0b00000000,
	],
	"W" : [
		0b00000000,
		0b00100010,
		0b00101010,
		0b00101010,
		0b00101010,
		0b00010100,
		0b00000000,
		0b00000000,
	],
	"w" : [
		0b00000000,
		0b00000000,
		0b00101010,
		0b00101010,
		0b00010100,
		0b00010100,
		0b00000000,
		0b00000000,
	],
	"X" : [
		0b00000000,
		0b00100100,
		0b00100100,
		0b00011000,
		0b00100100,
		0b00100100,
		0b00000000,
		0b00000000,
	],
	"x" : [
		0b00000000,
		0b00000000,
		0b00101000,
		0b00010000,
		0b00010000,
		0b00101000,
		0b00000000,
		0b00000000,
	],
	"Y" : [
		0b00000000,
		0b00100100,
		0b00100100,
		0b00011100,
		0b00000100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"y" : [
		0b00000000,
		0b00000000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00011100,
		0b00000100,
		0b00011000,
	],
	"Z" : [
		0b00000000,
		0b00111000,
		0b00001000,
		0b00010000,
		0b00100000,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"z" : [
		0b00000000,
		0b00000000,
		0b00111100,
		0b00001000,
		0b00010000,
		0b00111100,
		0b00000000,
		0b00000000,
	],
	"1" : [
		0b00000000,
		0b00010000,
		0b00110000,
		0b00010000,
		0b00010000,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"2" : [
		0b00000000,
		0b00111000,
		0b00000100,
		0b00011000,
		0b00100000,
		0b00111100,
		0b00000000,
		0b00000000,
	],
	"3" : [
		0b00000000,
		0b00111000,
		0b00000100,
		0b00011000,
		0b00000100,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"4" : [
		0b00000000,
		0b00001000,
		0b00011000,
		0b00101000,
		0b00111100,
		0b00001000,
		0b00000000,
		0b00000000,
	],
	"5" : [
		0b00000000,
		0b00111100,
		0b00100000,
		0b00111000,
		0b00000100,
		0b00111000,
		0b00000000,
		0b00000000,
	],
	"6" : [
		0b00000000,
		0b00011000,
		0b00100000,
		0b00111000,
		0b00100100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"7" : [
		0b00000000,
		0b00111100,
		0b00000100,
		0b00001000,
		0b00010000,
		0b00010000,
		0b00000000,
		0b00000000,
	],
	"8" : [
		0b00000000,
		0b00011000,
		0b00100100,
		0b00011000,
		0b00100100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"9" : [
		0b00000000,
		0b00011000,
		0b00100100,
		0b00011100,
		0b00000100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"0" : [
		0b00000000,
		0b00011000,
		0b00100100,
		0b00100100,
		0b00100100,
		0b00011000,
		0b00000000,
		0b00000000,
	],
	"!" : [
		0b00000000,
		0b00100000,
		0b00100000,
		0b00100000,
		0b00000000,
		0b00100000,
		0b00000000,
		0b00000000,
	],
	"?" : [
		0b00000000,
		0b00111000,
		0b00000100,
		0b00011000,
		0b00000000,
		0b00010000,
		0b00000000,
		0b00000000,
	],
	"," : [
		0b00000000,
		0b00000000,
		0b00000000,
		0b00000000,
		0b00000000,
		0b00010000,
		0b00100000,
		0b00000000,
	],
	"." : [
		0b00000000,
		0b00000000,
		0b00000000,
		0b00000000,
		0b00000000,
		0b00100000,
		0b00000000,
		0b00000000,
	],
	"<" : [
		0b00000000,
		0b00001000,
		0b00010000,
		0b00100000,
		0b00010000,
		0b00001000,
		0b00000000,
		0b00000000,
	],
	">" : [
		0b00000000,
		0b00100000,
		0b00010000,
		0b00001000,
		0b00010000,
		0b00100000,
		0b00000000,
		0b00000000,
	],
}

picture = {
	"heart":[
	0b00000000,
	0b00000000,
	0b00110110,
	0b01001001,
	0b01000001,
	0b00100010,
	0b00010100,
	0b00001000,
         ],


	"smile":[
	0b00000000,
	0b01000010,
	0b10100101,
	0b00000000,
	0b00000000,
	0b01000010,
	0b00111100,
	0b00000000,
	],
	"creeper":[
	0b11111111,
	0b11111111,
	0b10011001,
	0b10011001,
	0b11100111,
	0b11000011,
	0b11000011,
	0b11011011,
	],
}
