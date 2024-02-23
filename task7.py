import subprocess
import time
import pyautogui

# Function to open Visual Studio Code
def open_vscode():
    subprocess.Popen(["code"])

# Function to install an extension
def install_extension(extension_name):
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(9)
    pyautogui.write('ext install ' + extension_name)
    time.sleep(9)
    pyautogui.press('enter')
    
    time.sleep(9)  # Wait for installation to complete

# Open Visual Studio Code
#open_vscode()

time.sleep(9)
# Install clangd extension
install_extension('llvm-vs-code-extensions.vscode-clangd')
time.sleep(9)
# Install C++ TestMate extension
install_extension('matepek.vscode-catch2-test-adapter')
time.sleep(9)

# Install C++ Helper extension
install_extension('austin.code-gnu-global')
time.sleep(9)
# Install CMake extension
install_extension('twxs.cmake')

# Note: Adjust waiting times as needed, and be aware that this script might need adjustments based on your system and VS Code configuration.
