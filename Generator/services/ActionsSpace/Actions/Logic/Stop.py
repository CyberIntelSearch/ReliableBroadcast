#
#   This file represents the STOP() action

##################################################################################################################################
#
#   IMPORTS
#
##################################################################################################################################

#
from services.ActionsSpace.Actions.Logic.Logic import LOGIC
#
import inputs.GenerationInputs as GenerationInputs
import utils.GlobalVariables.TextVariables as Vars

##################################################################################################################################
#
#   CLASS
#
##################################################################################################################################


class STOP(LOGIC):

    ##################################################################################################################################
    #
    #   VARIBLES
    #
    ##################################################################################################################################

    ##################################################################################################################################
    #
    #   CONSTRUCTOR
    #
    ##################################################################################################################################

    # Constructor
    def __init__(self, message):
        super().__init__(Vars.STOP, "STOP", message,
                         GenerationInputs.getLogicReward(Vars.STOP))

    ##################################################################################################################################
    #
    #   GET
    #
    ##################################################################################################################################

    def getExtraConditionLabel(self):
        return ""

    ##################################################################################################################################
    #
    #   LOGIC
    #
    ##################################################################################################################################

    def __eq__(self, action):
        return super().__eq__(action) and (type(action) is STOP)

    # ----------------------------------------------------------------

    def isSTOP(self):
        return True
