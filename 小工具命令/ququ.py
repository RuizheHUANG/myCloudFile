import subprocess
import os
import sys
import json


arg1 = sys.argv[1]

project_name = folder_name = os.path.basename(os.path.dirname(__file__)) # get project name
folder_path = os.path.dirname(os.path.abspath(__file__)) # get path
UE_PATH = ""


def parse_json_from_dat_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        return json_data

parsed_data = parse_json_from_dat_file('C:\\ProgramData\\Epic\\UnrealEngineLauncher\\LauncherInstalled.dat')
install_locations = [entry["InstallLocation"] for entry in parsed_data["InstallationList"]] # get all UE_PATH

version_data = parse_json_from_dat_file(f"{folder_path}\\{project_name}.uproject")
engine_association = version_data["EngineAssociation"] # get UE version of current project

for location in install_locations: # find UE path accoridng to current version
    if engine_association in location:
        UE_PATH = location


if arg1=="clean":
    command = '&'+f'"{UE_PATH}\\Engine\\Build\\BatchFiles\\Clean.bat" ' + project_name + 'Editor Development Win64 ' + f'"{folder_path}\\{project_name}.uproject"' # Clean Command
elif arg1 == "generate":
    command = '&'+f'"{UE_PATH}\\Engine\\Binaries\\DotNET\\UnrealBuildTool.exe" -projectfiles -project="{folder_path}\\{project_name}.uproject" -game -rocket -progress' # Generate Command
elif arg1 == "build":
    command = '&'+f'"{UE_PATH}\\Engine\\Build\\BatchFiles\\Rebuild.bat" ' + project_name + 'Editor Development Win64 ' + f'"{folder_path}\\{project_name}.uproject"' # Build Command
elif arg1 == "package-Win64":
    command = f'& "{UE_PATH}\\Engine\\Build\\BatchFiles\\RunUAT.bat" BuildCookRun -project="{folder_path}\\{project_name}.uproject" ' \
              f'-noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -cook -allmaps -build -stage -pak -archive -archivedirectory="{folder_path}\\Build"' # Package Win64 Command
elif arg1 == "package-Android":
    # 1. 覆盖JAVA_HOME为Android Studio
    try:
        override_JAVA_HOME_command = '$env:JAVA_HOME = "C:\\Program Files\\Android\\Android Studio\\jre"'
        subprocess.run(['powershell', '-Command', override_JAVA_HOME_command])
        print("Successfully override $JAVA_HOME")
    except:
        print("Fail to override $JAVA_HOME")
        exit(1);

    # 2. 往PATH里添加JAVA_bin, Andro
    try:
        username = os.getlogin()
        add_Path_command = f'$newPathEntry1 = "C:\\Users\\{username}\\AppData\\Local\\Android\\Sdk\\platform-tools"; ' \
                  f'$newPathEntry2 = "C:\\Users\\{username}\\AppData\\Local\\Android\\Sdk\\tools"; ' \
                  f'$newPathEntry3 = "%JAVA_HOME%\\bin";'\
                  f'$currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine"); ' \
                  f'$newPath = "$currentPath;$newPathEntry1;$newPathEntry2;$newPathEntry3"; ' \
                  f'$env:Path = $newPath'
        subprocess.run(['powershell', '-Command', add_Path_command])
        print("Successfully add Andro to $Path")
    except:
        print("Fail to add Andro to $Path")
        exit(1);

    command = f'& "{UE_PATH}\\Engine\\Build\\BatchFiles\\RunUAT.bat" BuildCookRun -project="{folder_path}\\{project_name}.uproject" ' \
              f'-noP4 -platform=Android -clientconfig=Development -serverconfig=Development -cook -allmaps -build -stage -pak -archive -archivedirectory="{folder_path}\\Build"'  # Package Android Command
elif arg1 == "package-IOS":
    command = f'& "{UE_PATH}\\Engine\\Build\\BatchFiles\\RunUAT.bat" BuildCookRun -project="{folder_path}\\{project_name}.uproject" ' \
              f'-noP4 -platform=IOS -clientconfig=Development -serverconfig=Development -cook -allmaps -build -stage -pak -archive -archivedirectory="{folder_path}\\Build"'  # Package IOS Command
else:
    pass

subprocess.run(['powershell', '-Command', command])




