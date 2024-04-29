<h1> BREAKOUT - a python game demo</h1>
<h2>by Christopher Lazariuk</h2>
<h3>A Final Project for the Codedex 'The Legend of Python' Course</h3>
<br>

![GameImage](/breakoutGame.png)

<p>Codedex is an online learning platform dedicated to teaching the next generation of programmers the fundamentals they need to get their foot in the door in the professional world. Check out their main website here: <a href="https://www.codedex.io/home">Codedex</a></p>

<p>Breakout is an early days of the internet computer game that acts much like single player Pong- you control a single paddle bouncing a ball against it and into a set of bricks. Destroy bricks by bouncing into them, but don't let the ball go out of bounds by missing it with the paddle, or else you'll lose a life! Check out the history of the game Breakout here: <a href="https://en.wikipedia.org/wiki/Breakout_(video_game)">Breakout Game</a></p>

<h3>GETTING STARTED</h3>
<p>
In order to run this program, there's a couple of steps we'll have to follow to get you squared away. If you've already got python3 installed you're winning the game!
<ol>
    <li>
    Start by cloning this github repo into your own local repository
    </li>
    <li>
    Open the cloned project folder in VS Code or similar IDE.
    </li>
    <li>
    You'll want to make sure you have Python 3.0 or better installed on your device. If you don't, head over to <a href="https://www.python.org/downloads/">this page</a> for the latest and greatest. Follow the instructions therein for installation of Python 3 to your device.
    </li>
    <li>
    Next, install the Python extension if you haven't already. This will allow you to run Python programs and download additional packages through pip as needed.
    </li>
    <li>
    But we're not there yet! In order to get python up and running on VSCode we'll have to make a slight but major change. On shift+cmd+p or shift + ctrl + p  in vs code to bring up your quick search options. Search open user settings (JSON) and click the resulting tab for user settings (JSON)
    </li>
    <li>
    There is a single line we must alter here in order for your device to run python code if it can't already. "python": "python -u" must be altered to read "python": "python3 -u". Sounds crazy but it's really that simple and the ship is sunk before it can even sail if we don't get that taken care of! This is due to the deprecated version of python that VS Code is initially compatible with being in need of updating to python3.
    </li>
    <li>
    Now that all of that is out of the way, we've installed Python3, enabled it to function on VSCode, and opened our cloned repo in VSCode to view it. Open the file main.py...
    </li>
    <li>
    Now all that's left is to run the code! Make sure you have the code runner extension installed on your VSCode as well, so that you can run the files in the IDE.
    </li>
    <li>
    And without further ado, while main.py is open and your currently viewed file, either click the play symbol at upper right of VSCode screen or right click and select 'run code' from the command drop down to open the game in a separate window.
    </li>
</ol>
</p>

Life and tech doesn't always have to be a massive thing. Enjoy this light and breezy game demo of a beloved childhood treasure of mine!

Tutorial for code-along at:
https://geeksforgeeks.org/create-breakout-game-using-python/
