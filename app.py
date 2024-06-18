from flask import Flask, request, jsonify
from connect4 import Board

app = Flask(__name__)

# Initialize the game board
game_board = Board(7, 6)

@app.route('/api/game-state', methods=['GET'])
def get_game_state():
    return jsonify(game_board.data)

@app.route('/api/make-move', methods=['POST'])
def make_move():
    data = request.get_json()
    col = data['col']
    player = data['player']
    if game_board.allowsMove(col):
        game_board.addMove(col, player)
    return jsonify(game_board.data)

@app.route('/api/reset', methods=['POST'])
def reset():
    game_board.clear()
    return jsonify(game_board.data)

if __name__ == '__main__':
    app.run(port=5000)
