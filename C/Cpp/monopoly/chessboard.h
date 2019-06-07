#ifndef _CHESS_BOARD_H
#define _CHESS_BOARD_H
#include  "chessland.h"
#include  "player.h"
#include  <vector>
#include  <string>

class player;
class chess_land;
//cehssland
class chess_board{
    public:
    chess_board(){};
    chess_board(std::vector<player*> _players, std::vector<chess_land*> _chesslands, int _nCell);
    ~chess_board(){};
    private:
    int nCell;
    int pos;
    std::vector<player*> players;
    std::vector<chess_land*> chesslands;
    player *p;
    int nmove;

    public:
    void set_player(player *_p){ p = _p;}
    void set_pos(int _pos){ pos = _pos;}
    void set_nmove(int _nmove){ nmove = _nmove;}

    player* get_player(){ return p;}
    int get_pos(){ return pos;}
    int get_nmove(){ return nmove;}

    std::vector<player*> get_players(){ return players;}
    std::vector<chess_land*> get_chesslands(){ return chesslands;}

    chess_land* postoland(int ipos);
    void boardaction();
    void directpay();
    void jail();
    int chest();
    int quest();
    void action();
    void release();
    void print();
    void morgage();
    void demorgage();

};

#endif
