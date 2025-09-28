import React from "react";

export default function OrderCard({ order, onStatusChange }) {
  return (
    <div className="order-card" style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
      <h3>📝 Order #{order.id}</h3>
      <p>Table: {order.table_number || "N/A"}</p>
      <p>Status: <b>{order.status}</b></p>
      <div>
        {["pending", "confirmed", "completed", "cancelled"].map((status) => (
          <button
            key={status}
            disabled={order.status === status}
            onClick={() => onStatusChange(order.id, status)}
            style={{ margin: "5px" }}
          >
            {status}
          </button>
        ))}
      </div>
    </div>
  );
}
