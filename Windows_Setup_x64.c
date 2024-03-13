#include <stdio.h>
#include <stdlib.h>

int main() {
    //downloads setup python script
    system("curl https://raw.githubusercontent.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator/master/setup_files/Installer_windows_x64.py -o Installer_windows_x64.py");
    //runs said script
    system("py ./Installer_windows_x64.py");
    return 0;
}