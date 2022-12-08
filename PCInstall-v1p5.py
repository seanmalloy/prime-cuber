#-----------------------------------------------------------------------------
# Title:        PrimeCuber Installer
#
# Author:       David Gilday
#
# Copyright:    (C) 2020 David Gilday
#
# Website:      http://mindcuber.com
#
# Version:      v1p5
#
# Modified:     $Date: 2020-12-27 09:41:03 +0000 (Sun, 27 Dec 2020) $
#
# Revision:     $Revision: 7806 $
#
# Usage:
#
#   This software may be used for any non-commercial purpose providing
#   that the original author is acknowledged.
#
# Disclaimer:
#
#   This software is provided 'as is' without warranty of any kind, either
#   express or implied, including, but not limited to, the implied warranties
#   of fitness for a purpose, or the warranty of non-infringement.
#
#-----------------------------------------------------------------------------
# Purpose:      PrimeCuber-v1p5 software installer
#-----------------------------------------------------------------------------
#
# Note:
#   This program must be run once to install modules and data files
#   that will allow the main program, PrimeCuber-v1p5, to run
#
#-----------------------------------------------------------------------------

from spike import LightMatrix, Speaker
lm = LightMatrix()
lm.show_image('SQUARE')
sp = Speaker()
sp.beep(72)

import os, umachine, ubinascii

version = "v1p5"

# Remove any files from older versions
for fn in os.listdir("/"):
    if len(fn) > 10:
        ver = None
        if fn[-3:] == ".py" and (
            fn[:-7] == "pccolors_" or
            fn[:-7] == "pcsolver_" or
            fn[:-7] == "primecuber_"
            ):
            ver = fn[-7:-3]
        elif fn[-4:] == ".bin" and (
            fn[:-8] == "pcmtab1_" or
            fn[:-8] == "pcmtab4_"
            ):
            ver = fn[-8:-4]
        if ver != None and ver < version:
            print("DELETING: "+fn)
            os.unlink(fn)

def file_exists(fn):
    try:
        ok = os.stat(fn) != None
    except:
        ok = False
    return ok

# Install PrimeCuber v1p5 files
prj = "/projects/"
found = 0
with open(prj+".slots","r") as f:
    slots = eval(f.read())
for s in slots:
    base = prj+str(slots[s]['id'])
    # Filename used by latest hub OS
    fn = base+"/__init__.py"
    if not file_exists(fn):
        # Try filename used by older versions of hub OS
        fn = base+".py"
    if file_exists(fn):
        with open(fn) as f:
            for i in range(3):
                l = f.readline()
                if l == "#PRIMECUBER_FILES_V1P5#\n":
                    print("SLOT: "+str(s)+" "+fn+" "+str(os.stat(fn)[6])+"B")
                    found += 1
                    of = None
                    n = 0
                    for l in f:
                        if of != None:
                            if l[0:5] == "#====":
                                of.close()
                                of = None
                                print("SAVED: "+ofn+" "+str(os.stat(ofn)[6])+"B")
                            else:
                                of.write(ubinascii.a2b_base64(l[1:-1]))
                                n += 1
                                if n % 50 == 0:
                                    lm.show_image('CLOCK'+str(1+(int(n/50)%12)))
                        elif l[:5] == "#FILE":
                            ofn = l[5:-1]
                            sp.beep(67)
                            of = open(ofn, 'wb')
                    if of != None:
                        # Missing end of file
                        of.close()
                        print("ERROR: end file marker expected")
                        print("DELETING: "+ofn)
                        ofn.unlink()
os.sync()
if found > 0:
    sp.beep(72)
    msg = "PrimeCuber v1p5 files installed"
    print("FINISHED "+msg)
    lm.write(msg)
    umachine.reset()
else:
    msg = "ERROR: no files found to install"
    print(msg)
    lm.write(msg)

raise SystemExit

# END

