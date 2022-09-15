import PySimpleGUI as sg
from EasyChart import Narrative
sg.theme('DarkTeal9')

# Main screen layout
layout1 = [
    [sg.Text('Type of chart: ', size=(15, 1))],
    [sg.Button("Transport"), sg.Button("Refusal"), sg.Button("911 Triage"), sg.Button("911")]
]

# Transport window layout
layoutTransport = [
    [sg.Text('Unit: ', size=(15,1)), sg.Push(), sg.InputText(key='unit')],
    [sg.Text('Dispatcher: ', size=(15,1)), sg.Push(), sg.InputText(key='dispatcher')],
    [sg.Text('From: ', size=(15,1)), sg.Push(), sg.InputText(key='origin')],
    [sg.Text('To: ', size=(15,1)), sg.Push(), sg.InputText(key='destination')],
    [sg.Text('Age: ', size=(15,1)), sg.Push(), sg.InputText(key='age')],
    [sg.Text('Sex: ', size=(15,1)), sg.Push(), sg.InputText(key='sex')],
    [sg.Text('Found position: ', size=(15,1)), sg.Push(), sg.InputText(key='pos')],
    [sg.Text('HPI: ', size=(15,1)), sg.Push(), sg.InputText(key='hpi')],
    [sg.Text('Transfer method: ', size=(15,1)), sg.Push(), sg.InputText(key='tmethod1')],
    [sg.Text('Taken to: ', size=(15, 1)), sg.Push(), sg.InputText(key='where')],
    [sg.Text('Transfer method: ', size=(15, 1)), sg.Push(), sg.InputText(key='tmethod2')],
    [sg.Text('Name and Cert #: ', size=(15, 1)), sg.Push(), sg.InputText(key='name')],
    [sg.Multiline('', size=(75, 30), key='OUTPUT')],
    [sg.Button('Generate Narrative', key="TransportT")]
]

# 911 window layout
layout911 = [
    [sg.Text('Age: ', size=(15,1)), sg.Push(), sg.InputText(key='age911')],
    [sg.Text('Sex: ', size=(15,1)), sg.Push(), sg.InputText(key='sex911')],
    [sg.Text('L.O.C.: ', size=(15,1)), sg.Push(), sg.InputText(key='loc911')],
    [sg.Text('Found Position: ', size=(15,1)), sg.Push(), sg.InputText(key='pos911')],
    [sg.Text('Immediate life threats: ', size=(25,1)), sg.Push(), sg.InputText(key='life911')],
    [sg.Text('HPI: ', size=(15, 1)), sg.Push(), sg.InputText(key='hpi911')],
    [sg.Text('Downgrade? ', size=(15, 1)), sg.Push(), sg.InputText(key='downgrade911')],
    [sg.Text('STAIR CHAIR [1], REEVES [2], SCOOP [3], NONE [4]: ', size=(50, 1)), sg.Push(), sg.InputText(key='srs911')],
    [sg.Text('TRANSFER TO STRETCHER: [1] Sheet Lift, [2] Assisted, [3] Ambulated: ', size=(65, 1)), sg.Push(), sg.InputText(key='tmethod911')],
    [sg.Text('Room: ', size=(15,1)), sg.Push(), sg.InputText(key='room911')],
    [sg.Text('TRANSFER TO BED: [1] Sheet Lift, [2] Assisted, [3] Ambulated: ', size=(55, 1)), sg.Push(), sg.InputText(key='tmethod2911')],
    [sg.Text('Name and Cert #: ', size=(15, 1)), sg.Push(), sg.InputText(key='name911')],
    [sg.Multiline('', size=(75, 30), key='OUTPUT911')],
    [sg.Button("Generate 911 Narrative", key="911GEN")]
]

# Triage window layout
layoutTriage = [
    [sg.Text('Age: ', size=(15,1)), sg.Push(), sg.InputText(key='ageT')],
    [sg.Text('Sex: ', size=(15,1)), sg.Push(), sg.InputText(key='sexT')],
    [sg.Text('L.O.C.: ', size=(15,1)), sg.Push(), sg.InputText(key='locT')],
    [sg.Text('Found Position: ', size=(15,1)), sg.Push(), sg.InputText(key='posT')],
    [sg.Text('Immediate life threats: ', size=(25,1)), sg.Push(), sg.InputText(key='lifeT')],
    [sg.Text('HPI: ', size=(15, 1)), sg.Push(), sg.InputText(key='hpiT')],
    [sg.Text('Downgrade? ', size=(15, 1)), sg.Push(), sg.InputText(key='downgradeT')],
    [sg.Text('STAIR CHAIR [1], REEVES [2], SCOOP [3], NONE [4]: ', size=(50, 1)), sg.Push(), sg.InputText(key='srsT')],
    [sg.Text('TRANSFER: [1] Sheet Lift, [2] Assisted, [3] Ambulated: ', size=(50, 1)), sg.Push(),
     sg.InputText(key='tmethodT')],
    [sg.Text('Name and Cert #: ', size=(15, 1)), sg.Push(), sg.InputText(key='nameT')],
    [sg.Multiline('', size=(75, 30), key='OUTPUTT')],
    [sg.Button("Generate Triage Narrative", key="Tr")]
]

# Refusal window layout
layoutRefusal = [
    [sg.Text('Age: ', size=(15,1)), sg.Push(), sg.InputText(key='ageR')],
    [sg.Text('Sex: ', size=(15,1)), sg.Push(), sg.InputText(key='sexR')],
    [sg.Text('L.O.C.: ', size=(15,1)), sg.Push(), sg.InputText(key='locR')],
    [sg.Text('Found Position: ', size=(15,1)), sg.Push(), sg.InputText(key='posR')],
    [sg.Text('Immediate life threats: ', size=(29,1)), sg.Push(), sg.InputText(key='lifeR')],
    [sg.Text('HPI: ', size=(15, 1)), sg.Push(), sg.InputText(key='hpiR')],
    [sg.Text('Name and Cert #: ', size=(15, 1)), sg.Push(), sg.InputText(key='nameR')],
    [sg.Multiline('', size=(75, 30), key='OUTPUTR')],
    [sg.Button("Generate Refusal Narrative", key="R")]
]

# Layout settings
layout = [
          [sg.Column(layout1, key='-COL0-'), sg.Column(layoutTransport, visible=False, key='-COL1-'),
           sg.Column(layoutRefusal, visible=False, key='-COL2-'), sg.Column(layoutTriage, visible=False, key='-COL3-'),
           sg.Column(layout911, visible=False, key='-COL4-')],
          [sg.Exit()]
]

window = sg.Window('Easy Chart', layout, finalize=True)
window.bind('<Right>', '-NEXT-')
window.bind('<Left>', '-PREV-')
layout = 0

# Main UI loop
while True:
    event, values = window.read()
    newClass = Narrative()
    if event == '-NEXT-':
        next_element = window.find_element_with_focus().get_next_focus()
        next_element.set_focus()
    if event == '-PREV-':
        prev_element = window.find_element_with_focus().get_previous_focus()
        prev_element.set_focus()
    if event in (None, 'Exit'):
        break
    if event == 'Transport':
        print(values['unit'])
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
        event, values = window.read()
    if event == 'TransportT':
        narrative = newClass.narrativet(values["unit"], values["dispatcher"], values["origin"],
                                       values["destination"],
                                       values["age"], values["sex"], values["pos"], values["hpi"],
                                       values["tmethod1"], values["where"], values["tmethod2"], values["name"])
        window['OUTPUT'].update(value=narrative)
    if event == "Refusal":
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)
    if event == "R":
        narrativeR = newClass.refusal(values["ageR"], values["sexR"], values["locR"], values["posR"],
                                       values["lifeR"], values["hpiR"], values["nameR"])
        window['OUTPUTR'].update(value=narrativeR)
    if event == '911 Triage':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'Tr':
        narrativeT = newClass.triage(values["ageT"], values["sexT"], values["locT"], values["posT"],
                                      values["lifeT"], values["hpiT"], values["downgradeT"], values["srsT"],
                                      values["tmethodT"],values["nameT"])
        window['OUTPUTT'].update(value=narrativeT)
    if event == "911":
        window[f'-COL{layout}-'].update(visible=False)
        layout = 4
        window[f'-COL{layout}-'].update(visible=True)
    if event == '911GEN':
        narrative911 = newClass.c911(values["age911"], values["sex911"], values["loc911"], values["pos911"],
                                       values["life911"], values["hpi911"], values["downgrade911"], values["srs911"],
                                       values["tmethod911"], values["tmethod2911"], values["room911"],
                                       values["name911"])
        window['OUTPUT911'].update(value=narrative911)
window.close()