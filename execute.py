from pathlib import Path
import mainCJF
import utils as tool
import sys
import traceback
from InternalControl import cInternalControl

objControl=cInternalControl()
log_Dir=objControl.log_Dir


tool.writeLogAndConsole(log_Dir,'log_excelcjf.txt','Starting CJF excel service')
try:
    mainCJF.maincjf()
except:
    tool.writeLogAndConsole(log_Dir,'log_excelcjf.txt',str(traceback.print_exc()))          


