#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 52

typedef struct carte  //definisco la struttura
{
    char seme;  //variabile "seme"
    int val;    //vaiabile "val" per il vaklore della carta
    carte *next;  
}carte;

void enqueue(carte **head, carte **tail, carte *elemento) // funzione per aggiungere un elemento alla coda
{
    if(is_empty(*head)) //verifico se la prima cella è libera
    {
        *head = elemento; //se è libera inserisco l'elemento
    }
    else
    {
        *tail -> next = elemento; //se è occupata lo metto in qella dopo
    }   
    *tail = elemento;
    elemento -> next = NULL;    
}

carte* dequeue(carte **head, carte **tail, carte *elemento) //funzione per togliere un elemento dalla coda
{
    carte* ret = *head;
    if (is_empty(*head))  //verifico se l'HEAD è vuoto
    {
        return NULL;  //se l'HEAD è vuoto non faccio niente
    }
    else
    {
        *head = ret -> next  
    }
    
    if(*head == NULL)  //se HEAD = NULL entro nell'if
    {
        *tail = NULL;   //se HEAD è NULL metto anche TAIL a NULL
    }
    
    return ret;
}

char setSeme(int c)  //definire il seme delle carte 
{
    char seme;
    if(c < 13)  //carte con il seme dei cuori
    {
        seme = 'C';
    }
    if(c > 13 && c < 26)  //carte con il seme dei quadri
    {
        seme = 'D';
    }
    if(c > 26 && c < 39)   //carte con il seme dei fiori
    {
        seme = 'F';
    }
    if(c > 39 && c < MAX)   //carte con il seme dei picche
    {
        seme = 'P';
    }
    else
    {
        printf("errore");
    }

    return seme;
}

int main()
{
    carte *tail;
    carte *head;
    carte *valore;
    int contatore = 0;
    char seme;
    head = NULL;
    tail = NULL;

    while(contatore < MAX)  //ciclo WHILE
    {
        seme=setSeme(contatore);
        head = (carte*) malloc (sizeof(carte));  
        tail = (carte*) malloc (sizeof(carte));  
        for(int j = 1; j < 14; j++)
        {
            valore = (carte*)malloc(sizeof(carte));
            valore->val=i;
        }
    }
    
    
}
