//
//  main.c
//  GvsR
//
//  Created by Li Chen on 1/19/14.
//  Copyright (c) 2014 Li Chen. All rights reserved.
//
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

//define function f(r)
//===================================

double f(double x)
{
    double fofr, a1=2.6, a2=5;
    fofr=exp(-pow(a1/x,a2));
    return fofr;
}
//======================================

void main()
{
    
    
     int N=32, M=32, Nbin=60;
     double d=1.5;
     double R[M][N][3];
    
    FILE *gofr=NULL;
    FILE *p1ofr=NULL;
    
    
     // the initial configuration
    //===================================
    int H=0;
    for(int i=0; i<2; i++){
        for(int j=0; j<2; j++){
            for(int k=0; k<2; k++){
                R[0][H][0]=((double)i)*d;
                R[0][H][1]=((double)j)*d;
                R[0][H][2]=((double)k)*d;
               // printf("%f %f %f\n",R[0][H][0],R[0][H][1],R[0][H][2]);
                H++;
                
            }
        }
    }
    for(int i=0; i<2; i++){
        for(int j=0; j<2; j++){
            for(int k=0; k<2; k++){
                R[0][H][0]=(0.5+((double)i))*d;
                R[0][H][1]=(0.5+((double)j))*d;
                R[0][H][2]=((double)k)*d;
                //printf("%f %f %f\n",R[0][H][0],R[0][H][1],R[0][H][2]);
                H++;
                
            }
        }
    }
    for(int i=0; i<2; i++){
        for(int j=0; j<2; j++){
            for(int k=0; k<2; k++){
                R[0][H][0]=((double)i)*d;
                R[0][H][1]=(0.5+((double)j))*d;
                R[0][H][2]=(0.5+((double)k))*d;
                //printf("%f %f %f\n",R[0][H][0],R[0][H][1],R[0][H][2]);
                H++;
                
            }
        }
    }
    for(int i=0; i<2; i++){
        for(int j=0; j<2; j++){
            for(int k=0; k<2; k++){
                R[0][H][0]=0.5+(double)i;
                R[0][H][1]=(double)j;
                R[0][H][2]=0.5+(double)k;
              //  printf("%f %f %f\n",R[0][H][0],R[0][H][1],R[0][H][2]);
                H++;
                
            }
        }
    }
    printf("The fcc initial configuration\n");
    

    //get the distance between two particles
    //====================================
    
    double rij[M][N][N];
    double dr=2*d*sqrt(3)/((double)Nbin);
    int defBin;
  
    
  
    for(int j=0; j<N; j++){
        for(int i=0;i<N;i++){
            
           rij[0][j][i]=sqrt(pow(R[0][j][0]-R[0][i][0],2)+pow(R[0][j][1]-R[0][i][1],2)+pow(R[0][j][2]-R[0][i][2],2));
            
        }
    }
    
    
    printf("get the distance of initial configuration");
    
    //get the number of partibles in different distance of the initial configuration
    
    double G[Nbin];  // the number of particle at different distance
    
    double Fofone[Nbin][M/N];
    
    for(int i=0; i<Nbin; i++) G[i]=0;
    
    for (int i=0;i<Nbin;i++){
        for(int z=0; z<M/N; z++) {
            
        Fofone[i][z]=0;
        
        }
    }
    
    
    for(int j=1;j<N;j++){
        for(int i=0;i<j;i++){
            defBin=(int)(rij[0][j][i]/dr);
            G[defBin]=G[defBin]+1.0;
        }
    }
    
    
    //Monte Carlo method
    //===================================
    
    
     for(int i=0; i<M; ){
     for(int j=0; j<N; j++){
        
    //get try configuration
         
         double s0,s[3],t,x[3];
         
         
         srand((unsigned)time(NULL));
         s0=(double)rand()/RAND_MAX;
         
         for (int k=0;k<3;k++){
             s[k]=((double)rand()/RAND_MAX)*2-1;
             t=R[i][j][k]+s[k]*d;
             if (t<2*d && t>0)
                 x[k]=t;
             else
                 if(t>=2*d)
                     x[k]=t-2*d;
                 else
                     x[k]=t+2*d;
         }
         
         
        // get the probility of try configuration
    
         
         double rr[N], ri[N],fr=1,fi=1;
         for(int h=0;h<N;h++){
             if(h!=j){
               rr[h]=sqrt(pow(x[0]-R[i][h][0],2)+pow(x[1]-R[i][h][1],2)+pow(x[0]-R[i][h][2],2));
               ri[h]=sqrt(pow(R[i][j][0]-R[i][h][0],2)+pow(R[i][j][1]-R[i][h][1],2)+pow(R[i][j][2]-R[i][h][0],2));
                 fr=fr*f(rr[h]);
                 fi=fi*f(ri[h]);
                  }
         }
         
         double Pnrt, Pnri, eta0, eta;
         Pnrt=fr*fr;
         Pnri=fi*fi;
         
         //compare the probility of try configuration and i configuration, get i+1 configuration
         
         srand((unsigned)time(NULL));
         eta0=(double)rand()/RAND_MAX;
         eta=(double)rand()/RAND_MAX;
         
         if(Pnrt>=Pnri||Pnrt/Pnri>eta){
             R[i+1][j][0]=x[0];
             R[i+1][j][1]=x[1];
             R[i+1][j][2]=x[2];
             for(int k=0; k<N; k++){
                 rij[i+1][j][k]=rij[i+1][k][j]=sqrt(pow(R[i+1][j][0]-R[i][k][0],2)+pow(R[i+1][j][1]-R[i][k][1],2)+pow(R[i+1][j][2]-R[i][k][2],2)); //since only particle j, get the distance between the moved particle and others.
             }
         }
         else{
             R[i+1][j][0]=R[i][j][0];
             R[i+1][j][1]=R[i][j][1];
             R[i+1][j][2]=R[i][j][2];
             for(int k=0; k<N; k++){
                 rij[i+1][j][k]=rij[i+1][k][j]=sqrt(pow(R[i+1][j][0]-R[i][k][0],2)+pow(R[i+1][j][1]-R[i][k][1],2)+pow(R[i+1][j][2]-R[i][k][2],2));
             }
         }
         
         for(int n=0;n<N; n++){
                 if (n!=j){
                 for(int l=0; l<3; l++){
                     R[i+1][n][l]=R[i][n][l];   //in i+1 configuration the location of particle n!=j is same with the location in i configuration
                  }
                }
         }
         
         
         for(int p=0; p<N; p++){
                 for(int q=0;q<N;q++){
                     if(p!=j&&q!=j)
                     rij[i+1][p][q]=rij[i][p][q];  // the distances of particle p and q !=j in i+1 configuration are same with that in i configuration
                 }
             }
         
        //get the number of particles in different distance
         int defBin;
         for(int p=1;p<N;p++){
             for(int q=0;q<p;q++){
                 defBin=(int)(rij[i+1][p][q]/dr);
                 G[defBin]=G[defBin]+1.0;
             }
         }

         
         i++;
         
     }
   //calculate the one particle density
   //=============================================================
         
         
        
         
         for(int u=0; u<N; u++){
             for(int v=0; v<N; v++){
                 
                 int findbin=(int)(rij[i][u][v]/dr);
                 double multi=1;
                 for(int w=0; w<N; w++){
                     if(w!=v) multi=multi*(f(rij[i][u][w])/f(rij[i][v][w]));
                 }
                                           
                 Fofone[findbin][i/N-1]=Fofone[findbin][i/N-1]+multi;
                                           
             }
         }
        
         
         
         
   //===============================================================
     }
    
    
    
    //get g(r),get the results
    //=============================================================
    double density=2.2e22;
    double Goverg=N*density*4*3.1415926*dr*dr*dr/2;
    double g[Nbin], distance[Nbin];
    for(int i=1;i<Nbin; i++){
        g[i]=G[i]/((double)(i*i))/Goverg/((double)M);
        distance[i]=((double)i)*dr;
        fprintf(gofr,"%f %f\n",distance[i],g[i]);
        
    }
    //=========================================================
    
   printf("Data of one particle density\n");
    
   //get one particle density
//===================================================================
    double onedensity[Nbin];
    double PoverF=1/((double)M*4*3.1415926*dr*dr*dr);
    
    for(int i=0;i<Nbin;i++) onedensity[i]=0;
    
    for(int i=0;i<Nbin;i++){
        for(int j=0; j<M/N; j++){
            onedensity[i]=onedensity[i]+PoverF*Fofone[i][j];
    }
        
        fprintf(p1ofr, "%f %f\n", distance[i],onedensity[i]);
 
        
    }
 //=====================================================================
 
   fclose(gofr);
    fclose(p1ofr);
/**/    
    
    
}

