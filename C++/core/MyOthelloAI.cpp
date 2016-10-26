
#include "MyOthelloAI.hpp"

#include <ics46/factory/DynamicFactory.hpp>

#include<iostream>

chenjunz::MyOthelloAI::MyOthelloAI()
{
}

std::pair<int,int> chenjunz::MyOthelloAI::chooseMove(const OthelloGameState& state)
{
    std::vector<std::pair<int,int>> validMoves = validMove(state);
    int index = 0;
    int depth = 5;
    std::vector<int> eval;
    std::string turn;

    for(int i = 0; i<validMoves.size(); i++)
    {
        std::unique_ptr<OthelloGameState> state_ptr = state.clone();
        state_ptr->makeMove(validMoves[i].first,validMoves[i].second);
        if (state.isBlackTurn()) 
        {
            turn = "black";
        }
        else 
        {
            turn = "white";
        }
        eval.push_back(search(*state_ptr,depth,turn));
    }
    for(int i = 0; i<eval.size(); i++)
    {
        if (eval[index]<eval[i])
        {
            index = i;
        }
    }
    return validMoves[index];
}


int chenjunz::MyOthelloAI::search(OthelloGameState& s, int depth, std::string turn)
{
    if (depth == 0)
    {
        if (turn == "black"){return (s.blackScore()-s.whiteScore());}
        else {return (s.whiteScore()-s.blackScore());}
    }
    else
    {
        std::vector<std::pair<int,int>> validMoves = validMove(s);
        std::unique_ptr<OthelloGameState> s_ptr;
        int eval;
        
        
        if(checkTurn(s,turn))
        {
            int bestEval = -999;
            for(unsigned int i = 0; i < validMoves.size(); i++)
            {
                s_ptr = s.clone();
                s_ptr->makeMove(validMoves[i].first,validMoves[i].second);
                eval = search(*s_ptr,depth-1,turn);

                if (eval >= bestEval) {bestEval = eval;}
            }
        
        }
        else
        {
            int bestEval = 999;
            for(unsigned int i = 0; i < validMoves.size(); i++)
            {
                s_ptr = s.clone();
                s_ptr->makeMove(validMoves[i].first,validMoves[i].second);
                eval = search(*s_ptr,depth-1,turn);
                
                if (eval <= bestEval) {bestEval = eval;}
                                                                                                    }
        }

        return eval;
    }
}

bool chenjunz::MyOthelloAI::checkTurn(OthelloGameState& s,std::string turn)
{
    if (turn == "black")
    {
        if (s.isBlackTurn()) {return true;}
        else {return false;}
    }
    else
    {
        if (s.isWhiteTurn()) {return true;}
        else {return false;}
    }
}

std::vector<std::pair<int,int>> chenjunz::MyOthelloAI::validMove(const OthelloGameState& state)
{
    std::vector<std::pair<int,int>> validMove;
    int width = state.board().width();
    int height = state.board().height();
    
    for(int x = 0; x<width; x++)
    {
        for(int y = 0; y<height; y++)
        {
            if (state.isValidMove(x,y))
            {
                validMove.push_back(std::make_pair(x,y));
            }    
        }
    }
    return validMove;
}

ICS46_DYNAMIC_FACTORY_REGISTER(OthelloAI,chenjunz::MyOthelloAI,"My Othello AI(Required)");
