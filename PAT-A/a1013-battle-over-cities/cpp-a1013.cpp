/*
    @name     : a1013
    @source   : https://www.cnblogs.com/57one/p/11917581.html
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int G[1000][1000];
bool visit[1000] = { 0 };
int N, M, K;
void dfs(int v)
{
    visit[v] = true;
    for (int i = 1; i <=N; i++)
    {
        if (!visit[i] && G[v][i])
            dfs(i);
    }
}
int main()
{

    cin >> N >> M >> K;
    int v1, v2;
    int v;
    int count = 0;
    for (int i = 0; i < M; i++)
    {
        cin >> v1 >> v2;
        G[v1][v2] = G[v2][v1] = 1;
    }
    for (int i = 0; i < K; i++)
    {
        fill(visit, visit + 1000, false);
        count = 0;
        cin >> v;
        visit[v] = true;
        for (int i = 1; i <=N; i++)
        {
            if (!visit[i])
            {
                dfs(i);
                count++;
            }
        }
        cout << count-1<<endl;
    }
}