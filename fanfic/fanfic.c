//gcc -m32 -std=c99 -Wall -fno-stack-protector heaps_of_knowledge.c -o heaps_of_knowledge
#define _GNU_SOURCE
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>

struct chapter {
    struct chapter *prev_chapter;
    struct chapter *next_chapter;
    char title[50];
    char content[256];
    void (* print_ch)(int, struct chapter *);
};

typedef struct chapter chapter;

typedef struct fanfic {
    char *title;
    int num_chapters;
    chapter *first_chapter;
} fanfic;

fanfic *create_fanfic(char *title) {
    fanfic *b = malloc(sizeof(fanfic));
    b->title = strdup(title);
    b->first_chapter = NULL;
    b->num_chapters = 0;
    return b;
}

void print_chapter(int num, chapter *ch) {
    printf("\n---------------\n");
    printf("Chapter %i: %s", num, ch->title);
    printf("\n---------------\n");
    printf("%s\n", ch->content);
}



int success = 0xFFFF;
void validate(int ans) {
    if ((ans ^ 0xDEADBEEF) == 0xDEADBEAF) {
        success = 0xC001B4B3;
    }
}

void be_nice() {
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
}

void give_flag() {
    be_nice();
    FILE *f = fopen("flag.txt", "r");
    if (success==0xC001B4B3) {
        if (f != NULL) {
            char c;
            while ((c = fgetc(f)) != EOF) {
                putchar(c);
            }
        }
        else {
            printf("Couldn't open flag file!\n");
        }
    }
    else {
        printf("nope! \n");
    }
    fclose(f);
}



int i;
int num_ch;
char option[4];
int option_val;
int main(int argc, char *argv[]) {
    printf("Please enter the title of your brand new fanfic: ");
    char title[50];
    char text[256];
    fgets(title, 50, stdin);
    
    //get rid of newline
    title[strlen(title)-1] = '\0';
    
    printf("You have started writing the fanfic '%s'. Please select an option to get started!\n", title);

    fanfic *fanfic = create_fanfic(title);
    while(1) {
        printf("1. Edit chapter\n");
        printf("2. Delete chapter\n");
        printf("3. Publish fanfic\n");
        printf("> ");
        i=0;
        num_ch = fanfic->num_chapters;
        chapter *curr_ch;

        fgets(option, 4, stdin);
        option_val = atoi(option);

        switch(option_val) {
        case 1: //edit
            printf("Enter chapter number to edit: ");
            fgets(option, 4, stdin);
            
            option_val = atoi(option);

            if (option_val > 0 && option_val <= num_ch) {
                printf("Editing chapter\n");      
                printf("Enter new chapter text: \n");
               
                curr_ch = fanfic->first_chapter;
                for (i=1; i<option_val; i++) {
                    curr_ch = curr_ch->next_chapter;
                }
                gets(curr_ch->content);   
            }
            else if (option_val == num_ch+1) {
                printf("Adding new chapter\n");
                printf("Enter chapter title: ");
                fgets(title, 50,  stdin);
                title[strlen(title)-1] = '\0';
                printf("Enter chapter contents: ");
                fgets(text, 256, stdin);
                text[strlen(text)-1] = '\0';
                
                chapter *ch = malloc(sizeof(chapter));
                strcpy(ch->title, title);
                strcpy(ch->content, text);
                //ch->title = strdup(title);
                //ch->content = strdup(text);
                ch->print_ch = &print_chapter;

                curr_ch = fanfic->first_chapter;
                fanfic->num_chapters++;
                if (curr_ch == NULL) {
                    fanfic->first_chapter = ch;
                }
                else {
                    while (curr_ch->next_chapter != NULL) {
                        curr_ch = curr_ch->next_chapter;
                    }

                    curr_ch->next_chapter = ch;
                    ch->prev_chapter = curr_ch;
                }
            }
            else {
                printf("Invalid chapter number!\n"); 
                return 0;
            }
            break;
        case 2: //delete
            printf("Enter chapter number to delete: ");
            fgets(option, 4, stdin);

            option_val = atoi(option);

            if (option_val > 0 && option_val <= num_ch) {
                printf("deleting chapter\n");
                fanfic->num_chapters--;
                if (option_val == 1) {
                    
                    chapter *old_first = fanfic->first_chapter;
                    fanfic->first_chapter = old_first->next_chapter;
                    free(old_first->title);
                    free(old_first->content);
                    free(old_first);
                    if (fanfic->first_chapter != NULL)
                        fanfic->first_chapter->prev_chapter = NULL;
                }
                else {
                    curr_ch = fanfic->first_chapter;
                    for(i=2;i<option_val;i++) {
                        curr_ch = curr_ch->next_chapter;
                    }
                    
                    chapter *to_del = curr_ch->next_chapter;

                    curr_ch->next_chapter = to_del->next_chapter;
                    if (to_del->next_chapter != NULL)
                        to_del->next_chapter->prev_chapter = to_del->prev_chapter;
                    
                    free(to_del->title);
                    free(to_del->content);
                    free(to_del);
                }
            }
            else {
                printf("Invalid chapter number!\n");
                return 0;
            }
            break;
        default: //publish
            printf("Fanfic published! Here it is:\n");
            printf("===============\n");
            printf("%s\n", fanfic->title);
            printf("===============\n");
            i = 1;
            curr_ch = fanfic->first_chapter;
            while (curr_ch != NULL) {
                curr_ch->print_ch(i, curr_ch);
                curr_ch = curr_ch->next_chapter;
                i++;
            }
            return 0;
        }
    }
    return 0;
}
