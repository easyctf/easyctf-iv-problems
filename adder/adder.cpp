#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
//y0u_added_thr33_nums!
char * gen (int thing){
    char *flag = (char*) (malloc(22 * sizeof(char)));
    flag[0] = 'y';
    flag[1] = (thing % 7) + 48;
    flag[2] = thing - 1220;
    flag[3] = '_';
    flag[4] = flag[2] - 20;
    flag[5] = flag[4] + 3;
    flag[6] = flag[5];
    flag[7] = 'e';
    flag[8] = flag[6];
    flag[9] = flag[3];
    flag[10] = 116;
    *(flag + 11) = flag[10] - 12;
    *(flag + 12) = 'r';
    flag[13] = '3';
    flag[14] = '3';
    flag[15] = flag[3];
    flag[16] = 'n';
    flag[17] = flag[2];
    flag[18] = flag[16] - 1;
    flag[19] = 's';
    flag[20] = 33; 
    flag[21] = '\n';
    return flag;
}

void print_ptr(char * flag){
    for(int i = 0; i < 21; i++){
        printf("%c", *(flag+i));
    }
}

int main(){
  int first = 0;
  int second = 0;
  int third = 0;
  cout<<"Enter three numbers!\n";
  cin>>first>>second>>third;
  char * flag = gen(first+second+third);
  if(first + second + third == 1337){
    cout<<"easyctf{";
    print_ptr(flag);
    printf("}\n");
  }
  else
    cout<<"nope.\n";
  free(flag);
  return 0;
}
