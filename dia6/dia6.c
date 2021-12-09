#include <stdio.h>

int main(){
	int INPUT[5] = {3,4,3,2,1};
	int DIAS = 18;
	int i = 0;
	int suma = 0;
	printf("%d, %d\n", DIAS, i);
	int contador[9] = {0,0,0,0,0,0,0,0,0};
	for(i = 0; i < 5; i++){
		contador[INPUT[i]] += 1;
		printf("contador: %d\n", contador[INPUT[i]]);
	}

	for(i = 0; i < DIAS; i++){
		int dia = 0;
		int _t = 0;
		int _c[9] = {0,0,0,0,0,0,0,0,0};
		for(dia = 0; dia < 9; dia++){
			_t = contador[dia];
			if (dia == 0){
				_c[6] += contador[0];
				printf("%d-",_c[6]);
				_c[8] += contador[0];
				_c[0] = 0;
			}else{
				_c[dia - 1] = _t;
			}
		}
		for(dia = 0; dia < 9; dia++){
			contador[dia] = _c[dia];
		}
	}

	for(i = 0; i < 9; i++){
		suma += contador[i];
	}
	printf("\n %d", suma);
	return 0;
}






