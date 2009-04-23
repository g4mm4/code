##################################
# Sebastien Duquette - 2009       #
#                                 #
# pidfork                         #
# spawns the command in argument  #
# and echoes the process id.      #
#                                 #
##################################

if [ $# -lt 1 ]; then
	echo -n "usage: $0 <command>";
	exit
fi
$*&
echo $!
exit
