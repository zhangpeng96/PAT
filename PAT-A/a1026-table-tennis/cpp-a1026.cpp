/*
    @name     : a1026
    @version  : 21.0308
    @source   : https://blog.csdn.net/qq_34451909/article/details/105389786
*/

#include <bits/stdc++.h>

using namespace std;

class Player {
public:
    Player() {};

    Player(int a, int b, bool c) : arrive_time(a), using_time(b), vip(c) {}

    int arrive_time;
    int using_time;
    int serve_time;
    int wait_time = 0;
    bool vip;

    Player &operator=(Player p) {
        this->arrive_time = p.arrive_time;
        this->using_time = p.using_time;
        this->vip = p.vip;
        return *this;
    }
};

bool my_cmp(Player a, Player b) {
    return a.arrive_time < b.arrive_time;
}

int main() {
    int table_time[110] = {0}, table_served[110] = {0};
    bool table_vip[110] = {0};
    vector<Player> all_players, res_players;
    queue<Player> q_normal, q_vip;

    int N, K, M;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int hh, mm, ss, use, vip;
        scanf("%d:%d:%d %d %d", &hh, &mm, &ss, &use, &vip);
        int time = hh * 3600 + mm * 60 + ss;
        Player t(time, use > 120 ? 120 * 60 : use * 60, vip);//最多是用2h
        all_players.push_back(t);
    }
    sort(all_players.begin(), all_players.end(), my_cmp);
    for (auto it:all_players) {//普通队列和vip队列，按到达时间排序
        if (it.vip)
            q_vip.push(it);
        else
            q_normal.push(it);
    }
    cin >> K >> M;
    for (int i = 1; i <= K; i++)
        table_time[i] = 8 * 3600;//初始化乒乓桌
    for (int i = 0; i < M; i++) {//标记vip桌
        int t;
        cin >> t;
        table_vip[t] = true;
    }
    // 队列本质的作用是实现按序遍历，最终数据的存储要靠vector
    // 每一轮必然要为一个人服务，所谓等待只不过是值的变化
    while (q_vip.size() || q_normal.size()) {
        int min_all_id = 0, min_all_time = 1000000;
        int min_vip_id = 0, min_vip_time = 1000000;
        // 分别找时间值最小的所有球桌和VIP球桌编号，也就是即将服务完成的桌子
        for (int i = 1; i <= K; i++) {
            if (table_time[i] < min_all_time) {
                min_all_time = table_time[i];
                min_all_id = i;
            }
            if (table_time[i] < min_vip_time && table_vip[i]) {
                min_vip_time = table_time[i];
                min_vip_id = i;
            }
        }

        // 选桌子，是不是必须选VIP球桌
        int min_id;
        // 必须选择VIP桌的两种情况：1. 队列中VIP排在普通客户前 且 
        // 2. 且 队列中无普通客户
        if ((q_vip.front().arrive_time < q_normal.front().arrive_time &&
             q_vip.front().arrive_time >= table_time[min_vip_id] && q_vip.size()) ||
            (q_vip.front().arrive_time >= table_time[min_vip_id] && q_normal.empty()))
            min_id = min_vip_id;
        // 不用选VIP桌子，那么就选所有球桌
        else min_id = min_all_id;
        // 这一轮服务开始时间，至关重要，用来判断队列的优先
        int min_time = table_time[min_id];

        // 选完桌子，选人，该谁到这个桌子去打球呢？
        // 由于遍历条件是两个队列均为空，因此在遍历时不知道哪个队列为空，需要额外再作判断
        Player next;
        // 如果VIP队列无人，那么普通用户上，下同
        if (q_vip.empty()) {
            next = q_normal.front();
            q_normal.pop();
        // 如果普通用户队列无人，那么VIP上
        // 另外，如果当前选的桌子是VIP球桌，且到达时间早于桌子可用时间，那么VIP上
        // （如果arrive_time > min_time，也就是说这个VIP还没到，那么我就按照下面情况，看作普通客户按时服务）
        } else if (q_normal.empty() || (table_vip[min_id] && q_vip.front().arrive_time <= min_time)) {
            next = q_vip.front();
            q_vip.pop();
        // 其它情况，也就是VIP和普通客户队列都不为空，且不存在VIP插队，那么都看作普通客户，按到达时间服务
        } else {
            // 尽管桌子空闲，VIP还没到，但是如果普通客户比VIP还晚到，那么我还是分配给VIP
            if (q_vip.front().arrive_time < q_normal.front().arrive_time) {
                next = q_vip.front();
                q_vip.pop();
            } else {
                next = q_normal.front();
                q_normal.pop();
            }
        }

        if (next.arrive_time < min_time) { //需要等
            next.serve_time = min_time;
            next.wait_time = (min_time - next.arrive_time + 30) / 60;
        } else { //不需要等
            next.serve_time = next.arrive_time;
        }

        // 超过营业时间，数据剔除
        if (next.serve_time >= 21 * 3600)
            continue;
        // 更新当前桌子服务结束也就是下一轮服务开始的时间，为下一步做准备
        table_time[min_id] = next.serve_time + next.using_time;
        res_players.push_back(next);
        table_served[min_id]++;
    }

    for (auto it:res_players) {
        int time = it.arrive_time;
        printf("%02d:%02d:%02d ", time / 3600, (time / 60) % 60, time % 60);
        time = it.serve_time;
        printf("%02d:%02d:%02d %d\n", time / 3600, (time / 60) % 60, time % 60, it.wait_time);
    }
    // 输出每个球桌服务的客户总数
    for (int i = 1; i <= K; i++) {
        cout << table_served[i];
        if (i < K)cout << " ";
    }
    return 0;
}
