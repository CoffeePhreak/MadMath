>[!IMPORTANT]
>THIS PROGRAM REQUIRES PYTHON 3
>
>The most current version of Python can be
>downloaded [here](https://www.python.org/downloads).

>[!IMPORTANT]
>PYTHON 3 REQUIRES TKINTER
>
>Running 'pip install tk' from a command line
>or terminal AFTER installing Python should do
>the trick if tkinter did not come bundled in
>your version of Python.


>[!CAUTION]
>Mad Math searches the included "data" directory for a file
>named MadMath.db, which is created when the program is
>launched and can't find the file (like the first time it's
>run). Make a shortcut/symlink to MadMath.pyw if you would
>like to launch the program from a different folder than
>where it is saved.
>
>**Do not move anything OUT of the MadMath folder. The folder
>itself can be moved, but not while the program is running.**


# TO USE MAD MATH
Download and unzip MadMath.zip to the desired location
then double click MadMath.pyw in the MadMath directory to launch.


## ABOUT MAD MATH
>When I was in 2<sup>nd</sup> grade, we started every math segment
>by completing a timed one-minute worksheet containing 20
>equations in which we performed addition on two random
>single digit numbers. This was meant to be a warm up
>exercise, and at first most struggled to complete the
>entire sheet in time. My dad noticed this, decided it
>was unacceptable for me to take longer than a couple
>seconds to evaluate a simple equation, and began writing
>a program in Java. Within a couple weeks he had created
>the functional prototype of a digital addition program.
>He had me spend about an hour per day practicing on it,
>and within a few months I was able to sum any two single
>digit numbers in roughly two seconds. It was very slow
>going at the start, partly due to the number row being
the only way to input numbers. The program would save
>the high score in a hidden text file, and I would compete
>with myself to push it as high as possible. At first I
>would average around 12 per minute, but every day the
>number  slowly climbed. Around the time I was averaging
>mid 30 scores, we started doing similar worksheets in
>class with multiplication. Twenty minutes of modification,
>ten minutes of compilation later, and I was the proud
>owner of both addition and multiplication variants of
>the program. There were never subtraction or division
>variants. Possibly because we never had warm up sheets
>with those operations, potentially due to him entering
>a period of life bereft of free time, but I suspect it
>was because he moved on before figuring out how to serve
>the equations back properly as I had already learned math.
>Reversing and porting his logic from memory, extending
>the available operations, adding difficulty brackets
>via parameterized bounds, colors, sounds, and a full
>scoreboard database are my contributions to his idea.
>
>My dad's programs didn't teach me math, nor were they
>designed to. They were created to provide me with an
>adequate environment to practice and track my progress
>while learning. This program works the same way. There
>is no attempt to teach the user how to perform math
>operations, however anybody who can perform addition,
>subtraction, multiplication, and division can use this
>program to hone their solution speed.

I'm proud to have been able to put this together myself,
and to be releasing it as a free and open source project.
Contrarily I do accept coffee donations, but even if I
don't receive a cent I'll happily maintain and improve
this program in perpetuity as time permits. It's like
helping an old friend that once helped me. I just hope
it might help you too.

CashApp: $CoffeePhreak

Fellow Brave users can also drop me BAT



My PB for addition/easy is 62 with 1 missed, set 12/25/2023





## ABOUT THE CODE
>First off I'd like to announce my awareness of disregard
>for standard Python code formatting, it's the first thing
>I expect other devs to notice. My code convention, though
>non-standard, should be consistent. My functions are snake
>cased, variables camel cased, classes capital cased, and
>I prefix internal 'private' methods with an underscore.
>I dont 'privitize' variable names. They're used much more
>frequently, and the classes aren't currently generic enough
>to reuse without moderate refactoring. I enclose meaningful
>strings in 'single ticks' (like 'bold' or 'active') and
>display text or strings where the character order does
>not matter with "double quotes" (like sticky="ew").

>Tested and working in Win10 and Manjaro, but sound currently
>only works with Windows. I'm working on finding a native way
>to send async sound through both Mac and Linux. A hard fast
>rule I'd like to stick to is not having dependencies outside
>of the standard modules, in order to increase accessibility.
>I could send sound with pygame or playsound, but then the
>user needs to install another module to use the program and
>I'd rather sacrifice sound for now.

## Note on timer accuracy:
>It's not the most accurate. In a competitive setting, and
>depending on the system running it, the timer accuracy may
>be objectively unacceptable. I added a performance counter
>in Frames.py to quickly test the variance between the quiz's
>'implied time to complete' and the 'actual time to complete'.
>Simply uncomment lines: 2, 168, 175, and 179 and run MadMath.pyw
>from a command line or terminal to view. The variance on my
>machine averages 60.3 - 60.4 seconds which is acceptable for
>a local scoreboard in my use case. This import also breaks my
>one import rule, but once a more accurate timer is incorporated
>its related code will be removed.

### SOUND CREDITS
[correct](freesound.org/people/nicholasdaryl/sounds/563355)

[incorrect](freesound.org/people/Bertrof/sounds/131657)

[highscore](freesound.org/people/bone666138/sounds/198874)
