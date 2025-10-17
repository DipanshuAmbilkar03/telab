#include <iostream>
using namespace std;
#define INF 999

int main() {
    int n;
    cout << "Enter number of routers: ";
    cin >> n;

    int cost[10][10];
    cout << "Enter cost matrix (use 999 for infinity):\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> cost[i][j];

    int dist[10][10], via[10][10];
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++) {
            dist[i][j] = cost[i][j];
            via[i][j] = j;
        }
    }

    // Bellman-Ford update step
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][j] > cost[i][k] + dist[k][j]) {
                    dist[i][j] = cost[i][k] + dist[k][j];
                    via[i][j] = k;
                }

    cout << "\nFinal Distance Vector Table:\n";
    for (int i = 0; i < n; i++) {
        cout << "\nRouter " << i + 1 << " table:\n";
        for (int j = 0; j < n; j++)
            cout << "To " << j + 1 << " via " << via[i][j] + 1 << " cost = " << dist[i][j] << endl;
    }

    return 0;
}
