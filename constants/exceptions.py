from common.log import logUtils as log

class invalidArgumentsException(Exception): #중복
	def __init__(self, handler):
		log.warning("{} - Invalid arguments".format(handler))

class loginFailedException(Exception):
	def __init__(self, handler, who):
		log.warning("{} - {}'s Login failed".format(handler, who))

class userBannedException(Exception):
	def __init__(self, handler, who):
		log.warning("{} - {} is banned".format(handler, who))

class userLockedException(Exception):
	def __init__(self, handler, who):
		log.warning("{} - {} is locked".format(handler, who))

class noBanchoSessionException(Exception):
	def __init__(self, handler, who, ip):
		log.warning("{handler} - {username} has tried to submit a score from {ip} without an active bancho session from that ip. If this happens often, {username} is trying to use a score submitter.".format(handler=handler, ip=ip, username=who), "bunker")

class osuApiFailException(Exception):
	def __init__(self, handler):
		log.warning("{} - Invalid data from osu!api".format(handler))

class fileNotFoundException(Exception):
	def __init__(self, handler, f):
		log.warning("{} - File not found ({})".format(handler, f))

class ppCustomBeatmap(Exception):
	pass

class invalidBeatmapException(Exception):
	pass

class unsupportedGameModeException(Exception):
	pass

class beatmapTooLongException(Exception):
	def __init__(self, handler):
		log.warning("{} - Requested beatmap is too long.".format(handler))

class need2FAException(Exception): #중복
	def __init__(self, handler, who, ip):
		log.warning("{} - 2FA check needed for user {} ({})".format(handler, who, ip))

class noAPIDataError(Exception):
	pass

class scoreNotFoundError(Exception):
	pass

class ppCalcException(Exception):
	def __init__(self, exception):
		self.exception = exception

####################################################################################################

class loginFailedException_pep(Exception):
	pass

class loginBannedException(Exception):
	pass

class tokenNotFoundException(Exception):
	pass

class channelNoPermissionsException(Exception):
	pass

class channelUnknownException(Exception):
	pass

class channelModeratedException(Exception):
	pass

class noAdminException(Exception):
	pass

class commandSyntaxException(Exception):
	pass

class banchoConfigErrorException(Exception):
	pass

class banchoMaintenanceException(Exception):
	pass

class moderatedPMException(Exception):
	pass

class userNotFoundException(Exception):
	pass

class alreadyConnectedException(Exception):
	pass

class stopSpectating(Exception):
	pass

class matchWrongPasswordException(Exception):
	pass

class matchNotFoundException(Exception):
	pass

class matchJoinErrorException(Exception):
	pass

class matchCreateError(Exception):
	pass

class banchoRestartingException(Exception):
	pass

class apiException(Exception):
	pass

""" class invalidArgumentsException(Exception):
	pass """

class messageTooLongWarnException(Exception):
	pass

class messageTooLongException(Exception):
	pass

class userSilencedException(Exception):
	pass

""" class need2FAException(Exception):
	pass """

class userRestrictedException(Exception):
	pass

class haxException(Exception):
	pass

class forceUpdateException(Exception):
	pass

class loginCheatClientsException(Exception):
	pass

class loginLockedException(Exception):
	pass

class unknownStreamException(Exception):
	pass

class userTournamentException(Exception):
	pass

class userAlreadyInChannelException(Exception):
	pass

class userNotInChannelException(Exception):
	pass

class missingReportInfoException(Exception):
	pass

class invalidUserException(Exception):
	pass

class wrongChannelException(Exception):
	pass

class periodicLoopException(Exception):
	pass