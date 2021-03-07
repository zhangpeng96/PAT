#include <cstdio>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;
const int inf = 0x7fffffff;
int lineNum, queryNum;

struct node {
    int stationId;  //站号
    vector<int> nextStations;   //直接相连的站
    unordered_set<int> belongedLines;   //属于的线路
} table[10000];

unordered_map<int, int> line[101];  //每条线路号指向一个map，每个map保存这条线路的全部站号对
int getLineId(int s1, int s2) { //返回相邻两站属于哪条线路
    if (s1 == -1 || s2 == -1)
        return -1;
    for (auto it = table[s1].belongedLines.begin(); it != table[s1].belongedLines.end(); it++) {
        if (line[*it][s1] == s2 || line[*it][s2] == s1)
            return *it;
    }
}

bool visited[10000];
vector<int> route;
int minStationCount, minTransferCount, destination;

void dfs(int cur, int pre, int preLine, int transferCount, vector<int> curRoute) {
    curRoute.push_back(cur);
    visited[cur] = true;
    if (curRoute.size() > minStationCount) {    //剪枝
        curRoute.pop_back();
        visited[cur] = false;
        return;
    }
    int curLine = getLineId(pre, cur);
    if (curLine != preLine)
        transferCount++;
    if (cur == destination) {
        if (curRoute.size() < minStationCount ||
            (curRoute.size() == minStationCount && transferCount < minTransferCount)) {
            route = curRoute;
            minStationCount = curRoute.size();
            minTransferCount = transferCount;
        }
        curRoute.pop_back();
        visited[cur] = false;
        return;
    }
    for (int i = 0; i < table[cur].nextStations.size(); i++) {
        if (!visited[table[cur].nextStations[i]]) {
            dfs(table[cur].nextStations[i], cur, curLine, transferCount, curRoute);
        }
    }
    visited[cur] = false;
    curRoute.pop_back();
}

int main() {
    scanf("%d", &lineNum);
    for (int i = 0; i < lineNum; i++) {
        int stopNum;
        scanf("%d", &stopNum);
        int pre = -1;
        for (int j = 0; j < stopNum; j++) {
            int id;
            scanf("%d", &id);
            table[id].stationId = id;
            table[id].belongedLines.insert(i + 1);
            if (pre != -1) {
                table[id].nextStations.push_back(pre);
                table[pre].nextStations.push_back(id);
                line[i + 1][pre] = id;
            }
            pre = id;
        }
    }
    scanf("%d", &queryNum);
    for (int i = 0; i < queryNum; i++) {
        int source, dest;
        scanf("%d %d", &source, &dest);
        route.clear();
        minStationCount = inf, minTransferCount = inf, destination = dest;
        vector<int> temp;
        dfs(source, -1, -1, 0, temp);
        printf("%d\n", route.size() - 1);
        int start = 0, end = 1;
        while (end < route.size()) {
            int curLine = getLineId(route[start], route[end]);
            while (end + 1 < route.size() && getLineId(route[end], route[end + 1]) == curLine) {
                end++;
            }
            printf("Take Line#%d from %04d to %04d.\n", curLine, route[start], route[end]);
            start = end;
            end = start + 1;
        }
    }
}
