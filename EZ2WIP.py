caca = 1
class Narrative:
    
    def __init__(self):
        pass
    
    def __repr__(self):
        pass
    
    def refusal(age, sex, loc, pos, life, hpi, name):
      return(f"""
    ***************************************************************************************************************************************************

    Crew arrives to scene and finds a {str(age)} YO {sex} {loc} {pos}. {life}

    HPI: {hpi}

    At this time patient believes their condition does not require additional evaluation or treatment at hospital and wishes to refuse transport.
    Risks and consequences of this action explained to patient including unseen illness, injury and/or death. Patient acknowledges understanding these and wishes to sign EMS refusal.
    Refusal form read and explained to patient, whom acknowledged understanding the form and its content and signs without coercion. Patient appears to be competent to make this informed decision.
    They do not appear to be under the influence of mind or mood altering substances, nor do they appear to be a threat to themselves or others.
    
    **** ALL TIMES ARE ESTIMATED ****
    
    {name}

    ***************************************************************************************************************************************************""")
    
    def C911(age, sex, loc, pos, life, hpi, downgrade, srs, tmethod, tmethod2, room, name):
      return(f"""
    ***************************************************************************************************************************************************

    Crew arrives to scene and finds a {age} YO {sex} {loc} {pos}. {life}
    
    {hpi}
    {downgrade}
    {srs}    
    {tmethod}
    
    During transport pt is monitored for changes in vitals or alertness, or any new complaints. Pt rests during transport. Pt remains stable during transport.

    Upon arrival at the hospital the patient is unloaded from the ambulance and taken inside the emergency department and into room #{room}
    {tmethod2}
    Patient care is transferred to the receiving staff after they obtained a comprehensive report from the EMS crew.

    **** ALL TIMES ARE ESTIMATED ****

    {name}

    ***************************************************************************************************************************************************""")
    
    def triage(age, sex, loc, pos, life, hpi, downgrade, srs, tmethod, name):
      return(f"""
    ***************************************************************************************************************************************************

    Crew arrives to scene and finds a {str(age)} YO {sex} {loc} {pos}. {life}
    
    {hpi}
    {downgrade}
    {srs}
    {tmethod}
    
    During transport pt is monitored for changes in vitals or alertness, or any new complaints. Pt rests during transport. Pt remains stable during transport.

    Upon arrival at the hospital the patient is unloaded from the ambulance and taken inside the emergency department and into the triage area.
    The stretcher is lowered to a safe level and the safety straps undone. Pt is able to stand and pivot from EMS stretcher to wheelchair with assistance from crew. Pt is subsequently registered and situated in waiting room.
    Patient care is transferred to the receiving staff after they obtained a comprehensive report from the EMS crew.

    **** ALL TIMES ARE ESTIMATED ****

    {name}

    ***************************************************************************************************************************************************""")
    
    def NARRATIVET(unit, dispatcher, origin, destination, age, sex, pos, hpi, tmethod1, where, tmethod2, name):
      return(f"""
    ***************************************************************************************************************************************************

    Ambulance {str(unit)} dispatched by {str(dispatcher)} for a BLS transport to take the patient from {origin} to {destination}.

    ATF: {str(age)} Year Old {sex} {pos}; presents with a self-maintained, patent airway and is breathing at a normal rate and rhythm, with equal, bilateral chest rise. Pt appears to be perfusing adequately.
    
    HPI: {hpi}.
    
    BLS assessment:  See assessment TAB
    
    Transfer:  Pt is transferred to our stretcher via {tmethod1}.  Pt is assisted to a position of comfort and secured in with all safety straps. The side rails are placed up and locked. Pt is taken to the ambulance and loaded in while still on stretcher, stretcher secured via locking floor mount
    
    Transport: During transport pt is monitored for changes in vitals or alertness, or any new complaints. Pt rests during transport. Transport occurs without incident.
    
    Destination: When the crew arrives at the destination, pt is removed from the ambulance while still on stretcher and taken into {where}. Pt {tmethod2} onto bed. Upon transfer of care, patient offers no new complaints and no further changes noted in patient's condition beyond what has been documented elsewhere.
    
    
    **** All times in this PCR are estimated ****
    
    {name}
    
    ***************************************************************************************************************************************************""")
    
class Narrative_Build:
    srs_list = {1:"Pt is able to stand and pivot onto stair chair with assistance from crew.", 2:"The reeves is placed adjecent to pt and was rolled into the device. Straps are applied and pt is lifted by crew. Pt is taken outside where the stretcher is waiting. Litter sraps are applied and pt is taken to the ambulance and loaded in, stretcher secured via locking floor mount.", 3:"The sides of the scoop stretcher are alligned with pt and then connected. Pt is lifted from found position and onto litter. Litter straps are applied and pt was taken outside and loaded into ambulance.", 4: ""}
    #srs_list [1] Stair Chair, [2] Reeves, [3] Scoop
    tmethod_list = {1: "Pt is able to ambulate from found position and to the stretcher with assistance from crew. Pt is assisted to a position of comfort and secured in with all appropriate safety straps.  The side rails are placed up and locked. Pt is taken to the ambulance and loaded in, stretcher secured via locking floor mount.", 2 :"Pt is able to ambulate from found position and into the ambulance where the stretcher is waiting with assistance from crew. Pt is assisted to a position of comfort, secured via all appropriate safety straps, and the side rails are placed up and locked.  The stretcher remains secured via locking floor mounts.", 3: "Pt is transferred to our stretcher via sheet lift. Pt is assisted to a position of comfort and secured in with all safety straps.  The side rails are placed up and locked.  Pt is taken to the ambulance and loaded in while still on stretcher, stretcher secured via locking floor mount.", 4: "Patient is able to stand and pivot from found position onto the stretcher with assistance from crew. Patient is assisted to a position of comfort and secured in with all appropriate safety straps.  The side rails are placed up and locked. Pt is taken to the ambulance and loaded in, stretcher secured via locking floor mount."}
    #tmethod_list [1] Assisted to stretcher, [2] Assisted to ambulance, [3] Sheet lift, [4] Stand and Pivot
    tmethod2_list = {1: "EMS stretcher is aligned with hospital bed and safety straps removed. Pt is transferred from EMS stretcher to hospital bed via sheet lift.", 2: "EMS stretcher is aligned with  bed and safety straps removed. Pt is able to transfer themselves with assistance from staff/crew.", 3: "The stretcher is lowered to a safe level and the safety straps undone. Pt is able to independently ambulate from EMS stretcher to LGH bed."}
    #tmethod2_list [1] Sheet Lift, [2] Assisted, [3] Ambulated
    lifer = "Pt presents with a self-maintained, patent airway and is breathing with no signs of distress or difficulty. No immediate life threats are noted."
    
    def __init__(self):
        pass
    
    def __repr__(self):
        pass
    
    def vari_call(self):
        refusal = input("Refusal? ")
        age = input("Patient Age:  ")
        sex = input("Patient Sex: ")
        loc = input("Patient LOC: ")
        if loc in [" ", ""]: loc = "CAOx4"
        pos = input("Found Position: ")
        life = input('Immediate Life Threats? ')
        if life in [" ", "", 'n', '2']: life = self.lifer
        hpi = input('HPI: ')
        if refusal in ['n', 'N', 'No', 'no', 'NO', '']:
          downgrade = input('[blank = NO] Downgrade?: ')
          if downgrade in ['y', 'Y', 'Yes', 'YES', 'yes']: downgrade = 'At this time the patient does not require continuous ALS monitoring or intervention in accordance with PA BEMS Protocol. The patient can be safely downgraded to BLS level of care for continued treatment and transport.'
          numi = input('STAIR CHAIR [1], REEVES [2], SCOOP [3], NONE [4]: ')
          srs = self.srs_list[int(numi)]
          tnumi = input('[1] Assisted to stretcher, [2] Assisted to ambulance, [3] Sheet lift, [4] Stand and Pivot: ')
          tmethod = self.tmethod_list[int(tnumi)]
          triage = input('E.R. [1], Triage [2]')
          if int(triage) == 1:
              tnumi2 = input('TRANSFER: [1] Sheet Lift, [2] Assisted, [3] Ambulated: ')
              tmethod2 = self.tmethod2_list[int(tnumi2)]
              room = input('ROOM NUMBER: ')
              name = input('NAME AND CERT NUMBER: ')
              varilist = [age, sex, loc, pos, life, hpi, downgrade, srs, tmethod, tmethod2, room, name]
              return varilist
            
          elif int(triage) == 2:
              name = input('NAME AND CERT NUMBER: ')
              varilist = [age, sex, loc, pos, life, hpi, downgrade, srs, tmethod, name]
              return varilist
            
        else:
            name = input('NAME AND CERT NUMBER: ')
            varilist = [age, sex, loc, pos, life, hpi, name]
            return varilist
  
    def vari_tra(self):
        unit = input("UNIT: ")
        dispatcher = input("DISPATCHED BY COMM CENTER OR MEDIC 600? ")
        origin = input("FROM: ")
        destination = input("DESTINATION: ")
        age = input("PATIENT AGE: ")
        sex = input("PATIENT GENDER: ")
        pos = input("POSITION IN BED: ")
        hpi = input("HPI: ")
        tmethod1 = input("TRANSFER METHOD: ")
        where = input("PATIENT TAKEN TO: ")
        tmethod2 = input("TRANSFER METHOD: ")
        name = input("NAME AND CERT NUMBER:")
        varilist = [unit, dispatcher, origin, destination, age, sex, pos, hpi, tmethod1, where, tmethod2, name]
        return varilist

