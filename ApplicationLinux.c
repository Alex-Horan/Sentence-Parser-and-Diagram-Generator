#include <stdio.h>
#include <stdlib.h>

int main() {
    system("echo $PWD; source ../App/bin/activate; python3 -m flask --app FlaskServer run");
    system("npm start");
    return 0;
}