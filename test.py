import os, asyncio, sys

async def chase_app():
    os.chdir(os.path.join(os.getcwd(), 'game')) # need this
    cmd =\
        "/usr/bin/java -Xmx4G -Xms2G -jar /network/craft/game/server.jar nogui"
    process = await asyncio.create_subprocess_exec(
        '/bin/bash', '-c', cmd,
        stdin=asyncio.subprocess.PIPE,  # <- default
        # stdout=asyncio.subprocess.PIPE,  # <- default
        stdout=open('logs/command.log', 'w')  # <- this works fine
    )
    os.system('clear')
    print('#'*40);print('Started Command:');print(cmd);counter = 0
    while True:
        # print(counter)
        await asyncio.sleep(.1)
        try:
            output, _ = await asyncio.wait_for(
                process.communicate(), timeout=0.1 )
        except: output = 0
        if output:
            counter = 0
            try: print(output.decode('ascii').rstrip())
            except: print(output.decode('utf-8').rstrip()); pass

        else: counter += 1
        if counter > 100:
            process.stdin.write(b"/say Hello World!")
            await process.stdin.drain()
            process.stdin.write_eof()
            """
            # process.stdin.write('help'.encode(encoding='ascii'))
            # process.stdin.flush()
            try:
                x, y = await asyncio.wait_for(
                    process.communicate(
                        '/say Hello World!'.encode(encoding='ascii')
                    ),
                    timeout=2.5
                )
                # print(x)
            except Exception as e:
                print(repr(e))
                # break
            """
            counter = 0


asyncio.run(chase_app())
print('fin')
