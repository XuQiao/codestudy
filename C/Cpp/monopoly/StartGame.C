#include "Setup.h"
#include <iostream>

int main(){
    //Initialization
    srand (time(NULL));
    
    chess_board *cb = Initialize();
    int nplayer = cb->get_players().size();

    //Game
    while(nplayer > 1){
        cb->set_nmove(cb->get_nmove()+1);
        std::cout<< cb->get_nmove() << " round move" << std::endl;
    for(int iplayer = 0;iplayer < nplayer; iplayer++){
        player *p = cb->get_players()[iplayer];
        cb->set_player(p);  //iplayer turn
        std::cout << "Player " << p->get_name() << " money : " << p->get_money() << std::endl;
        cb->demorgage(); //Any morgage want to get back
        //std::cout << " His safe percentage is " << p->get_safeper() << std::endl;
        int rd = p->roll_dice(); //Throw dice
        int pos = p->get_pos() + rd; //move
        pos = pos % nCell;
        cb->set_pos(pos); // to a position
        std::cout<< "Throw " << rd << " Get Position " << pos << std::endl;
        cb->boardaction(); //take some action
        if(nplayer != cb->get_players().size()) { //One player left
            nplayer --;
            iplayer --;
        } 
        std::cout<<std::endl;   
    }
}
}
