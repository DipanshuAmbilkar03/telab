#include <iostream>
#include <vector>
using namespace std;

#define INF 999

// Function to print actual path between routers
void printPath(int i, int j, int via[10][10]) {
    if (via[i][j] == j) {
        cout << "Router " << j + 1;
        return;
    }
    printPath(i, via[i][j], via);
    cout << " -> Router " << j + 1;
}

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

    // Initialize distance and via matrices
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = cost[i][j];
            via[i][j] = j;
        }
    }

    // Distance Vector update (Bellman-Ford-like)
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    via[i][j] = k;
                }

    cout << "\n=== Final Distance Vector Table ===\n";
    for (int i = 0; i < n; i++) {
        cout << "\nRouter " << i + 1 << " Table:\n";
        for (int j = 0; j < n; j++) {
            cout << "To Router " << j + 1
                    << " via Router " << via[i][j] + 1 
                    << " | Cost = " << dist[i][j] << endl;
        }
    }

    // Show shortest paths
    cout << "\n=== Shortest Paths Between Routers ===\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && dist[i][j] != INF) {
                cout << "\nShortest path from Router " << i + 1 
                        << " to Router " << j + 1 << " : ";
                cout << "Router " << i + 1 << " -> ";
                printPath(i, j, via);
                cout << " | Total Cost = " << dist[i][j];
            }
        }
        cout << endl;
    }

    return 0;
}
