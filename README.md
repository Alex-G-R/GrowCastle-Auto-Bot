# GrowCastle-Auto-Bot
This is an auto play bot created for Grow Castle, it automaticly will start the game, use any possible heros including for example mags (witch need another click to deploy their skills) and then end game, wait a few seconds and do the same. 

To use the bot you need to have 1920x1080 screen
You need to play on PC by bluestack
You need to turn-ON the fullscreen option inside of the blue stack so the game take every bit of your 1920x1080 screen

After turning on the  script from the VS or any other IDE you will see a window where you have some options and a console for logging so you know what the bot is doing.

The first button is Start the bot, witch well - starts the bot

The second button is a stop button witch will stop the bot from clicking.

I also added three new buttons that manage witch functions you want to use and witch not, there is: Auto castle upgrade, Auto Archers upgrade and auto Chest collect. Names speak for themselfs so i won't explain it, any needed info will be displayed in console.

Bot is not blindly clicking on X and Y cords hoping it's a good moment, he reads the color of bars and then he decide is it time to click it. So don't worry it won't delete anything by accident
Chest collect and auto upgrades are working by image recognition, the program is searching for specific images on the screen, then it gives back the location of it and finally clicks it ot not based of functions that you turned on.

If you want to export this to exe i will reccomend pyinstaller, simply pip install it go to the folder when you have the app.py and type this into the CMD:

  python -m PyInstaller app.py --onefile -w

However if you are intrasted in upgrading my bot i left some tools in the Tools folder and by tools i mean two python scripts
One - that will print you your mouse X,Y position and on top of that RGB of the pixel you are pointing to.
And second one will make a screenshot of given area of the screen and save it to AreaScreenShot folder, however you need to change the directory for yourself because it requires full directory beginning with r"C:...."
Feel free to use them because it helped me a lot

I also want to say that bots are not allowed by the creators of the Grow Castle, this is ONLY for education ;)

Good luck and have fun!
