import subprocess
import os
import sys

# UE_PATH = "E:\\Unreal Engine\\UE_4.27" # by yourself

arg1 = sys.argv[1]

count = 0
UE_PATH = ""
with open('C:\\ProgramData\\Epic\\UnrealEngineLauncher\\LauncherInstalled.dat', 'rb') as file: # read LauncherInstalled.dat to get UE_PATH
    for line in file:
        # Process each line as needed
        if count==3:
            decode_line = line.decode('utf-8')
            result = decode_line.split(':')
            part_one = result[1] # "E
            part_two = result[2].split('"')[0]
            UE_PATH = part_one + ":" + part_two
            break;
        count += 1

project_name = folder_name = os.path.basename(os.path.dirname(__file__)) # get project name
folder_path = os.path.dirname(os.path.abspath(__file__)) # get path

if arg1=="clean":
    command = '&'+f'{UE_PATH}\\Engine\\Build\\BatchFiles\\Clean.bat" ' + project_name + 'Editor Development Win64 ' + f'"{folder_path}\\{project_name}.uproject"' # Clean Command
elif arg1 == "generate":
    command = '&'+f'{UE_PATH}\\Engine\\Binaries\\DotNET\\UnrealBuildTool.exe" -projectfiles -project="{folder_path}\\{project_name}.uproject" -game -rocket -progress' # Generate Command
elif arg1 == "build":
    command = '&'+f'{UE_PATH}\\Engine\\Build\\BatchFiles\\Rebuild.bat" ' + project_name + 'Editor Development Win64 ' + f'"{folder_path}\\{project_name}.uproject"' # Build Command
else:
    print("请输入clean, generate, 或build")

subprocess.run(['powershell', '-Command', command])




