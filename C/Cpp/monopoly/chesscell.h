#ifndef _CHESS_CELL_H
#define _CHESS_CELL_H
#include  <vector>
#include  <string>
#include  <iostream>

//each cel in the board, base class
class chess_cell{
    public:
    chess_cell(){};
    ~chess_cell(){};
    private:
    std::string cellname;
    int type;
    int pos;
    //type: 0: Nothing, 1: Normal, 2:Chest, 3: Quest, 4: Jail
    public:
    void set_pos(int _pos){ pos = _pos;}
    void set_type(int _type){ type = _type;}
    void set_cellname(std::string _cellname){ cellname = _cellname;}

    int get_type(){ return type;}
    int get_pos(){ return pos;}
    std::string get_cellname(){ return cellname;}
};

#endif
