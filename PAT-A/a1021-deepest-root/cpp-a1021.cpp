/*
    @name     : a1021
    @accepted :
    @source   : https://zhuanlan.zhihu.com/p/137990346
*/

#include<cstdio>
#include<cstring>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

int deepest = 0, ans = 0;//每个顶点所能到达的最大深度、所有顶点的最大深度
set<int> output;//存储具有最大深度的顶点
vector<int> adj[10001];//邻接表数组
bool marked[10001] = {0};//标记顶点是否到达过
//用于计算连通分量个数的dfs
void dfs(int v) {
    marked[v] = true;
    for(int w = 0; w < adj[v].size(); w++)
        if(!marked[adj[v][w]])    dfs(adj[v][w]);
}
//用于计算每个顶点能到达的最大深度的dfs
void dfs(int v, int depth) {//第一个参数为当前顶点，第二个参数为当前深度
    marked[v] = true;
    deepest = max(deepest, depth);//更新能到达的最大深度
    for(int w = 0; w < adj[v].size(); w++)
        if(!marked[adj[v][w]])    dfs(adj[v][w], depth + 1);
}

int main() {
    int n, cc = 0;//顶点数、连通分量个数
    scanf("%d", &n);
    //构造图
    for(int i = 0; i < n - 1; i++) {
        int v, w;
        scanf("%d %d", &v, &w);
        adj[v].push_back(w);
        adj[w].push_back(v);
    }
    //第一遍dfs，计算连通分量的个数
    for(int s = 1; s <= n; s++) {
        if(!marked[s]) {
            dfs(s);
            cc++;
        }
    }
    if(cc == 1) { //连通分量个数为1，说明该图是一棵树，无环连通，则按要求输出结果
        for(int s = 1; s <= n; s++) { //对每个顶点都进行dfs计算能到达的最大深度
            memset(marked, 0, sizeof(marked));
            deepest = 0;//初始化每个顶点所能到达的最大深度为0
            dfs(s, 1);//相当于树的dfs
            //将具有最大深度的顶点存储于set中
            if(deepest > ans) {
                ans = deepest;
                output.clear();
                output.insert(s);
            } else if(deepest == ans)
                output.insert(s);
        }
        //set自动升序，自动去重
        for(set<int>::iterator it = output.begin(); it != output.end(); it++)
            printf("%d\n", *it);
    }
    //连通分量个数不为1，输出连通分量的个数
    else    printf("Error: %d components\n", cc);
    return 0;
}
