#include <iostream>

using namespace std;

char board[3][3];
char currentPlayer;

void resetBoard() {
    char count = '1';

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = count++;
        }
    }

    currentPlayer = 'X';
}

void showBoard() {
    cout << "\n";
    cout << " " << board[0][0] << " | " << board[0][1] << " | " << board[0][2] << endl;
    cout << "---|---|---" << endl;
    cout << " " << board[1][0] << " | " << board[1][1] << " | " << board[1][2] << endl;
    cout << "---|---|---" << endl;
    cout << " " << board[2][0] << " | " << board[2][1] << " | " << board[2][2] << endl;
    cout << "\n";
}

bool checkWin() {

    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return true;

        if (board[0][i] == board[1][i] && board[1][i] == board[2][i])
            return true;
    }

    if (board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return true;

    if (board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return true;

    return false;
}

bool checkDraw() {

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] != 'X' && board[i][j] != 'O')
                return false;
        }
    }

    return true;
}

void switchPlayer() {
    if (currentPlayer == 'X')
        currentPlayer = 'O';
    else
        currentPlayer = 'X';
}

void makeMove() {
    int choice;
    bool validMove = false;

    while (!validMove) {

        cout << "Player " << currentPlayer << ", enter your move (1-9): ";
        cin >> choice;

        int row = (choice - 1) / 3;
        int col = (choice - 1) % 3;

        if (choice >= 1 && choice <= 9 && board[row][col] != 'X' && board[row][col] != 'O') {
            board[row][col] = currentPlayer;
            validMove = true;
        }
        else {
            cout << "Invalid move! Try again." << endl;
        }
    }
}

int main() {

    char playAgain = 'y';

    while (playAgain == 'y' || playAgain == 'Y') {

        resetBoard();

        bool gameOver = false;

        while (!gameOver) {

            showBoard();
            makeMove();

            if (checkWin()) {
                showBoard();
                cout << "Player " << currentPlayer << " wins!" << endl;
                gameOver = true;
            }
            else if (checkDraw()) {
                showBoard();
                cout << "Game is a draw!" << endl;
                gameOver = true;
            }
            else {
                switchPlayer();
            }
        }

        cout << "Do you want to play again? (y/n): ";
        cin >> playAgain;
    }

    return 0;
}