#ifndef MYOTHELLOAI_HPP
#define MYOTHELLOAI_HPP

#include "OthelloAI.hpp"
#include "OthelloGameState.hpp"
#include<vector>
#include<iostream>

namespace chenjunz
{
    class MyOthelloAI: public OthelloAI
    {
    public:
        MyOthelloAI();

        virtual std::pair<int,int> chooseMove(const OthelloGameState& state);

        int search(OthelloGameState& s, int depth,std::string turn);

        bool checkTurn(OthelloGameState& s, std::string turn);

        std::vector<std::pair<int,int>> validMove(const OthelloGameState& state);

    };
}

#endif //MYOTHELLOAI
