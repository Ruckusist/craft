import os
from shutil import copyfile, copytree, rmtree

def get_current_version(dirs=None) -> None:
    game_path = os.path.join(dirs[-1], 'game')
    with open(os.path.join(game_path, 'version.txt'), 'r') as f:
        version = f.readline().split(' ')[1].rstrip("\n")
    return version

def backup_settings(dirs=None) -> None:
    files = [
        'banned-ips',
        'banned-players',
        'ops',
        'usercache',
        'whitelist'
    ]
    game_path = os.path.join(dirs[-1], 'game')
    dest_path = os.path.join(dirs[-1], 'user_settings')
    for file in files:
        filepath = os.path.join(game_path, f"{file}.json")
        filedest = os.path.join(dest_path, f"{file}.json")
        if os.path.exists(filepath):
            copyfile(filepath, filedest)
        else:
            print(f"{file}.json does not exist")
    filepath = os.path.join(game_path, f"server.properties")
    filedest = os.path.join(dest_path, f"server.properties")
    if os.path.exists(filepath):
        copyfile(filepath, filedest)
    else:
        print(f"server.properties does not exist")
    return True

def backup_world(dirs=None) -> None:
    game_path = os.path.join(dirs[-1], 'game')
    file_path = os.path.join(game_path, f"server.properties")
    with open(file_path, 'r') as f:
        data = f.readlines()
        for line in data:
            if 'level-name' in line:
                world = line[11:].rstrip("\n")
    world_path = os.path.join(game_path, world)
    dest_path = os.path.join(dirs[-1], 'backup_world', world)
    if os.path.isdir(dest_path):
        if os.path.isdir(dest_path+'_old'):
            rmtree(dest_path+'_old')
        if copytree(dest_path,dest_path+'_old'):
            rmtree(dest_path)
    if os.path.isdir(world_path):
        copytree(world_path, dest_path)
    return world

def swapin_new_server(ver) -> None:
    path = ver['file_path']
    root = os.getcwd()
    game_path = os.path.join(root, 'game')
    for file_name in os.listdir(game_path):
        if 'server.jar' in file_name:
            os.remove(os.path.join(game_path, file_name))
            print('removed old Minecraft Version.')
    dest_path = os.path.join(game_path, 'server.jar')
    copyfile(path, dest_path)
    with open(os.path.join(game_path, 'version.txt'), 'w') as f:
        f.write(f"version: {ver['version']}")
    return True

def restore_user_settings(dirs=None) -> None:
    game_path = os.path.join(dirs[-1], 'game')
    source_path = os.path.join(dirs[-1], 'user_settings')
    for file in os.listdir(source_path):
        filepath = os.path.join(source_path, file)
        if os.path.exists(os.path.join(game_path, file)):
            os.remove(os.path.join(game_path, file))
        copyfile(
            os.path.join(source_path, file),
            os.path.join(game_path, file)
        )
