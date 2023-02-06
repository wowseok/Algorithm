import sys

jh = sys.stdin.readline().rstrip()
doctor = sys.stdin.readline().rstrip()
if len(jh) >= len(doctor):
    print('go')
else:
    print('no')