import React, { useState, useEffect } from 'react';
import './App.css';

const Cell = ({ value, onClick }) => (
  <div className="cell" onClick={onClick}>
    {value}
  </div>
);

const Board = ({ board, onCellClick }) => (
  <div className="board">
    {board.map((row, rowIndex) => (
      <div className="row" key={rowIndex}>
        {row.map((cell, colIndex) => (
          <Cell
            key={colIndex}
            value={cell}
            onClick={() => onCellClick(colIndex)}
          />
        ))}
      </div>
    ))}
  </div>
);

function App() {
  const [board, setBoard] = useState([]);
  const [currentPlayer, setCurrentPlayer] = useState('X');

  useEffect(() => {
    fetch('http://localhost:5000/api/game-state')
      .then(response => response.json())
      .then(data => setBoard(data));
  }, []);

  const handleCellClick = async (col) => {
    if (board[0][col] !== ' ') return; // Prevent moves in full columns

    try {
      const response = await fetch('http://localhost:5000/api/make-move', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ col, player: currentPlayer }),
      });

      const newBoard = await response.json();
      setBoard(newBoard);

      // Switch player
      setCurrentPlayer(currentPlayer === 'X' ? 'O' : 'X');
    } catch (error) {
      console.error("Failed to fetch:", error);
    }
  };

  const handleReset = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/reset', {
        method: 'POST',
      });

      const newBoard = await response.json();
      setBoard(newBoard);
      setCurrentPlayer('X');
    } catch (error) {
      console.error("Failed to fetch:", error);
    }
  };

  return (
    <div className="App">
      <h1>Connect Four</h1>
      <Board board={board} onCellClick={handleCellClick} />
      <button onClick={handleReset}>Reset Game</button>
    </div>
  );
}

export default App;