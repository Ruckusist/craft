import os

from src.download import get_mincraft_versions, download_new_version
from src.update import get_current_version, backup_settings, backup_world, swapin_new_server, restore_user_settings
from src.setup import setup
from src.run import launch_game, game_loop
if True:
    dirs = setup()
    versions = get_mincraft_versions(dirs)
    recent_version = list(versions)[0]
    last_version = list(versions)[1]
    current_version = get_current_version(dirs)
    print(f"Current Minecraft Version: {current_version}")
    print(f"Most Recent Version: {recent_version}")
    need_update = False
    if current_version not in str(recent_version):
        print(f'Minecraft needs update to {recent_version}')
        need_update = True
        if 'None' in current_version:
            need_update = False
    if need_update:
        ver = versions[recent_version]
        print('Starting Backup and Update.')
        backup_settings(dirs)
        print('Backed up User Settings')
        world_name = backup_world(dirs)
        print(f'Backed up World: {world_name}')
        print(f'Downloading New Version: {recent_version}')
        rollback_server_filepath = download_new_version(versions[last_version])
        ver['file_path'] = download_new_version(ver)
        swapin_new_server(ver)
        print(f'Finished Update to Version: {recent_version}')
    if 'None' in current_version:
        print('Starting a fresh install.')
        ver = versions[recent_version]
        ver['file_path'] = download_new_version(ver)
        restore_user_settings(dirs)
        swapin_new_server(ver)
        print(f"Finished Setting up Minecraft Server v: {ver['version']}")
# # # # # # #
if False:
    dirs = setup()
    os.chdir(os.path.join(os.getcwd(), 'game'))
    launch_file = os.path.join(dirs[-1], 'game', 'server.jar')
    running_game = launch_game(launch_file)
    # This runs an asyncio loop elsewhere.
    game_loop(running_game)
    print('test')
