import React, { useState } from "react";
import { getForecast, sendAlert } from "../api";

export default function Sidebar({ setForecast, forecast }) {
  const [rain, setRain] = useState([5, 10, 20, 15, 0, 0]);
  const [phone, setPhone] = useState("");

  const handleForecast = async () => {
    const { data } = await getForecast({
      rain_seq: rain,
      static_feat: [100, 30, 10]
    });
    setForecast(data.predicted_level);
  };

  const handleAlert = async () => {
    await sendAlert({
      message: `🚨 Flood alert! Predicted water level = ${forecast.toFixed(2)} m.`,
      recipients: [phone]
    });
    alert("Alert sent!");
  };

  return (
    <div className="w-1/3 p-4 bg-gray-100">
      <h2 className="font-bold text-lg mb-4">Flood Forecast</h2>
      <button onClick={handleForecast} className="bg-blue-500 text-white px-3 py-2 rounded">
        Predict Flood Level
      </button>
      {forecast && (
        <>
          <p className="mt-3 text-green-700">Predicted Level: {forecast.toFixed(2)} m</p>
          <input
            className="mt-4 p-2 border w-full"
            placeholder="Enter phone number"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
          <button onClick={handleAlert} className="mt-2 bg-red-500 text-white px-3 py-2 rounded">
            Send Alert
          </button>
        </>
      )}
    </div>
  );
}
