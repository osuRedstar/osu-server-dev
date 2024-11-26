from common.constants import bcolors
from objects import glob

def printServerStartHeader(asciiArt=True):
	"""
	Print server start message

	:param asciiArt: print BanchoBoat ascii art. Default: True
	:return:
	"""
	if asciiArt:
		print("{}           _                 __".format(bcolors.GREEN))
		print("          (_)              /  /")
		print("   ______ __ ____   ____  /  /____")
		print("  /  ___/  /  _  \\/  _  \\/  /  _  \\")
		print(" /  /  /  /  /_) /  /_) /  /  ____/")
		print("/__/  /__/  .___/  .___/__/ \\_____/")
		print("        /  /   /  /")
		print("       /__/   /__/\r\n")
		print("                          .. o  .")
		print("                         o.o o . o")
		print("                        oo...")
		print("                    __[]__")
		print("             ______/o_o_o_|__  everybody is gone :(")
		print("             \\\"\"\"\"\"\"\"\"\"\"\"\"\"\"/")
		print("              \\ . ..  .. . /")
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{}".format(bcolors.ENDC))

	""" printColored("> Welcome to pep.py osu!bancho server v{}".format(glob.VERSION), bcolors.GREEN)
	#printColored("> Made by the Debian team, custom fork by osu!thailand", bcolors.GREEN)
	printColored("> Made by the Redstar team, custom fork by osu!Debian, by custom fork by osu!thailand", bcolors.GREEN)
	printColored("> {}https://zxq.co/ripple/pep.py".format(bcolors.UNDERLINE), bcolors.GREEN)
	printColored("> Press CTRL+C to exit\n", bcolors.GREEN) """

	if asciiArt:
		printColored(" (                 (     ", bcolors.YELLOW)
		printColored(" )\\ )        *   ) )\\ )  ", bcolors.YELLOW)
		printColored("(()/(  (   ` )  /((()/(  ", bcolors.YELLOW)
		printColored(" /(_)) )\\   ( )(_))/(_)) ", bcolors.YELLOW)
		printColored("(_))  ((_) (_(_())(_))   ", bcolors.YELLOW)
		printColored("| |   | __||_   _|/ __|  ", bcolors.GREEN)
		printColored("| |__ | _|   | |  \\__ \\  ", bcolors.GREEN)
		printColored("|____||___|  |_|  |___/  \n", bcolors.GREEN)

	""" printColored("> Welcome to the Latest Essential Tatoe Server {}".format(glob.VERSION), bcolors.GREEN)
	printColored("> Common submodule v{}".format(glob.COMMON_VERSION), bcolors.GREEN)
	printColored("> Made by the Ripple team", bcolors.GREEN)
	printColored("> {}https://zxq.co/ripple/lets".format(bcolors.UNDERLINE), bcolors.GREEN)
	printColored("> Press CTRL+C to exit\n", bcolors.GREEN) """

	printColored("> Welcome to pep.py osu!bancho server v{} | Welcome to the Latest Essential Tatoe Server {}".format(glob.VERSION), bcolors.GREEN)
	printColored("> Made by the Redstar team, custom fork by osu!Debian, by custom fork by osu!thailand | Made by the Ripple team", bcolors.GREEN)
	printColored("> {}https://zxq.co/ripple/pep.py | https://zxq.co/ripple/lets".format(bcolors.UNDERLINE), bcolors.GREEN)
	printColored("> Press CTRL+C to exit\n", bcolors.GREEN)

def printNoNl(string):
	"""
	Print a string without \n at the end

	:param string: string to print
	:return:
	"""
	print(string, end="")

def printColored(string, color):
	"""
	Print a colored string

	:param string: string to print
	:param color: ANSI color code
	:return:
	"""
	print("{}{}{}".format(color, string, bcolors.ENDC))

def printError():
	"""
	Print a red "Error"

	:return:
	"""
	printColored("Error", bcolors.RED)

def printDone():
	"""
	Print a green "Done"

	:return:
	"""
	printColored("Done", bcolors.GREEN)

def printWarning():
	"""
	Print a yellow "Warning"

	:return:
	"""
	printColored("Warning", bcolors.YELLOW)

def printGetScoresMessage(message):
	printColored("[get_scores] {}".format(message), bcolors.PINK)

def printSubmitModularMessage(message):
	printColored("[submit_modular] {}".format(message), bcolors.YELLOW)

def printBanchoConnectMessage(message):
	printColored("[bancho_connect] {}".format(message), bcolors.YELLOW)

def printGetReplayMessage(message):
	printColored("[get_replay] {}".format(message), bcolors.PINK)

def printMapsMessage(message):
	printColored("[maps] {}".format(message), bcolors.PINK)

def printRippMessage(message):
	printColored("[ripp] {}".format(message), bcolors.GREEN)

# def printRippoppaiMessage(message):
# 	printColored("[rippoppai] {}".format(message), bcolors.GREEN)

def printWifiPianoMessage(message):
	printColored("[wifipiano] {}".format(message), bcolors.GREEN)

def printDebugMessage(message):
	printColored("[debug] {}".format(message), bcolors.BLUE)

def printScreenshotsMessage(message):
	printColored("[screenshots] {}".format(message), bcolors.YELLOW)

def printApiMessage(module, message):
	printColored("[{}] {}".format(module, message), bcolors.GREEN)