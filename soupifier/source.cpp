#include "stdio.h"
#include "math.h"
#include <iostream>
#include <stdexcept>
using namespace std;

void print_error(){
	//STUB
	/*ifstream reader;
 	reader.open("flag.txt");
 	char output[100];
 	if (reader.is_open()) {
 		while (!reader.eof()) {
    		reader >> output;
    		cout<<output;
 		}
 		printf("\n");
	}
	reader.close();
	*/
	printf("hi\n");
}
bool soupify_string_successful(string input, short* ret, int counter)
{
    counter++;
    int upper = input.length();
    if(upper > 500)
        upper = 500;
    for(int i = 0; i < upper; i++){
	if(*ret < 0) return false;
	*ret += (short)(input.at(i));
    }
    input = "";
    cout<<"Input another string! ";
    cin>>input;
    if(counter == 3){
    	printf("Now soupifying! \n");
    	return true;
    }
    return soupify_string_successful(input, ret, counter);
}
int main()
{
    string input = ""; //really bad mix of C and C++?
    printf("Welcome to the Souper Magic Soup Number Generator! Input your string: ");
    cin>>input;
    short start = 4;
    short* short_ptr = &start;
    if(soupify_string_successful(input, short_ptr, 0)){
	if(sqrt(*short_ptr) > 0){
	    cout<<"\nYour soup number is: "<<sqrt(*short_ptr)<<".\n";
	    return 0;
	}
	else{
            print_error();
        }
    }
    else{
 	printf("Soupify failed!\n");
    }
    return 0;
}
