using namespace std;
/*
rule1 if last is 'I', we can add "U'
rule2 if Mx, we can change to Mxx
rule3 III can be replaced with U
rule4 UU can be removed
*/
void crule1(char *s){
    if(*(s+len) == 'I')
        *(s+len+1) = 'U';
}

void crule2(char *s){
    char *r;
    if(*s == 'M')
        r = s+1;
    s+len+1 = r;
}

void crule3(char *s){
    int i = 0;
    char *r;
    while(*(s+i) != ""){
        if(*(s+i) == "I" && *(s+i+1) == "I" && *(s+i+2) == "I")
            r = s+i+3;
        *(s+i) = 'U';
        s+i+1 = r;
        i++;
    }
}

void crule4(char *s){
    int i = 0;
    char *r;
    while(*(s+i)!=""){
        if(*(s+i)=="U" && *(s+i+1)=="U")
            r = s+i+2;
        s+i = r;
        i++;
    }
}

int main(){
int MAX_TRY=1000;
char *s = "MI";
cout<<crule1(s);
/*
    for(int i=0;i<MAX_TRY;i++){
        int rule = random(4);
        if(rule==1 && s)
    }       
*/
}
