# GrowCastle-Auto-Bot
This is an auto play bot created for Grow Castle, it automaticly will start the game, use any possible heros including for example mags (witch need another click to deploy their skills) and then end game, wait a few seconds and do the same. 

To use the bot you need to have 1920x1080 screen
You need to play on PC by bluestack
You need to turn-ON the fullscreen option inside of the blue stack so the game take every bit of your 1920x1080 screen

After turning on the  script from the VS or any other IDE you will see a window where you have 2 options (for now) and a console for logging so you know what the bot is doing.

The first button is Start the bot, witch well - starts the bot

The second button is a stop button witch will stop the bot from clicking.
The hold Q feture is not working by now, i reccomend waiting till the of the wave to click it manually, if you screw something up and the bot will start to click stuff he shouldn't you need to open task menager and kill the execuatble or your IDE.

Bot is not blindly clicking on X and Y cords hoping it's a good moment, he reads the color of bars and then he decide is it time to click it. So don't worry it won't delete anything by accident

Id you want to export this to exe i will reccomend pyinstaller, simply pip install it go to the folder when you have the app.py and type this into the CMD 
  python -m PyInstaller app.py --onefile -w

I also want to say that bots are not allowed by the creators of the Grow Castle, this is ONLY for education ;)

Good luck and have fun!
