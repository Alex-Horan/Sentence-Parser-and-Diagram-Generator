#include <stdio.h>
#include <stdlib.h>

int main() {
    system("curl https://raw.githubusercontent.com/Alex-Horan/Sentence-Parser-and-Diagram-Generator/master/setup_files/installer_windows_x64.py -o installer_windows_x64.py");
    system("py ./installer_windows_x64.py");
    return 0;
}