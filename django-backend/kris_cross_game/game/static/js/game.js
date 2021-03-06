let whose_move = 'player1';

function change_move() {
    if (whose_move === 'player1') {
        whose_move = "player2"
    } else if (whose_move === "player2") {
        whose_move = "player1"
    }
}

change_move();

console.log(whose_move);