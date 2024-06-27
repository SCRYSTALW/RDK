
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
from psychopy import visual, data, core, event
import matplotlib as mpl
import numpy as np
from scipy.stats import weibull_min
import random
import matplotlib.pyplot as plt
import pandas as pd
mpl.use('TkAgg')

ISI= random.gauss(0.1,0.1)
print(ISI)

soundfile=['correct.wav','incorrect.wav']


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'RDK right '  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sc/Desktop/Psychopy/Psychopy staircase/03 try _lastrun.py',
    savePickle=True, saveWideText=True,
# save a log file for detail verbose info
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1470, 956], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Press "p" if dots moving to the right\nPress "q" if dots moving to the left\n\nKeep fixation on the "X" at the middle\n\n\n\nPlace space bar to start \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, 0.0039], colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);
wel = keyboard.Keyboard()


# Initialize components for Routine "block"
blockClock = core.Clock()
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='x',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.0196, 0.0196, 0.0039], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
blank500 = visual.TextStim(win=win, name='blank500',
    text='\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
dots = visual.DotStim(
    win=win, name='dots',units='deg', 
    nDots=250, dotSize=10.0,
    speed=0.2, dir=1.0, coherence=1.0,
    fieldPos=(9, 0.0), fieldSize=4.0, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='direction',dotLife=1.5,
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0,
    depth=0.0)
key_resp = keyboard.Keyboard()
fixation = visual.TextStim(win=win, name='fixation',
    text='x',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.0196, 0.0196, 0.0039], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
TrialCount = 0 # This will keep count of how many trials there are

dir = np.random.choice([0, 180])

# Initialize components for Routine "feedback_2"
feedback_2Clock = core.Clock()
incorrect_count = 0
sound_1 = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# Initialize components for Routine "block"
blockClock = core.Clock()
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='x',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.0196, 0.0196, 0.0039], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
blank500 = visual.TextStim(win=win, name='blank500',
    text='\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
wel.keys = []
wel.rt = []
_wel_allKeys = []
# keep track of which components have finished
welcomeComponents = [text, wel]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *wel* updates
    if wel.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wel.frameNStart = frameN  # exact frame index
        wel.tStart = t  # local t and not account for scr refresh
        wel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wel, 'tStartRefresh')  # time at next scr refresh
        wel.status = STARTED
        # keyboard checking is just starting
        wel.clock.reset()  # now t=0
    if wel.status == STARTED:
        theseKeys = wel.getKeys(keyList=['space'], waitRelease=False)
        _wel_allKeys.extend(theseKeys)
        if len(_wel_allKeys):
            wel.keys = _wel_allKeys[-1].name  # just the last key pressed
            wel.rt = _wel_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Coherence periphery SIMPLE.xlsx')
Coherence_staircase = data.MultiStairHandler(stairType='simple', name='Coherence_staircase',
    nTrials=40.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(Coherence_staircase)  # add the loop to the experiment
# initialise values for first condition
level = Coherence_staircase._nextIntensity  # initialise some vals
condition = Coherence_staircase.currentStaircase.condition

for level, condition in Coherence_staircase:
    currentLoop = Coherence_staircase
    if condition['label'] == 'dir0_high coherence' or condition['label'] == 'dir0_low coherence':
        dir = 0
        corrAns = 'p'
    else:
        dir = 180
        corrAns = 'q'
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    continueRoutine = True


    # ------Prepare to start Routine "block"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blockComponents = [fixation_2, blank500]
    for thisComponent in blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(False)
        
        # *blank500* updates
        if blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank500.frameNStart = frameN  # exact frame index
            blank500.tStart = t  # local t and not account for scr refresh
            blank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank500, 'tStartRefresh')  # time at next scr refresh
            blank500.setAutoDraw(True)
        if blank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank500.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank500.tStop = t  # not accounting for scr refresh
                blank500.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank500, 'tStopRefresh')  # time at next scr refresh
                blank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    dots.setDir(dir)
    dots.setFieldCoherence(level)
    dots.refreshDots()
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    TrialCount += 1
    
    if TrialCount in [20,55]:
        fixation_color = 'red'
    
    else: 
        fixation_color = 'grey'

    #if TrialCount in [10]:
        #pause.draw
        #core.wait(20)
        #win.flip()

    # update/draw the fixation stimulus with the chosen color
    fixation.setColor(fixation_color)
    fixation.draw()
    
    
    # keep track of which components have finished
    trialComponents = [dots, key_resp, fixation]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dots* updates
        if dots.status == NOT_STARTED and tThisFlip >= ISI-frameTolerance:
            # keep track of start time/frame for later
            dots.frameNStart = frameN  # exact frame index
            dots.tStart = t  # local t and not account for scr refresh
            dots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dots, 'tStartRefresh')  # time at next scr refresh
            dots.setAutoDraw(True)
        if dots.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dots.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                dots.tStop = t  # not accounting for scr refresh
                dots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(dots, 'tStopRefresh')  # time at next scr refresh
                dots.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['q','p','space','left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Coherence_staircase.addOtherData('dots.started', dots.tStartRefresh)
    Coherence_staircase.addOtherData('dots.stopped', dots.tStopRefresh)
    thisExp.addData('dotDirection',dir)

    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for Coherence_staircase (MultiStairHandler)
    Coherence_staircase.addResponse(key_resp.corr, level)
    Coherence_staircase.addOtherData('key_resp.rt', key_resp.rt)
    Coherence_staircase.addOtherData('key_resp.started', key_resp.tStartRefresh)
    Coherence_staircase.addOtherData('key_resp.stopped', key_resp.tStopRefresh)
    Coherence_staircase.addOtherData('fixation.started', fixation.tStartRefresh)
    Coherence_staircase.addOtherData('fixation.stopped', fixation.tStopRefresh)
    Coherence_staircase.addOtherData('dir', dir)

    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback_2"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    sound = None
    
    # Check key response and coherence value
    if key_resp.corr:  # correct response
        sound = soundfile[0]
    else:  # incorrect response
        sound = soundfile[0]
    
    sound_1.setSound(sound, secs=0.5, hamming=True)
    sound_1.setVolume(1.0, log=False)
    # keep track of which components have finished
    feedback_2Components = [sound_1]
    for thisComponent in feedback_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedback_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedback_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedback_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback_2"-------
    for thisComponent in feedback_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    Coherence_staircase.addOtherData('sound_1.started', sound_1.tStartRefresh)
    Coherence_staircase.addOtherData('sound_1.stopped', sound_1.tStopRefresh)
    thisExp.nextEntry()
    
# all staircases completed


# ------Prepare to start Routine "block"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
blockComponents = [fixation_2, blank500]
for thisComponent in blockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "block"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_2* updates
    if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.tStart = t  # local t and not account for scr refresh
        fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_2.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            fixation_2.tStop = t  # not accounting for scr refresh
            fixation_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_2, 'tStopRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(False)
    
    # *blank500* updates
    if blank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank500.frameNStart = frameN  # exact frame index
        blank500.tStart = t  # local t and not account for scr refresh
        blank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank500, 'tStartRefresh')  # time at next scr refresh
        blank500.setAutoDraw(True)
    if blank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            blank500.tStop = t  # not accounting for scr refresh
            blank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank500, 'tStopRefresh')  # time at next scr refresh
            blank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block"-------
for thisComponent in blockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
thisExp.addData('blank500.started', blank500.tStartRefresh)
thisExp.addData('blank500.stopped', blank500.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

threshold = Coherence_staircase.method()
print("Threshold estimate: ", threshold)


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
