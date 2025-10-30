import React, { useState } from "react";
import MapView from "./components/MapView";
import Sidebar from "./components/Sidebar";
import "./App.css";

export default function App() {
  const [forecast, setForecast] = useState(null);
  return (
    <div className="flex">
      <Sidebar setForecast={setForecast} forecast={forecast} />
      <MapView forecast={forecast} />
    </div>
  );
}
