class Narrative:
    srs_list = {1: "Pt is able to stand and pivot onto stair chair with assistance from crew.",
                2: """The reeves is placed adjecent to pt and was rolled into the device. Straps are applied and pt is \
                lifted by crew. Pt is taken outside where the stretcher is waiting. Litter sraps are applied and pt is \
                taken to the ambulance and loaded in, stretcher secured via locking floor mount.""",
                3: """The sides of the scoop stretcher are alligned with pt and then connected. Pt is lifted from \
                found position and onto litter. Litter straps are applied and pt was taken outside and loaded into the \
                ambulance.""",
                4: ""}
    tmethod_list = {
        1: "Pt is able to ambulate from found position and to the stretcher with assistance from crew. Pt is assisted \
        to a position of comfort and secured in with all appropriate safety straps.  The side rails are placed up and \
        locked. Pt is taken to the ambulance and loaded in, stretcher secured via locking floor mount.",
        2: "Pt is able to ambulate from found position and into the ambulance where the stretcher is waiting with \
        assistance from crew. Pt is assisted to a position of comfort, secured via all appropriate safety straps, and \
        the side rails are placed up and locked.  The stretcher remains secured via locking floor mounts.",
        3: "Pt is transferred to our stretcher via sheet lift. Pt is assisted to a position of comfort and secured in \
        with all safety straps.  The side rails are placed up and locked.  Pt is taken to the ambulance and loaded in \
        while still on stretcher, stretcher secured via locking floor mount.",
        4: "Patient is able to stand and pivot from found position onto the stretcher with assistance from crew. \
        Patient is assisted to a position of comfort and secured in with all appropriate safety straps.  The side \
        rails are placed up and locked. Pt is taken to the ambulance and loaded in, stretcher secured via locking \
        floor mount."}
    tmethod2_list = {
        1: "EMS stretcher is aligned with hospital bed and safety straps removed. Pt is transferred from EMS stretcher \
        to hospital bed via sheet lift.",
        2: "EMS stretcher is aligned with  bed and safety straps removed. Pt is able to transfer themselves with \
        assistance from staff/crew.",
        3: "The stretcher is lowered to a safe level and the safety straps undone. Pt is able to independently \
        ambulate from EMS stretcher to LGH bed."}
    lifer = "Pt presents with a self-maintained, patent airway and is breathing with no signs of distress or \
    difficulty. No immediate life threats are noted."

    def __init__(self):
        pass
    
    def refusal(self, age, sex, loc, pos, life, hpi, name=None):
        if loc in ["", " "]: loc = "CAOx4"
        if life in [" ", "", 'n', '2']:
            life = self.lifer
        return(f"""
    
    ****************************************************************************
    
    Crew arrives to scene and finds a {str(age)} YO {sex} {loc} {pos}. {life}
    
    {hpi}
    At this time patient believes their condition does not require additional evaluation or treatment at hospital and wishes to refuse transport.
    Risks and consequences of this action explained to patient including unseen illness, injury and/or death. Patient acknowledges understanding these and wishes to sign EMS refusal.
    Refusal form read and explained to patient, whom acknowledged understanding the form and its content and signs without coercion. Patient appears to be competent to make this informed decision.
    They do not appear to be under the influence of mind or mood altering substances, nor do they appear to be a threat to themselves or others.
    
    **** ALL TIMES ARE ESTIMATED ****
    
    {name}

    ****************************************************************************""")
    
    def c911(self, age, sex, loc, pos, life, hpi, downgrade, srs=4, tmethod=1, tmethod2=1, room="00", name=None):
        if loc in ["", " "]: loc = "CAOx4"
        if life in [" ", "", 'n', '2']:
            life = self.lifer
        if downgrade in ['y', 'Y', 'Yes', 'YES', 'yes']:
            downgrade = '''At this time the patient does not require continuous ALS monitoring or intervention in \
            accordance with PA BEMS Protocol. The patient can be safely downgraded to BLS level of care for continued \
            treatment and transport.'''
        srs = self.srs_list[int(srs)]
        tmethod = self.tmethod_list[int(tmethod)]
        return(f"""
    
    ****************************************************************************
    
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

    ****************************************************************************""")
    
    def triage(self, age, sex, loc, pos, life, hpi, downgrade, srs=4, tmethod=1, name=None):
        if loc in ["", " "]: loc = "CAOx4"
        if life in [" ", "", 'n', '2']:
            life = self.lifer
        if downgrade in ['y', 'Y', 'Yes', 'YES', 'yes']:
            downgrade = '''At this time the patient does not require continuous ALS monitoring or intervention in \
            accordance with PA BEMS Protocol. The patient can be safely downgraded to BLS level of care for continued \
            treatment and transport.'''
        srs = self.srs_list[int(srs)]
        tmethod = self.tmethod_list[int(tmethod)]
        return (f"""
        ****************************************************************************
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

****************************************************************************""")
    
    def narrativet(self, unit, dispatcher, origin, destination, age, sex, pos, hpi, tmethod1, where, tmethod2, name):
        return(f"""
      
    ****************************************************************************

    Ambulance {str(unit)} dispatched by {str(dispatcher)} for a BLS transport to take the patient from {origin} to {destination}.

    ATF: {str(age)} Year Old {sex} {pos}; presents with a self-maintained, patent airway and is breathing at a normal rate and rhythm, with equal, bilateral chest rise. Pt appears to be perfusing adequately.
    
    HPI: {hpi}.
    
    BLS assessment:  See assessment TAB
    
    Transfer:  Pt is transferred to our stretcher via {tmethod1}.  Pt is assisted to a position of comfort and secured in with all safety straps. The side rails are placed up and locked. Pt is taken to the ambulance and loaded in while still on stretcher, stretcher secured via locking floor mount
    
    Transport: During transport pt is monitored for changes in vitals or alertness, or any new complaints. Pt rests during transport. Transport occurs without incident.
    
    Destination: When the crew arrives at the destination, pt is removed from the ambulance while still on stretcher and taken into {where}. Pt {tmethod2} onto bed. Upon transfer of care, patient offers no new complaints and no further changes noted in patient's condition beyond what has been documented elsewhere.
    
    
    **** All times in this PCR are estimated ****
    
    {name}
    ****************************************************************************""")


