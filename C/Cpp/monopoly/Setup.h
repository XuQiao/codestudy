#include <vector>
#include <string>
#include "chesscell.h"
#include "chessland.h"
#include "chessboard.h"
#include "player.h"

const int IniPlayer = 4;
const int IniMoney = 5000;
const int nCell = 40;
struct conflands{
    std::string s;
    int lp;
    int hp;
    std::vector<int> hr;
    int color;
    int mg;
    int pos;
};

//Setup for players
const std::string pnames[] = {"A","B","C","D","E","F","G","H","I","J"};
const float psafeper[] =  {0.9, 0.3, 1.0, 0.5, 0.95, 0.8, 0.2, 0.3, 0.1};

//Setup for cells
const conflands alllands[] = {
       {"MEDITERRRANEAN AVENUE", 60, 50, {2, 10, 30, 90, 160, 250}, 0, 30, 1},
       {"BALTIC AVENUE", 60, 50, {4, 20, 60, 180, 320, 450}, 0, 30, 3},
       {"Oriental AVENUE", 100, 50, {6, 30, 90, 270, 400, 550}, 1, 50, 6},
       {"VERMONT AVENUE", 100, 50, {6, 30, 90, 270, 400, 550}, 1, 50, 8},
       {"CONNECTICUT AVENUE", 120, 50, {8, 40, 100, 300, 450, 600}, 1, 60, 9},
       {"ST. CHARLES PLACE", 140, 100, {10, 50, 150, 450, 620, 750}, 2, 70, 11},
       {"STATES AVENUE", 140, 100, {10, 50, 150, 450, 620, 750}, 2, 70, 13},
       {"VIRGINIA AVENUE", 160, 100, {12, 60, 180, 500, 700, 900}, 2, 80, 14},
       {"ST. JAMES PLACE", 180, 100, {14, 70, 200, 550, 750, 950}, 3, 90, 16},
       {"TENNESSEE AVENUE", 180, 100, {14, 70, 200, 550, 750, 950}, 3, 90, 18},
       {"NEW YORK AVENUE", 200, 100, {16, 80, 220, 600, 800, 1000}, 3, 100, 19},
       {"KENTUCKY AVENUE", 220, 150, {18, 90, 250, 700, 870, 1050}, 4, 110, 21},
       {"INDIANA AVENUE", 220, 150, {18, 90, 250, 700, 870, 1050}, 4, 110, 23},
       {"ILLINOIS AVENUE", 240, 150, {20, 100, 300, 750, 926, 1100}, 4, 120, 24},
       {"ATLANTIC AVENUE", 260, 150, {22, 110, 330, 800, 975, 1150}, 5, 130, 26},
       {"VENTNOR AVENUE", 260, 150, {22, 110, 330, 800, 975, 1150}, 5, 130, 27},
       {"MARVIN GARDENS", 280, 150, {24, 120, 360, 850, 1025, 1200}, 5, 140, 29},
       {"PACIFIC AVENUE", 300, 200, {26, 130, 390, 900, 1100, 1275}, 6, 150, 31},
       {"NORTH CAROLINA AVENUE", 300, 200, {26, 130, 390, 900, 1100, 1275}, 6, 150, 32},
       {"PENNSYLVANIA AVENUE", 320, 200, {28, 150, 450, 1000, 1200, 1400}, 6, 160, 34},
       {"PARK PLACE", 350, 200, {35, 175, 500, 1100, 1300, 1500}, 7, 175, 37},
       {"BOARDWAY", 400, 200, {50, 200, 600, 1400, 1700, 2000}, 7, 200, 39}
};

const conflands allrr[] = {
       {"PENNSYLVANIA RAILROAD", 200, 0, {25, 50, 100, 200}, -1, 100, 5},
       {"B & O RAILROAD", 200, 0, {25, 50, 100, 200}, -1, 100, 15},
       {"SHORT LINE", 200, 0, {25, 50, 100, 200}, -1, 100, 25},
       {"READING RAILROAD", 200, 0, {25, 50, 100, 200}, -1, 100, 35}
};

const conflands allut[] = {
       {"ELECTRIC COMPANY", 150, 0, {0}, -1, 75, 12},
       {"WATER WORKS", 150, 0, {0}, -1, 75, 28}
};

std::vector<chess_land*> prepare(const conflands alllands[], const int nlands, const int type){
    std::vector<chess_land*> chesslands;
    for(int iland = 0; iland < nlands; iland ++){
        chess_land *tmp = new chess_land();
        tmp->set_cellname(alllands[iland].s);
        tmp->set_state(-1);
        tmp->set_type(type);
        tmp->set_pos(alllands[iland].pos);
        tmp->set_landprice(alllands[iland].lp);
        tmp->set_houseprice(alllands[iland].hp);
        tmp->set_houserent(alllands[iland].hr);
        tmp->set_morgage(alllands[iland].mg);
        tmp->set_color(alllands[iland].color);
        chesslands.push_back(tmp);
    }
    return chesslands;
}

chess_board* Initialize(){
    int nlands = sizeof(alllands)/sizeof(alllands[0]);
    std::vector<chess_land*> chesslands = prepare(alllands, nlands, 0);
    int nrr = sizeof(allrr)/sizeof(allrr[0]);
    std::vector<chess_land*> chessrr = prepare(allrr, nrr, 1);
    int nut = sizeof(allut)/sizeof(allut[0]);
    std::vector<chess_land*> chessut = prepare(allut, nut, 2);
    chesslands.insert( chesslands.end(), chessrr.begin(), chessrr.end() );
    chesslands.insert( chesslands.end(), chessut.begin(), chessut.end() );
    
    std::vector<player*> players;
    for(int iplayer = 0;iplayer< IniPlayer; iplayer++){
        player *p = new player();
        p->set_name(pnames[iplayer]);
        p->set_safeper(psafeper[iplayer]);
        p->set_money(IniMoney);
        p->set_pos(0);
        p->set_jailstate(1);
        p->set_nland(0);
        p->set_nrr(0);
        p->set_nmgg(0);
        p->set_nhouse(0);
        p->set_nhotel(0);
        players.push_back(p);
    }
    
    chess_board* cb = new chess_board(players, chesslands, nCell);
    return cb;
}
