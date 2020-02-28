## Station Analysis Template for Surface Water Records
## Author(s): Patrick Bryan, Hydrologic Technician, OTXWSC
## Author(s): 
## Working Date: 2/12/2019
## Version 1.0.1

import tkinter as tk
from tkinter import simpledialog
parent = tk.Tk()

#Build a table taking user input for station specific variables
def show_entry_fields():
    return print("Define Station ID %s\nDefine Station Name %s\nBegin Period Date: mm/dd/yyyy %s\nEnd Period Date: mm/dd/yyyy %s\nAnalyst Name (ex.'jsmith') %s"% (e1.get(), e2.get(), e3.get(), e4.get(),e5.get()))

master = tk.Tk()
tk.Label(master, text="Station ID:").grid(row=0)
tk.Label(master, text="Station Name:").grid(row=1)
tk.Label(master, text="Begin Period Date: ").grid(row=2)
tk.Label(master, text="End Period Date: ").grid(row=3)
tk.Label(master, text="Analyst: ").grid(row=4)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Enter', command=show_entry_fields).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
master.mainloop()

# Define global variables from table
stid = str(e1)
stname = str(e2)
begin = str(e3)
mdate = str(e4)
analyst = str(e5)

per = (begin + "-" + mdate)

def ghrecord(ghrec): #Ask question: Is this a dry site? Answer yes or no 
    ghqual = simpledialog.askstring('Gage Height Record', 'What rating do you give the GH time series data? (poor/fair/excellent??) ', parent=parent)
    ghqualifier = simpledialog.askstring('Gage Height Record', 'Explain why you rate it this way. (ex. "due to minor painting during period")')
    cmpl = simpledialog.askstring('Gage Height Record', 'Is the GH time-series data complete or missing data? (Answer "complete", or "missing data due to...") ', parent=parent)
    nl = simpledialog.askstring('Gage Height Record', 'Any data gaps?, (one, few, or many...answer no for none.) ', parent=parent)
    nld = simpledialog.askstring('Gage Height Record', 'If there are data gaps, answer why (due to battery failure, due to bad transmissions, etc... if not then leave blank) ', parent=parent)
    ldate = simpledialog.askstring('Gage Height Record', 'Input date of last levels run, (mm/dd/yyyy) ', parent=parent)
    lfreq = simpledialog.askstring('Gage Height Record', 'Input levels frequency in years, (number only). ', parent=parent)
    reset = simpledialog.askstring('Gage Height Record', 'Was the dial reset during last levels run? (Answer "reset" or "not reset"). ', parent=parent)
    ddat = simpledialog.askstring('Gage Height Record', 'What did the dial read during most recent field visit? (Numbers only) ', parent=parent)
    lval = simpledialog.askstring('Gage Height Record', 'What is the checkbar by levels? (Numbers only) ', parent=parent)
    edits = simpledialog.askstring('Gage Height Record', 'Were there any edits to the data? (If not answer "None"). ', parent=parent)
    pzf = simpledialog.askstring('Discharge Record', 'What was the pzf during the visit? (Numbers only, if no PZF was taken leave blank) ', parent=parent)
    if ghrec == ('yes') or ('Yes'): #If site is dry then ask these questions and log returns as local variables
        maxdry = simpledialog.askstring('Gage Height Record', 'What was the maximum gage height during period? (numbers only) ', parent=parent)
        maxdrydate = simpledialog.askstring('Gage Height Record', 'What date did the max GH occur? (mm/dd/yyyy) ', parent=parent)
        return print("\nGage Height Record: Gage height record is rated "+(ghqual)+(" "+ghqualifier)+". Stage was dry for duration of period with a max gage height of "+(maxdry)+" on "+(maxdrydate)+". Gage height record is "+(cmpl)+" with "+(nl)+" data gaps"+(nld)+".")
        return print("\n\tDatum: Full station levels were run "+(ldate)+". Levels frequency is "+(lfreq)+". WWT was "+(reset)+" during levels run.\n\tElevation of check bar by dial during visit on "+(ldate)+": "+(ddat)+" ft.\n\tElevation by levels: "+(lval)+" ft. on "+(ldate)+".")
        return print("\n\tBackup Data:  All data is backed up to shared network data folder.")
        return print("\n\tIce Affected: N/A")
        return print("\n\tEdits: "+(edits)+".")
        return print("\n\tGage Height Corrections: Site was dry for most recent field visit, with no rises between; no GH corrections needed.")
        return print("\n\tPeak Stage: The maximum computed gage-height for the period was "+(maxdry)+" ft. on "+(maxdrydate)+". No high-water marks were noted during the period.")
        return print("\n\tPZF: N/A")
    elif ghrec == ('no') or ('No'): #If site is not dry then ask these questions and log returns as local variables
        mingh = simpledialog.askstring('Gage Height Record', 'What was the minimum GH during period? (Numbers only) ', parent=parent)
        minghd = simpledialog.askstring('Gage Height Record', 'What was date of the minimum GH during period? (mm/dd/yyyy) ', parent=parent)
        maxgh = simpledialog.askstring('Gage Height Record', 'What was the maximum GH during period? (Number only) ', parent=parent)
        maxghd = simpledialog.askstring('Gage Height Record', 'What was date of the maximum GH during period? (mm/dd/yyyy) ', parent=parent)
        inout = simpledialog.askstring('Gage Height Record', 'Did DCP GH report within or outside error threshold on field visit date? (Answer "in" or "out"). ', parent=parent)
        ghcor = simpledialog.askstring('Gage Height Record', 'Was the DCP reset? By how much? (Ex. DCP read -0.05 ft. from WWT and was reset by +0.05 ft. to match WWT, if not then answer "no corrections needed")')
        return print("\nGage Height Record: Gage height record is rated "+(ghqual)+(ghqualifier)+". Range of computed stage was "+(mingh)+" ft. on "+(minghd)+" to "+(maxgh)+" ft. on "+(maxghd)+". Gage height record is "+(cmpl)+" with "+(nl)+" data gaps.")
        return print("\n\tDatum: Full station levels were run "+(ldate)+". Levels frequency is "+(lfreq)+". WWT was "+(reset)+" during levels run.\n\tElevation of check bar by dial during visit on "+(ldate)+": "+(ddat)+" ft.\n\tElevation by levels: "+(lval)+" ft. on "+(ldate)+".")
        return print("\n\tBackup Data:  All data is backed up to shared network data folder.")
        return print("\n\tIce Affected: N/A")
        return print("\n\tEdits: "+(edits)+".")
        return print("\n\tGage Height Corrections: DCP read "+(inout)+" +/-0.02 ft. threshold of WWT on the field visit on "+(mdate)+", "+(ghcor)+".")
        return print("\n\tPeak Stage: The maximum computed gage-height for the period was "+(maxgh)+" ft. on "+(maxghd)+". No high-water marks were noted during the period.")
        return print("\n\tPZF – GZF computed to be "+(pzf)+" ft for visit on "+(mdate)+".")
    else:
        return print('')

def sitetype(nump): ## Ask question: Is this site a stage only (1) or stage/discharge (2)? (Answer 1 or 2)
    if nump == ('2'): #If this site requires Q Mmts, ask these questions and log local variables
        rating = simpledialog.askstring('Rating', 'What is the current rating number? ', parent=parent)
        inputlo = simpledialog.askstring('Rating', 'What is the low hinge point of the current rating? (Numbers only) ', parent=parent)
        inputmid = simpledialog.askstring('Rating', 'What is the mid hinge point of the current rating? (Numbers only) ', parent=parent)
        inputhi = simpledialog.askstring('Rating', 'What is the high hinge point of the current rating? (Numbers only) ', parent=parent)
        mdate = simpledialog.askstring('Discharge Record', 'What was the date of the most recent measurement? (mm/dd/yyyy) ', parent=parent)
        mmtno = simpledialog.askstring('Discharge Record', 'What is the measurement number? (Number only) ', parent=parent)
        mqual = simpledialog.askstring('Discharge Record', 'What was the measurement quality: poor, fair, good, or excellent? ', parent=parent)
        m1d = simpledialog.askstring('Discharge Record', 'What was the previously measured discharge? (numbers only) ', parent=parent)
        m2d = simpledialog.askstring('Discharge Record', 'What was the most recent measured discharge? (Numbers only) ', parent=parent)
        qdifpct = simpledialog.askstring('Discharge Record', 'What was the percent difference between measured and currently shifted Q? (Numbers only) ', parent=parent)
        scourfill = simpledialog.askstring('Discharge Record', 'Was there a scour or fill observed between visits? (Answer "(slight/significant) scour" or "fill") ', parent=parent)
        hydrocomp = simpledialog.askstring('Discharge Record', 'What is the site number for hydrographic comparisons? ', parent=parent)
        hydrocompqual = simpledialog.askstring('Discharge Record', 'How does the site compare by hydrograph? Answer: compares reasonably well, or does not compare well due to... ', parent=parent)
        maxq = simpledialog.askstring('Discharge Record', 'What was the maximum computed discharge for period? Number only ', parent=parent)
        maxqdate = simpledialog.askstring('Discharge Record', 'On what date did this occur? mm/dd/yyyy ', parent=parent)
        minq = simpledialog.askstring('Discharge Record', 'What was the minimum computed discharge for period? Number only ', parent=parent)
        minqdate = simpledialog.askstring('Discharge Record', 'On what date did this occur? mm/dd/yyyy ', parent=parent)
        conclear = simpledialog.askstring('Discharge Record', 'Was the control clear or not clear? (Answer "clear" or "not clear") ', parent=parent)
        concond = simpledialog.askstring('Discharge Record', 'Was the stream under section or channel control? Describe the conditions at the control during measurement. (ex. "Stream was under section control with scattered tree debris along banks.") ', parent=parent)
        estimates = simpledialog.askstring('Discharge Record', 'Estimates? (if yes, please describe; or answer None) ', parent=parent)
        def shiftyesno(answer): ## Did the site require shifts?
            if answer == ('no' or 'No'):    # If no shifts required, explain why
                whynoshifts = simpledialog.askstring('Rating', 'Why were no shifts required?', parent=parent)
                return print("Application of shift curves: No shifts were needed based on " + (mmtno)+". "+(whynoshifts))
            elif answer == ('yes' or 'Yes'):
                eventend = simpledialog.askstring('Rating', 'Did the previous shift end at the peak or recession of largest event? Answer peak or recession ', parent=parent)
                eventbegin = simpledialog.askstring('Rating', 'Did the new shift begin at peak or on recession? Answer at peak or on recession ', parent=parent)
                shiftdate = simpledialog.askstring('Rating', 'What date was the shift applied? Number only ', parent=parent)
                return print("Application of shift curves: Ended previous shift at "+(eventend)+" on "+(shiftdate)+". Began new "+(scourfill)+" shift "+(eventbegin)+" of event and continued through MMT "+(mmtno)+" on "+(mdate)+" which rated "+(mqual)+".")
            else:
                return print("N/A")
        return print("\nStage-Discharge Relation: Rating No. "+(rating)+" was continued into use during the entire period. Measurements confirmed the rating at the low end of the rating during the current period. Measurement number "+(mmtno)+" indicated a slight scour shift on lower end.")
        return print("\n\tDischarge Measurements and Control Conditions: Both measurements agreed within "+(qdifpct)+" of each other and indicated a "+(scourfill)+" effect in channel.\n\n\tThe control conditions were observed to be "+(conclear)+". "+(concond)+".\n\n\tMeasured discharges for the period ranged from "+(m1d)+" to "+(m2d)+" cfs.")
        return print("\n\tShift Curves: The stage shifts use a low-end (section) shift point of "+(inputlo)+" ft., which is the low-point of Rating No. "+(rating)+" before extending up to a stage of "+(inputmid)+" ft. which is the stage at which the section control begins to become inundated during normal conditions. From this knee point, the shift curves are brought back to the rating at a stage of "+(inputhi)+" ft., where channel control conditions are expected to be fully in control.")
        return print(shiftyesno(simpledialog.askstring('Dialog Title', 'Were shifts required? If no measurement answer "N/A"', parent=parent)))
        return print("\nComputed Discharge: Record for period rated fair. Discharge record was computed using gage-height record from a pressure transducer, gage-height corrections, and Rating No. "+(rating)+" with variable shift applications. Discharge record for the period was complete with the following exceptions:")
        return print("\n\tEstimates: "+(estimates)+" for period.")
        return print("\nHydrographic Comparison: Hydrographic comparison can be made with station "+(hydrocomp)+" to verify the timing and magnitude of rises throughout the period. Hydrographic comparison "+(hydrocompqual))
        return print("\n\tPeak Streamflow: Maximum computed discharge for the period was "+(maxq)+" cfs at a on "+(maxqdate)+". The minimum computed discharge for the period was "+(minq)+" cfs on "+(minqdate)+".")
    else:
        return print("\n")

## Form paragraphs from variable inputs

h1 =  stid
h2 =  per
h3 =  analyst
h4 =  ghrecord(simpledialog.askstring('GH record', 'Is this a dry site/did the stage have any rises during period? Answer yes or no', parent=parent))
h5 =  sitetype(simpledialog.askstring('Stage/Discharge Relation', 'Is this site a stage only (1) or stage/discharge (2)? (Answer 1 or 2)', parent=parent))
h6 = "\nComments: "+simpledialog.askstring('Final Thoughts', 'Any comments to add? (CSG needed?, New rating needed?, etc... If not answer "None")', parent=parent)+"."


stationanaly = (h1+h2+h3+h4+h5+h6)      ## Add paragraphs together to form Station Analysis
f = open("station_analysis.txt","w+")   ## Create and open new textfile named 'Station Analysis'
f.write(stationanaly)                   ## Log Station Analysis text to textfile
f.close()                               ## Close textfile