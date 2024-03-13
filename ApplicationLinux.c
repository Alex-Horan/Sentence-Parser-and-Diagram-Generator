#include <stdio.h>
#include <stdlib.h>

int main() {
    system("source ../App/bin/activate; python3 -m flask --app FlaskServer run");
    system("npm start");
    return 0;
}