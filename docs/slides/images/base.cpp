#include <iostream>
int main(){
	int somme = 0;
	int n = 5; /* Connu à l'éxécution*/

	for(int i = 0; i < n; i++){
		somme += i;
	}

	for(int i = 0; i < n; i++){
		somme += n - i;
	}

	std::cout << somme << std::endl;
}
