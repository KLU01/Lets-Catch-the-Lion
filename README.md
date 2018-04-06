# Lets Catch the Lion (elementary subset of Japanese Chess)

## Pieces
1. Lion
    - Can move in all directions, one step
      - north, south, east, west, northeast, northwest, southeast, southwest
2. Giraffe
    - Can move in a straight line, one step
      - north, south, east, west
3. Elephant
    - Can move in a diagonal, one step
      - northeast, northwest, southeast, southwest
4. Chick
    - Can move only forward, one step
      - north
5. Hen (not on the board until Chick moves to opponent's base)
    - Can move in all directions except southeast and southwest, one step
      - north, south, east, west, northeast, northwest

## Rules of the Game
1. 4 x 3 game
 -       | G | L | E | <-- Base
 -       |   | C |   |
 -       |   | C |   |
 -       | E | L | G | <-- Base
2. Checkmate the lion or eat the lion
3. A chick can become a hen once it reacher the opponent's base
4. Any of the opponents pieces that you have eaten can be resurrected to become your own. 
   You can place the piece wherever you wnt on the board as long as there is no other piece there. 
   This is considered one move.
 
## Steps 
- [ ] Develop a strategy-static evaluation function
- [ ] Create a minimax algorithm
- [ ] Should run in Man-Machine mode
 
 ## License

  Copyright [2018] [Kelly Lu]

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

