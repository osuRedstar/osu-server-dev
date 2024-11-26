"""Bancho packets data types"""
BYTE = 0
UINT16 = 1
SINT16 = 2
UINT32 = 3
SINT32 = 4
UINT64 = 5
SINT64 = 6
STRING = 7
FFLOAT = 8		# 'float' is a keyword
BBYTES = 9      # 'bytes' is a keyword
INT_LIST = 10   # TODO: Maybe there are some packets that still use uInt16 + uInt32 thing somewhere.

"""Lets packets data types"""
byte 	= 0
uInt16 	= 1
sInt16 	= 2
uInt32 	= 3
sInt32 	= 4
uInt64 	= 5
sInt64 	= 6
string 	= 7
ffloat	= 8
bbytes 	= 9
rawReplay = 10