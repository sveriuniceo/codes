int main() {

int i,sintoma,soma,mulher,houve,houvesintoma,nao,s[3][10];

    sintoma=0;
    soma=0;
    i=0;
    s[0][9]=0,s[1][9]=0,s[2][9]=0;
    s[0][3]=0,s[1][3]=0,s[2][3]=0;

float idoso=0,emergencia=0,idosoemergencia=0,mdsintoma=0,idadem=0,dias=0;

 for(i=0;i<3;i++){


printf("\ndigite os primeiros 3 digitos do CPF: \n");
scanf("%d",&s[i]);

printf("\ndigite sua idade: \n");
scanf("%d",&s[i][8]);
   if (s[i][8]>=65){
       idoso=1;
printf(" idoso\n",s[i][8]);}
   else {idoso=0;}

printf("digite 1 MASCULINO ou 2 FEMININO.\n");
scanf("%d",&s[i][1]);
   if (s[i][1]<=1){
printf("masculino\n");}
   else{
printf("feminino\n");}

printf("digite 1 se houve sintomas de covid ou 2 se não houve sintomas\n");
scanf("%d",&s[i][2]);
   if (s[i][2]<=1){
      sintoma++;
      houve=1;

printf("quantos dias de sintoma?\n");
scanf("%d",&s[i][3]);

printf("precisou procurar ajuda medica? (1-NÃO 2-CONSULTA 3-EMERGÊNCIA)\n");
scanf("%d",&s[i][4]);
   if(s[i][4]>=3){ emergencia=1; }
   else { emergencia=0;}
   if(s[i][4]<=1){ nao=1;}
   else{ nao=0;}
   if (emergencia+idoso>=2){
       idosoemergencia++;}

printf("Realizou algum teste de covid? (digite 1-SIM ou 2-NÃO)\n");
scanf("%d",&s[i][5]);
    if(s[i][5]<=1){

printf("Qual foi o resultado? (digite 1-POSITIVO ou 2-NEGATIVO)\n");
scanf("%d",&s[i][6]);
    if (s[i][6]<=1){

printf("positivo\n");}
   else{  if (s[i][2]<=1){  
   if (s[i][1]>=2) {mulher++, s[i][9]=s[i][8];
printf("%d\n",s[i][9]);                  } }
printf("negativo\n");}}}

   if (s[i][2]>=2){
      soma++;
      houve=0;
printf("assintomatico\n");}
    if (nao+houve>=2){houvesintoma++;}}
{
idadem=(s[0][9]+s[1][9]+s[2][9])/mulher;
dias=(s[0][3]+s[1][3]+s[2][3]);
mdsintoma=dias/sintoma;

                 
                 printf("\nRELATORIO FINAL\n");

printf("Número de participantes: 3");

printf("\nPessoas assintomaticas:%d\n",soma);

printf("Porcentual idoso que procurou emergência:  %.1f% \n",(idosoemergencia/3)*100);

printf("Pessoas com sintomas %d\n",sintoma);

printf("Média de dias de sintoma: %.2f\n", mdsintoma);
   
printf("Pessoas com sintomas e não precisaram de ajuda médica: %d\n",houvesintoma);
}
printf("A média de idade de mulheres que tiveram sintomas e o teste negativo: %.1f\n", idadem);

 

return 0;

 }