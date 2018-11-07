import os

dirs = [
    'backup_world',
    'game_versions',
    'game',
    'user_settings',
]

files = [
    'banned-ips',
    'banned-players',
    'ops',
    'usercache',
    'whitelist'
]

settings = """#Minecraft server properties
#Mon Oct 22 23:29:41 UTC 2018
view-distance=10
max-build-height=256
server-ip=
level-seed=
allow-nether=true
enable-command-block=false
server-port=25565
gamemode=0
enable-rcon=false
op-permission-level=4
enable-query=false
prevent-proxy-connections=false
generator-settings={"useCaves"\:true,"useStrongholds"\:true,"useVillages"\:true,"useMineShafts"\:true,"useTemples"\:true,"useRavines"\:true,"useMonuments"\:true,"useMansions"\:true,"useLavaOceans"\:false,"useWaterLakes"\:true,"useLavaLakes"\:true,"useDungeons"\:true,"fixedBiome"\:-3,"biomeSize"\:4,"seaLevel"\:63,"riverSize"\:4,"waterLakeChance"\:4,"lavaLakeChance"\:80,"dungeonChance"\:8,"dirtSize"\:33,"dirtCount"\:10,"dirtMinHeight"\:0,"dirtMaxHeight"\:255,"gravelSize"\:33,"gravelCount"\:8,"gravelMinHeight"\:0,"gravelMaxHeight"\:255,"graniteSize"\:33,"graniteCount"\:10,"graniteMinHeight"\:0,"graniteMaxHeight"\:80,"dioriteSize"\:33,"dioriteCount"\:10,"dioriteMinHeight"\:0,"dioriteMaxHeight"\:80,"andesiteSize"\:33,"andesiteCount"\:10,"andesiteMinHeight"\:0,"andesiteMaxHeight"\:80,"coalSize"\:17,"coalCount"\:20,"coalMinHeight"\:0,"coalMaxHeight"\:128,"ironSize"\:9,"ironCount"\:20,"ironMinHeight"\:0,"ironMaxHeight"\:64,"goldSize"\:15,"goldCount"\:5,"goldMinHeight"\:0,"goldMaxHeight"\:32,"redstoneSize"\:8,"redstoneCount"\:8,"redstoneMinHeight"\:0,"redstoneMaxHeight"\:16,"diamondSize"\:15,"diamondCount"\:5,"diamondMinHeight"\:0,"diamondMaxHeight"\:16,"lapisSize"\:20,"lapisCount"\:5,"lapisMinHeight"\:0,"lapisMaxHeight"\:32,"coordinateScale"\:485,"heightScale"\:1406,"mainNoiseScaleX"\:80,"mainNoiseScaleY"\:160,"mainNoiseScaleZ"\:80,"depthNoiseScaleX"\:200,"depthNoiseScaleZ"\:200,"depthNoiseScaleExponent"\:0.5,"biomeDepthWeight"\:2,"biomeDepthOffset"\:1,"biomeScaleWeight"\:1.2,"biomeScaleOffset"\:1.8,"lowerLimitScale"\:512,"upperLimitScale"\:563,"baseSize"\:9.6,"stretchY"\:12,"lapisCenterHeight"\:16,"lapisSpread"\:16}
resource-pack=
player-idle-timeout=0
level-name=RuckusCraft
motd=awesome this works
force-gamemode=true
hardcore=false
white-list=false
pvp=true
spawn-npcs=true
generate-structures=true
spawn-animals=true
snooper-enabled=false
difficulty=3
network-compression-threshold=256
level-type=CUSTOMIZED
spawn-monsters=true
max-tick-time=60000
enforce-whitelist=false
use-native-transport=true
max-players=20
resource-pack-sha1=
online-mode=false
allow-flight=false
max-world-size=999
"""

def setup(root=None) -> list:
    root = os.getcwd()
    for dir in dirs:
        if not os.path.isdir(os.path.join(root, dir)):
            os.mkdir(os.path.join(root, dir))
    # in game folder place a version.txt
    if not os.path.exists(os.path.join(root, 'game', 'version.txt')):
        with open(os.path.join(root, 'game', 'version.txt'), 'w+') as f:
            f.write('version: None')
    # in user_settings folder place a eula.txt
    if not os.path.exists(os.path.join(root, 'user_settings', 'eula.txt')):
        with open(os.path.join(root, 'user_settings', 'eula.txt'), 'w+') as f:
            f.write('eula=true')
    # in the user_settings folder place a server.properties
    if not os.path.exists(os.path.join(root, 'user_settings', 'server.properties')):
        with open(os.path.join(root, 'user_settings', 'server.properties'), 'w') as f:
            f.write(settings)
    # build out the rest of user_settings
    for file in files:
        if not os.path.exists(os.path.join(root, 'user_settings', f"{file}.json")):
            with open(os.path.join(root, 'user_settings', f"{file}.json"), 'w') as f:
                f.write("[]")
    dirs.append(root)
    return dirs

# setup()
