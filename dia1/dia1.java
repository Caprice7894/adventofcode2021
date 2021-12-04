class dia1{
	int main(){
		int increases = 0;
		for (int i = 3; i < input.size(); i++){
			increases += input.get(i) > input.get(i - 3) ? 1:0;
		}
		return 0;
	}
}
