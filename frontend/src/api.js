import axios from "axios";
const API = axios.create({ baseURL: "http://localhost:5000/api/v1" });

export const getForecast = (payload) => API.post("/forecast", payload);
export const sendAlert = (payload) => API.post("/alert", payload);
