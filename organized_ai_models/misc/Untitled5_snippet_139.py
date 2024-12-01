// In your React project, create a new component (e.g., InteractionLogger.js)

import React, { useState } from 'react';

function InteractionLogger() {
  const [interactionData, setInteractionData] = useState('');

  const handleInteraction = async (interactionType) => {
    const response = await fetch('http://localhost:5000/log_interaction', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        interaction_type: interactionType,
        data: interactionData,
      }),
    });
    const result = await response.json();
    console.log(result);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter interaction data"
        value={interactionData}
        onChange={(e) => setInteractionData(e.target.value)}
      />
      <button onClick={() => handleInteraction('emotion_detection')}>Log Emotion</button>
    </div>
  );
}

export default InteractionLogger;
