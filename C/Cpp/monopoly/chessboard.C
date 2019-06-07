#include <vector>
#include <string>
#include "chesscell.h"
#include "chessland.h"
#include "chessboard.h"
#include <algorithm>
#include "player.h"

chess_board::chess_board(std::vector<player*> _players, std::vector<chess_land*> _chesslands, int _nCell):
    players(_players),
    chesslands(_chesslands),
    p(NULL),
    nmove(0),
    nCell(_nCell){}

//Setup for Chest
int chess_board::chest(){
    int r = rand() % 16 + 1;
    int newpos = pos;
    std::cout<< "Get " << r << " th Chest card" << std::endl; 
    switch(r){
        case 1: case 2:
    p->set_money(p->get_money() - 50);
    std::cout<< " Lose 50 " << std::endl; 
    break;
        case 3:
    p->set_money(p->get_money() + 200);
    std::cout<< " Get 200 " << std::endl; 
    break;
        case 4:
    p->set_money(p->get_money() - p->get_nhouse() * 40 - p->get_nhotel() * 115);
    std::cout<< " house big repair " << std::endl; 
    break;
        case 5: case 10: case 11:
    p->set_money(p->get_money() + 100);
    std::cout<< " Get 100 " << std::endl; 
    break;
        case 6:
    p->set_money(p->get_money() - 100);
    std::cout<< " Lose 100 " << std::endl; 
    break;
        case 7:
    p->set_jailstate(p->get_jailstate() + 1);
    std::cout<< " jail free card " << std::endl; 
    break;
        case 8:
    p->set_money(p->get_money() + 10);
    std::cout<< " Get 10 " << std::endl; 
    break;
        case 9:
    pos == 30; jail();//jail case
    std::cout<< " Go to jail " << std::endl; 
    break;
        case 12:
    p->set_money(p->get_money() + 10 * (players.size() - 1)); //other - 10
        for(int iplayer = 0; iplayer < players.size(); iplayer ++ ){
            if(players[iplayer] != p)
            players[iplayer]->set_money(players[iplayer]->get_money() - 10);
        }
    std::cout<< " each player pay you 10 " << std::endl; 
    break;
        case 13:
    p->set_money(p->get_money() + 50);
    std::cout<< " Get 50 " << std::endl; 
    break;
        case 14:
    p->set_money(p->get_money() - 25);
    std::cout<< " Lose 25 " << std::endl; 
    break;
        case 15:
    p->set_money(p->get_money() + 20);
    std::cout<< " Get 25 " << std::endl; 
    break;
        case 16:
        newpos = 0;    
    p->set_money(p->get_money() + 200);
    std::cout<< " Advance to Go " << std::endl; 
    break;
    }
    return newpos;
}

//Setup for quest
int chess_board::quest(){
    int r = rand() % 16 + 1;
    int newpos = pos;
    std::cout<< "Get " << r << " th Quest card" << std::endl; 
    switch(r){
        case 1:
    if(pos > 11) p->set_money(p->get_money() + 200);
    newpos = 11;
    std::cout<< " Go to Pos 11 " << std::endl; 
    break;
        case 2:
    p->set_money(p->get_money() - p->get_nhouse() * 25 - p->get_nhotel() * 100);
    std::cout<< " house small repair " << std::endl; 
    break;
        case 3:
    pos == 30; jail();
    std::cout<< " Go to jail " << std::endl; 
    break;
        case 4:
    newpos = 39;
    std::cout<< " Go to Pos 39 " << std::endl; 
    break;
        case 5:
    newpos = pos - 3; if(pos < 3) newpos = pos + 37;
    std::cout<< " Go Back 3 spaces " << std::endl; 
    break;
        case 6:
    newpos = 0;
    p->set_money(p->get_money() + 200);
    std::cout<< " Advance to Go " << std::endl; 
    break;
        case 7:
    p->set_money(p->get_money() + 50);
    std::cout<< " Get 50 " << std::endl; 
    break;
        case 8:
    p->set_money(p->get_money() - 15);
    std::cout<< " Lose 15 " << std::endl; 
    break;
        case 9:
    if(pos > 5) p->set_money(p->get_money() + 200);
    newpos = 5; 
    std::cout<< " Go to Pos 5 " << std::endl; 
    break;
        case 10:
    if(pos >= 35 && pos < nCell){
        newpos = 5;  
        p->set_money(p->get_money() + 200);
    }
    else
    newpos = ((pos + 5) / 10) * 10 + 5;
    std::cout<< " Advance to nearest railroad " << std::endl; 
    break;
        case 11:
    p->set_money(p->get_money() + 100);
    std::cout<< " Get 100 " << std::endl; 
    break;
        case 12:
    newpos = (pos >= 12 && pos < 28) ? 28 : 12;
    std::cout<< " Go to Nearest utility " << std::endl; 
    break;
        case 13:
    p->set_jailstate(p->get_jailstate() + 1);
    std::cout<< " jail free card " << std::endl; 
    break;
        case 14:
    p->set_money(p->get_money() - 50 * (players.size() - 1)); //other + 50
        for(int iplayer = 0; iplayer < players.size(); iplayer ++ ){
            if(players[iplayer] != p)
            players[iplayer]->set_money(players[iplayer]->get_money() + 50);
        }
    std::cout<< " pay each player 50 " << std::endl; 
    break;
        case 15:
    if(pos > 24) p->set_money(p->get_money() + 200);
    newpos = 24;
    std::cout<< " Go to Pos 24 " << std::endl; 
    break;
        case 16:
    p->set_money(p->get_money() + 150);
    std::cout<< " Get 150 " << std::endl; 
    break;
    }
    return newpos;
}

void chess_board::directpay(){
    int money = p->get_money();
    if(pos == 4) p->set_money(money - 200); 
    if(pos == 38) p->set_money(money - 100); 
    return;
}

void chess_board::jail(){
    if(p->get_pos() != 30 && pos == 30 ){
        p->set_jailstate(p->get_jailstate()-1);
        p->set_pos(30);//jail case
        return;
    }
    else if(p->get_pos() == 30 && pos == 10 && !p->get_jailstate()){
        if(p->roll_dice()){
            pos = pos + p->roll_dice();
            boardaction();
        }
        p->set_pos(10);
        p->set_jailstate(p->get_jailstate()+1);
        return;
    }
    else return;
}

void chess_board::action(){
    p->build(postoland(pos));
    p->payrent(chesslands, postoland(pos));
}


chess_land* chess_board::postoland(int ipos){
    for(int iland = 0; iland < chesslands.size(); iland ++){
        if(ipos == chesslands[iland]->get_pos()) return chesslands[iland];
    }
    return NULL;
}

void chess_board::release(){
    for(int iland = 0; iland < chesslands.size(); iland ++){
        if(chesslands[iland]->get_owned() == p){
            chesslands[iland]->set_owned(NULL);
            chesslands[iland]->set_state(-1);
        }
    }
    return;
}

void chess_board::boardaction(){
    if(!p->get_jailstate()) pos = 10; 
    if(p->get_pos()>=pos && p->get_jailstate()) {
        std::cout << "passing go" << std::endl;
        p->set_money(p->get_money() + 200); 
    }
    if(pos == 0 || pos == 20);
    else if(pos == 4 || pos == 38) directpay();
    else if(pos == 7 || pos == 22 || pos == 36){
       int newpos = quest();
       if(newpos != pos){
       pos = newpos;
       action();
       }
    }
    else if(pos == 2 || pos == 17 || pos == 33){
       int newpos = chest();
       if(newpos != pos){
       pos = newpos;
       action();
       }
    }
    else if(pos == 10 || pos == 30) jail();
    else action();
    
    p->set_pos(pos);
    if(p->get_money()<0) morgage();
}

void chess_board::morgage(){
    int ipos = 0;
    while(p->get_money()<0 && ipos < nCell){
        p->morgage(postoland(ipos));
        ipos ++ ;
    }
    if(p->get_money()<0){
        release();
        std::cout<< p->get_name() << " BANKRUPTED! " << std::endl;
        players.erase(std::remove(players.begin(), players.end(), p), players.end());
    } 
}

void chess_board::demorgage(){
    int ipos = 0;
    while(ipos < nCell && p->get_money() >= 0){
        p->demorgage(postoland(ipos));
        ipos ++ ;
    }
} 

