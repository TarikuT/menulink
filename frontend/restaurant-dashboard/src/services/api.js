import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const fetchOrders = async () => {
  const res = await API.get("/order/");
  return res.data;
};

export const updateOrderStatus = async (orderId, newStatus) => {
  const res = await API.post(`/order/${orderId}/status/${newStatus}`);
  return res.data;
};
