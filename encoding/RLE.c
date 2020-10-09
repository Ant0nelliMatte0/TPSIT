#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{   

    int input = 0; //inizializza la variabile input a 0
    printf("seleziona una opzione \n1.Encoding\n2.Deconding\n\n inserisci numero... ");
    scanf("%d",&input); // visualizza sullo schermo il menu iniziale
    if (input==1)
    {
       char str[100];                     //inizializza l'array di max 100 caratteri denominato str
    int cont = 1;                      //inizializza il contatore a 1
    
    printf("Inserire la stringa da comprimere... (max. 100 caratteri) ");  //riscrive il messasggio tra virgloette sul dispaly
    scanf("%s", str);       //inserisce il dato dentro la variabile str

    
    int n = strlen(str);       //inizializza la variabile n uguagliandola a "strlen"

    for (int i = 0; i < n; i++){          //descrive le condizioni del for e inizializza la variabile i
    while(i < n - 1 && str[i] == str[i+1]){ //descrive le condizioni del while
        cont = cont + 1;   //aumenta il contatore di 1
        i = i + 1;   //aumenta la variabile i di 1
    }
    

    printf("%d", cont);  // stampa del numero 
    cont = 1;     // eguaglia il contatore a 1
    printf("%c", str[i]); //stampa el carattere
    
}

    printf("\n\n"); 
    }
    else if(input==2)
    {
        printf("programma non ancora sviluppato");
    }
    else 
    {
        printf("input errato avvia autodistruzione");
    }

    return 0;
}