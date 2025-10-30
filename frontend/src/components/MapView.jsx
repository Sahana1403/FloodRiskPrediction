import React from "react";
import { MapContainer, TileLayer, Circle } from "react-leaflet";

export default function MapView({ forecast }) {
  return (
    <div className="w-2/3 h-screen">
      <MapContainer center={[13.08, 80.27]} zoom={8} className="h-full">
        <TileLayer
          attribution="&copy; OpenStreetMap"
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {forecast && (
          <Circle
            center={[13.08, 80.27]}
            radius={forecast * 1000}
            color="red"
            fillOpacity={0.3}
          />
        )}
      </MapContainer>
    </div>
  );
}
