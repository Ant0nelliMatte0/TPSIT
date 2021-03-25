#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#define MAX 1000
typedef struct s_musica{
	int  num;
	char nome[100];
	char cantante[100];
	bool rip;
    musica* next;
} musica;
void Mem(musica* Playlist, FILE* pt);
void RipCasuale(musica* Playlist);
int main()
{
    musica* Playlist;
    FILE *pt;
    pt=fopen("playlist.csv", "r");
    if (pt){
            printf("file file aperto correttamente\n");
            Mem(Playlist,pt);
            RipCasuale(Playlist);
            fclose(pt);
    return 0;
    }
    else {
        printf("errore durante l'apertura del file!");
    }
}
void Mem(musica** head, FILE* pt){
            musica* elemento;
            int j=0;
            char vet[MAX];
            const char *c = ",";
            char *field;
            while (fgets(vet,MAX,pt)){
            field = strtok(vet, c);
            Playlist[j].num = atoi(field);
            printf("numero: %d\n",Playlist[j].num);
            strcpy(Playlist[j].nome, strtok(NULL, c));
            printf("titolo: %s\n",Playlist[j].nome);
            strcpy(Playlist[j].cantante, strtok(NULL, c));
            Playlist[j].cantante[strlen(Playlist[j].cantante)-1] = '\0';
            printf("cantante: %s\n",Playlist[j].cantante);
            j++;
            }

    }
    void RipCasuale(musica* Playlist){
        int a,n,f=0;
        srand(time(NULL));
        printf("\n");
        printf("riproduzione\n");
        for (f=0;f<10;f++){
            Playlist[f].rip=false;
        }
        for (a=0;a<10;a++){
            do {
            n = rand() % 10;
            }
            while(Playlist[n].rip==true);
            printf("titolo: %s, cantante: %s\n", Playlist[n].nome, Playlist[n].cantante);
            Playlist[n].rip=true;

        }
    }
