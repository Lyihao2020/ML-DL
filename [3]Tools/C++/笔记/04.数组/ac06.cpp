// 输入一个n行m列的矩阵，从左上角开始将其按回字形的顺序顺时针打印出来
#include<iostream>
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    int a[n][m];

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            cin >> a[i][j];

    int up = 0, down = n - 1, left = 0, right = m - 1;
    while(true){
        for(int i = left; i <= right; i++) cout << a[up][i] << " ";
        if(++up > down) break;
        for(int i = up; i <= down; i++) cout << a[i][right] << " ";
        if(--right < left) break;
        for(int i = right; i >= left; i--) cout << a[down][i] << " ";
        if(--down < up) break;
        for(int i = down; i >= up; i--) cout << a[i][left] << " ";
        if(++left > right) break;
    }
    
    return 0;
}

/*
#include<iostream>
#include<vector>

using namespace std;

void printMatrix(vector<vector<int>>& matrix) {
    int row = matrix.size();
    if (row == 0) return;
    int col = matrix[0].size();
    int up = 0, down = row - 1, left = 0, right = col - 1;
    while (true) {
        for (int j = left; j <= right; j++) cout << matrix[up][j] << " ";
        if (++up > down) break;
        for (int i = up; i <= down; i++) cout << matrix[i][right] << " ";
        if (--right < left) break;
        for (int j = right; j >= left; j--) cout << matrix[down][j] << " ";
        if (--down < up) break;
        for (int i = down; i >= up; i--) cout << matrix[i][left] << " ";
        if (++left > right) break;
    }
}

int main() {
    vector<vector<int>> matrix{{1,2,3},{4,5,6},{7,8,9}};
    printMatrix(matrix);
    return 0;
}

*/