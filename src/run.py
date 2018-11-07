import asyncio
import pexpect

def get_java_exe():
    exe = pexpect.spawn('/bin/bash', ['-c', 'which java'])
    return str(exe.readline())[2:-5]

def launch_game(game_path):
    java_exe = get_java_exe()
    print(f"Launching Java: {java_exe}")
    exe = pexpect.spawn(java_exe, ['--version'])
    print( str(exe.readline())[2:-5] )
    print('-'*25)
    exe = pexpect.spawn(java_exe, [
        '-Xmx4G', '-Xms2G', '-jar', game_path, 'nogui'
        ])
    return exe

def game_loop(exe):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(game(exe))


async def game(exe):
    counter = 0
    while True:
        print(f"test {counter}")
        if exe.readlines():
            for i in data:
                print(i)
        else:
            input = raw_input("to_server> ")
            exe.send(str(input))
        # exe.expect('*.')
        asyncio.sleep(1)
        counter += 1
