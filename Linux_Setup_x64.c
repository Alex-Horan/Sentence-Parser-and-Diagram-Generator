#include <stdio.h>
#include <stdlib.h>

int main() {
    //downloads the setup python script
    system("curl https://raw.githubusercontent.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator/master/setup_files/Installer_linux_x64.py -o Installer_linux_x64.py; python3 ./Installer_linux_x64.py");
    //runs the setup
    
    //testing
    system("echo 'testing\n'; echo 'testing 2'");
    return 0;
}