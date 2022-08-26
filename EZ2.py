from EZ2WIP import Narrative, Narrative_Build

# TITLE SCREEN
print("""

oooooooooooo  oooooooooooo   .oooooo.   ooooo   ooooo       .o.       ooooooooo.   ooooooooooooo
`888'     `8 d'      d888'  d8P'  `Y8b  `888'   `888'      .888.      `888   `Y88. 8'   888   `8
 888               .888P   888           888     888      .8"888.      888   .d88'      888
 888oooo8         d888'    888           888ooooo888     .8' `888.     888ooo88P'       888
 888    "       .888P      888           888     888    .88ooo8888.    888`88b.         888
 888       o   d888'    .P `88b    ooo   888     888   .8'     `888.   888  `88b.       888
o888ooooood8 .8888888888P   `Y8bood8P'  o888o   o888o o88o     o8888o o888o  o888o     o888o         Version 0.2

***************************************************************************************************************************************************

Disclaimer: This program is designed to be a learning tool, it is NOT to be used for charting.
            By using this application you assume all responsibility for your actions.

***************************************************************************************************************************************************



""")

TYPE = input('TYPE "1" FOR 911 AND "2" FOR TRANSPORT CHART: ')
if TYPE == '1':
    variables = Narrative_Build()
    varilist = variables.vari_call()
    if len(varilist) == 7:
        print(Narrative.refusal(varilist[0], varilist[1], varilist[2], varilist[3], varilist[4], varilist[5], varilist[6]))
    elif len(varilist) == 10:
        print(Narrative.triage(varilist[0], varilist[1], varilist[2], varilist[3], varilist[4], varilist[5], varilist[6], varilist[7], varilist[8], varilist[9]))
    elif len(varilist) == 12:
        print(Narrative.C911(varilist[0], varilist[1], varilist[2], varilist[3], varilist[4], varilist[5], varilist[6], varilist[7], varilist[8], varilist[9], varilist[10], varilist[11]))
        
elif TYPE == "2":
    variables = Narrative_Build()
    varilist = variables.vari_tra()
    print(Narrative.NARRATIVET(varilist[0], varilist[1], varilist[2], varilist[3], varilist[4], varilist[5], varilist[6], varilist[7], varilist[8], varilist[9], varilist[10], varilist[11]))