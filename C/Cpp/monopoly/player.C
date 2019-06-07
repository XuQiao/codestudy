#include "chessland.h"
#include "player.h"
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

void player::build(chess_land *cl){
    if(!cl) return;
    int lp = cl->get_landprice();
    int hp = cl->get_houseprice();
    int state = cl->get_state();
    int type = cl->get_type();
    std::cout<< "pos: " << pos << " name: " << cl->get_cellname() << " landprice: " << lp << " houseprice: "<< hp << " state: "<< state<<std::endl;
    if(state == -2) return;
    player *p = cl->get_owned();
    if(!p && state == -1){ //not owned
        if(money * safeper >= lp){
            money -= lp;
            cl->set_state(0);
            cl->set_owned(this);
            nland = nland + 1;
            if(type == 1)
                nrr = nrr + 1;
        }
    }
    else if(p == this && type == 0 && state >= 0 && state < 5){ //self owned
        if(money * safeper >= hp){
            money -= hp;
            cl->set_state(state+1);
            cl->set_owned(this);
            if(state == 5)
                nhotel = nhotel + 1;
                nhouse = nhouse + 1;
        }
    }
    else return;
}

void player::morgage(chess_land *cl){
    if(!cl) return;
    int state = cl->get_state();
    int mgg = cl->get_morgage();
    int hp = cl->get_houseprice();
    int type = cl->get_type();
    if(state == -2) return;
    player *p = cl->get_owned();
    if(p == this && state >= 0){
        std::cout << "Morgage " << cl->get_cellname() << " for "<< mgg << ", house built " << state << std::endl;
        money = money + mgg + (int)hp/2 * state;
        cl->set_state(-2);
        nland = nland - 1;
        nmgg = nmgg + 1;
        if(type == 1)
           nrr = nrr - 1;
    }
    else return;
}

void player::demorgage(chess_land *cl){
    if(!cl) return;
    int state = cl->get_state();
    int mgg = cl->get_morgage();
    int type = cl->get_type();
    if(state != -2) return;
    player *p = cl->get_owned();
    if(p == this && money * (1 - safeper) >= mgg * 1.1){
        std::cout << "DeMorgage " << cl->get_cellname() << " for "<< mgg * 1.1 << std::endl;
        money = money - mgg * 1.1;
        cl->set_state(0);
        nland = nland + 1;
        nmgg = nmgg - 1;
        if(type == 1)
           nrr = nrr + 1;
    }
    else return;
}

void player::payrent(std::vector<chess_land*> chesslands, chess_land *cl){
    if(!cl) return;
    int state = cl->get_state();
    int type = cl->get_type();
    int color = cl->get_color();
    player *p = cl->get_owned();
    if(!p || p == this) return;
    std::vector<int> houserent = cl->get_houserent();
    if(state < 0) return;
    int hr = houserent[state];
    if(state == 0){
    int iland = 0;
    for(iland = 0; iland < chesslands.size(); iland ++){
        if(color == chesslands[iland]->get_color() && p != chesslands[iland]->get_owned())  break;
    }
    if(iland == chesslands.size())
    hr = hr * 2;
    }
    if(type == 1){
        hr = houserent[p->get_nrr()-1];
    }
    if(type == 2){
        hr = roll_dice() * 4;
    }
    std::cout<< "state = " << state << ", "<< hr << " rent paid to " << p->get_name() <<std::endl;
    money -= hr;
    p->set_money(p->get_money()+hr);    
}

int player::roll_dice(){
    int dice1 = rand() % 6 + 1;
    int dice2 = rand() % 6 + 1;
    if(!jailstate)
    return dice1 == dice2;
    else
    return dice1 + dice2;
}

