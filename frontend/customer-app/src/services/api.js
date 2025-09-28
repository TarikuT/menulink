import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", // backend
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
