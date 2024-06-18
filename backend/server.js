const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(bodyParser.json());
app.use(cors());

// Import the Board class from your connect4.js
const { Board } = require('./connect4'); // Update this line to match your import method

const gameBoard = new Board(7, 6);

app.get('/api/game-state', (req, res) => {
  res.json(gameBoard.data);
});

app.post('/api/make-move', (req, res) => {
  const { col, player } = req.body;
  if (gameBoard.allowsMove(col)) {
    gameBoard.addMove(col, player);
  }
  res.json(gameBoard.data);
});

app.post('/api/reset', (req, res) => {
  gameBoard.clear();
  res.json(gameBoard.data);
});

app.listen(port, () => {
  console.log(`Backend running at http://localhost:${port}`);
});
