#include <stdio.h>
#include <stdlib.h>

int main() {
    //downloads the setup python script
    system("curl https://raw.githubusercontent.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator/master/setup_files/Installer_windows_x64.py -o Installer_Windows_x64.py");
    system("py ./Installer_Windows_x64.py");
    return 0;
}