#-----------------------------------------------------------------------------
# Title:        PrimeCuber
#
# Author:       David Gilday
#
# Copyright:    (C) 2020 David Gilday
#
# Website:      http://mindcuber.com
#
# Version:      v1p5
#
# Modified:     $Date: 2020-12-25 14:37:55 +0000 (Fri, 25 Dec 2020) $
#
# Revision:     $Revision: 7803 $
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
# Purpose:    PrimeCuber robot Rubik's Cube solver
#-----------------------------------------------------------------------------
# Note:
#   The programs, PCSolver-v1p5 and PCInstall-v1p5 must be run once in that
#   order to install the modules and data file used by this program. This
#   basic solver will allow the cube to be solved in around 3.5 minutes.
#
#   Optionally, the programs, PCMTab4-v1p5 and PCInstall-v1p5, may be run
#   once to install a large data file that enables shorter solutions to be
#   calculated. In this case, the cube will be solved in around 2 minutes.
#-----------------------------------------------------------------------------

import hub, os
hub.display.show(hub.Image.DIAMOND)

def file_ok(fname, sz):
    try:
        ok = os.stat(fname)[6] >= sz
    except:
        ok = False
    return ok

if not (file_ok("/pccolors_v1p5.py", 7000) and
        file_ok("/pcsolver_v1p5.py", 22000) and
        file_ok("/primecuber_v1p5.py", 13000) and
        (file_ok("/pcmtab1_v1p5.bin", 18985) or
        file_ok("/pcmtab4_v1p5.bin", 2561877)
        )
    ):
    from spike import LightMatrix
    msg = "ERROR: check that PCSolver-v1p5 has been installed"
    print(msg)
    LightMatrix().write(msg)

import pcsolver_v1p5
import pccolors_v1p5
import primecuber_v1p5

pcsolver_v1p5.init(pccolors_v1p5)
primecuber_v1p5.main()

raise SystemExit

# END

