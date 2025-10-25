<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Break Reminder</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f0f8ff;
    }

    .container {
      text-align: center;
      background-color: #ffffff;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    input {
      width: 60px;
      padding: 5px;
      font-size: 16px;
      margin-left: 10px;
    }

    button {
      padding: 8px 16px;
      font-size: 16px;
      margin: 5px;
      cursor: pointer;
      border-radius: 5px;
      border: none;
      background-color: #007bff;
      color: white;
    }

    button:hover {
      background-color: #0056b3;
    }

    #timer {
      font-size: 28px;
      margin-top: 20px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Break Reminder App</h1>
    <label for="minutes">Set break interval (minutes):</label>
    <input type="number" id="minutes" min="1" value="60">
    <div>
      <button id="startBtn">Start</button>
      <button id="pauseBtn">Pause</button>
      <button id="resetBtn">Reset</button>
    </div>
    <p id="timer">00:00:00</p>
  </div>

  <script>
    const startBtn = document.getElementById('startBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const resetBtn = document.getElementById('resetBtn');
    const timerDisplay = document.getElementById('timer');
    const minutesInput = document.getElementById('minutes');

    let interval;
    let totalSeconds = 0;
    let isPaused = false;

    function updateTimerDisplay() {
      const hrs = Math.floor(totalSeconds / 3600);
      const mins = Math.floor((totalSeconds % 3600) / 60);
      const secs = totalSeconds % 60;
      timerDisplay.textContent = ${hrs.toString().padStart(2,'0')}:${mins.toString().padStart(2,'0')}:${secs.toString().padStart(2,'0')};
    }

    function startTimer() {
      if (totalSeconds === 0) {
        const minutes = parseInt(minutesInput.value);
        if (isNaN(minutes) || minutes < 1) {
          alert("Please enter a valid number of minutes.");
          return;
        }
        totalSeconds = minutes * 60;
      }

      if (interval) clearInterval(interval);

      interval = setInterval(() => {
        if (!isPaused) {
          updateTimerDisplay();
          if (totalSeconds === 0) {
            clearInterval(interval);
            alert("Time for a break! 🛑");
          } else {
            totalSeconds--;
          }
        }
      }, 1000);
    }

    startBtn.addEventListener('click', () => {
      isPaused = false;
      startTimer();
    });

    pauseBtn.addEventListener('click', () => {
      isPaused = true;
    });

    resetBtn.addEventListener('click', () => {
      isPaused = true;
      totalSeconds = parseInt(minutesInput.value) * 60 || 0;
      updateTimerDisplay();
    });
  </script>
</body>
</html>
