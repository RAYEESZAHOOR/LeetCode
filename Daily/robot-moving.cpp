// 874. Walking Robot Simulation
// Medium
// Topics
// Companies
// A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

// -2: Turn left 90 degrees.
// -1: Turn right 90 degrees.
// 1 <= k <= 9: Move forward k units, one unit at a time.
// Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

// Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

// Note:

// North means +Y direction.
// East means +X direction.
// South means -Y direction.
// West means -X direction.
// There can be obstacle in [0,0].

class Solution {
private:
    string solve(string dir, int val){
        if(val == -1){ // turn right
            if(dir == "+y"){ dir = "+x"; }
            else if(dir == "+x"){ dir = "-y"; }
            else if(dir == "-y"){ dir = "-x"; }
            else if(dir == "-x"){ dir = "+y"; }
        } else if(val == -2){ // turn left
            if(dir == "+y"){ dir = "-x"; }
            else if(dir == "-x"){ dir = "-y"; }
            else if(dir == "-y"){ dir = "+x"; }
            else if(dir == "+x"){ dir = "+y"; }
        }

        return dir;
    }

public:
    int robotSim(vector<int>& c, vector<vector<int>>& obs) {
        int mx = 0;
        int x = 0, y = 0;
        string dir = "+y"; // initial direction

        set<pair<int, int>> um;
        for(auto &val : obs){
            um.insert({val[0], val[1]});
        }

        for(auto &val : c){
            if(val == -1 || val == -2){
                dir = solve(dir, val);
                continue;
            }

            if(dir == "+y"){
                for(int i = 0; i < val; i++){
                    if(um.find({x, y + 1}) != um.end()){
                        break;
                    }
                    y++;
                }
            } else if(dir == "-y"){
                for(int i = 0; i < val; i++){
                    if(um.find({x, y - 1}) != um.end()){
                        break;
                    }
                    y--;
                }
            } else if(dir == "+x"){
                for(int i = 0; i < val; i++){
                    if(um.find({x + 1, y}) != um.end()){
                        break;
                    }
                    x++;
                }
            } else if(dir == "-x"){
                for(int i = 0; i < val; i++){
                    if(um.find({x - 1, y}) != um.end()){
                        break;
                    }
                    x--;
                }
            }
            mx = max(mx, x*x + y*y);
        }

        return mx;
    }
};