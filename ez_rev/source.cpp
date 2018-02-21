#include <unistd.h>
#include <stdio.h>
#include <cstdio>
#include <signal.h>

char * target;
void print_5(int * arr){
    printf("%d%d%d%d%d\n", arr[0], arr[1], arr[2], arr[3], arr[4]);
    return;
}

void sigintHandler(int sig_num)
{
    signal(SIGINT, sigintHandler);
    printf("\n You thought you could avoid it huh?\n");
    fflush(stdout);
    std::remove(target);
}

int main( int argc, char * argv[] ){
    signal(SIGINT, sigintHandler);
    target = argv[0];
    switch( argc ){
        case 2: goto TOP;
        default: goto SAD;
    }    
    SAD: return 2;
    TOP: char * input = argv[1];
         int arr [] = {1, 2, 3, 4, 5}; 
         arr[0] += input[0];
         arr[1] += input[1];
         arr[2] += input[2];
         arr[3] += input[3];
         arr[4] += input[4];
         if (arr[3] == 111){
             if(arr[2] == arr[3] + 14){
                 if(arr[0] == arr[4] - 10){
                      if((arr[1] == 53) && (arr[4] == arr[3] + 3)){
                          printf("Now here is your flag: ");
                          print_5(arr);
                          return 1;
                      }   
                 }   
             }   
         }   
         goto END;
    END: 
         sleep(2);
         std::remove(argv[0]);
         printf("successfully deleted!\n");
         return 2;
}

