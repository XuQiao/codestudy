#ifndef _CHESS_LAND_H
#define _CHESS_LAND_H
#include  "chesscell.h"
#include  "player.h"
#include  <vector>
#include  <string>

class player;
//cehssland
class chess_land : public chess_cell{
    public:
    chess_land(){};
    ~chess_land(){};
    private:
    //only valid for type 0 and 1
    int state;  //number of houses, -1: UnOwned, 0: with land, -2: Morgaged
    int landprice;
    int houseprice;
    int morgage;
    int color; //color set
    std::vector<int> houserent;
    player *p = NULL; // owned by player p

    public:
    void set_color(int _color){ color = _color;}
    void set_state(int _state){ state = _state;}
    void set_landprice(int _landprice){ landprice = _landprice;}
    void set_houseprice(int _houseprice){ houseprice = _houseprice;}
    void set_houserent(std::vector<int> _houserent){ houserent = _houserent;}
    void set_morgage(int _morgage){ morgage = _morgage;}
    void set_owned(player *_player){ p = _player;}

    int get_color(){ return color;}
    int get_state(){ return state;}
    int get_landprice(){ return landprice;}
    int get_houseprice(){ return houseprice;}
    std::vector<int> get_houserent(){ return houserent;}
    int get_morgage(){ return morgage;}
    player *get_owned(){ return p;}

};

#endif
