import sys
s =0
for arg in sys.argv[1:]:
    """One can type this program in the terminal and pass argument to it"""
    number =float(arg)
    s += number
print(s)
################################
s = sum([float(x) for x in sys.argv[1:]])
print("The sum of %s is %s" % (" ".join(sys.argv[1:]),s))
###################################
s0 = float(sys.argv[1])
v0 = float(sys.argv[2])
t = float(sys.argv[3])
a = float(sys.argv[4])
s = s0 + v0t + (v0*t) + (1/2)*a*t**2
######################################
parser = argparse.ArgumentParser()
parser.add_argument('--v0', '--initial_velocity', type = float, default=0.0, help='initial velocity', metavar='v')
parser.add_argument('--s0', '--initial_position',type = float, default = 0.0, help = 'initial position', metavar = 's')
parser.add_argument ( '--a', '--acceleration', type = float, default = 1.0, help = 'acceleration', metavar = 'a')
parser.add_argument ( '--t', '--time', type = float, default = 1.0, help = 'time', metavar = 'a')

args= parser.parse_args()
s = args.s0 + args.v0*args.t + 0.5*args.a*args.t*2
########################################################
if len(sys.argv) < 2:
    print("You failed to provide Celcius degrees as input on the command line!")
    sys.exit(1)
C = float(sys.argv[1])
F = 9.0*C/5 +32
print("%g C is %0.1fF" % (C,F))
##############################################################

try:
    C = float(sys.argv[1])
except:
    print("You failed to provide Celsius degrees as input on the command line!")
    sys.exit(1)
F = 9.0*C/5 + 32
print("%gC is %.1fF" % (C,F))
###################################################################

try:
    C = float(sys.argv[1])
except IndexError:
    print("Celsius degrees must be supplied on the command line")
    sys.exit(1)
except ValueError:
    print('celsius degrees must be a pure number, not %s' % sys.argv[1])
    sys.exit(1)
F = 9.0*C/5 + 32
print("%gC is %0.1fF" % (C,F))