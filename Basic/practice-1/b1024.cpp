#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
	double dig1, result;
	int dig2;
	char input[255];
	cin >> input;

	char *p = strtok(input, "E");

	sscanf(p, "%lf", &dig1); 

	p = strtok(NULL, "E");

	sscanf(p, "%d", &dig2); 

	result = dig1 * pow(10.0, dig2);

	cout << fixed << result << endl;

	return 0;
}