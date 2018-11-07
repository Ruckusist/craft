A Python Wrapper for the Minecraft Server Java Program.

Features:
    - checks for recent version from mcversion.net
    - downloads most recent verison (any version)
    - backup world for compaitibity check on server upgrade
    - easily add in custom world params for more interesting vanilla games

Current broken upgrade in progress:
To hold and further communicate with the runnning server process from python,
using asyncio.

Which leads to:
To run a aiohttp(asyncio webserver) websocket server also attached to the
running java process which can then send and receieve messages from the server.

which leads to:
    - To run a slack style chatbot in the server
    - to run a tensorflow chatbot in server
    - to allow access to the server and ingame chat from a webfrontend.

# Current issue:
    having trouble talking to the server from stdin = asyncio.subprocess.PIPE.
    it will talk once and then it cant talk again on that pipe? so it needs
    another one? every loop? i dont understand.
    link to probable solution:
        - https://docs.python.org/3/library/asyncio-subprocess.html

# Steps to recreate issue
git clone https://github.com/Ruckusist/craft
cd craft
python3 craft.py
python3 test.py
- check game/logs/command.log for the stdout of that last crashed run
- there is clearly 1 Hello World in there... but thats it.
- pick up right here.


######
Thanks
######
@ mcversion.net
This relies heavily on mcversion.net. They provide a cool service.
