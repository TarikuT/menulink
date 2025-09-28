import React from "react";
export default function Cart({ cart, removeFromCart, checkout }) {
  return (
    <div className="cart">
      <h2>🛒 Cart</h2>
      {cart.length === 0 && <p>No items added</p>}
      {cart.map((item, idx) => (
        <div key={idx}>
          {item.name} x {item.quantity}
          <button onClick={() => removeFromCart(item)}>❌</button>
        </div>
      ))}
      {cart.length > 0 && (
        <button onClick={checkout}>Checkout</button>
      )}
    </div>
  );
}
