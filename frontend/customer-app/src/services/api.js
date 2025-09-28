import axios from "axios";

// Use environment variable first, fallback to localhost
const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

const API = axios.create({
  baseURL: API_URL,
});

// ✅ use named exports
export const fetchMenu = async () => {
  const res = await API.get("/menu/");
  return res.data;
};

export const placeOrder = async (order) => {
  const res = await API.post("/order/", order);
  return res.data;
};
