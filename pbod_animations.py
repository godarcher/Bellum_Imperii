## Prebattle Orders & Deployment by Caba'drin
## v0.91
## 14 Dec 2011

from module_animations import *

animations=[
 ##Shield Bash by Xeno, animation by Papa Larazou

##
 ]
 
from util_animations import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "animations"
        orig_animations = var_set[var_name_1]
        modmerge_animations(orig_animations)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
		
def modmerge_animations(orig_animations):
    try:
        add_animations(orig_animations, animations) 		
    except:
        import sys
        print "Injecton 1 failed:", sys.exc_info()[1]
        raise