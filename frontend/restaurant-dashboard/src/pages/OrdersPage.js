import React, { useEffect, useState } from "react";
import { fetchOrders, updateOrderStatus } from "../services/api";
import OrderCard from "../components/OrderCard";

export default function OrdersPage() {
  const [orders, setOrders] = useState([]);

  const loadOrders = async () => {
    const data = await fetchOrders();
    setOrders(data);
  };

  useEffect(() => {
    loadOrders();
    const interval = setInterval(loadOrders, 5000); // auto-refresh every 5s
    return () => clearInterval(interval);
  }, []);

  const handleStatusChange = async (orderId, newStatus) => {
    await updateOrderStatus(orderId, newStatus);
    loadOrders();
  };

  return (
    <div>
      <h1>📊 Restaurant Dashboard</h1>
      <button onClick={loadOrders}>🔄 Refresh Orders</button>
      <div>
        {orders.length === 0 ? (
          <p>No orders yet.</p>
        ) : (
          orders.map((order) => (
            <OrderCard key={order.id} order={order} onStatusChange={handleStatusChange} />
          ))
        )}
      </div>
    </div>
  );
}
