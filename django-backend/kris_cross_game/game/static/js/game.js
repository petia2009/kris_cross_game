let whose_move = 'player1';
let descr_player1 = 'Ожидание хода...       ';
let descr_player2 = 'Сейчас не ваш ход.';

let descr_player1_html = document.getElementById("descr_player1");
let descr_player2_html = document.getElementById("descr_player2");

function change_descrs() {
    descr_player1_html.innerHTML = descr_player1;
    descr_player2_html.innerHTML = descr_player2;
}

function change_move() {
    if (whose_move === 'player1') {
        whose_move = "player2";
        descr_player1 = 'Сейчас не ваш ход.';
        descr_player2 = 'Ожидание хода...   ';
    } else if (whose_move === "player2") {
        whose_move = "player1";
        descr_player1 = 'Ожидание хода...   ';
        descr_player2 = 'Сейчас не ваш ход.';
    }
}

function move(td, coord) {

    // var request = new XMLHttpRequest();
    // request.open('GET', '?coords=' + coord, false);
    // request.send();

    // if (!td.classList.contains("not_free")) {
    //     if (whose_move === 'player1') {
    //         td.innerHTML = 'X';
    //         td.classList.add("not_free");
    //         change_move();
    //         change_descrs()
    //     } else if (whose_move === 'player2') {
    //         td.innerHTML = 'O';
    //         td.classList.add("not_free");
    //         change_move();
    //         change_descrs()
    //     }
    // }

}
