import React from "react";

export default function MenuItem({ item, addToCart }) {
  return (
    <div className="menu-item">
      <h3>{item.name}</h3>
      <p>{item.description}</p>
      <p><b>€{item.price}</b></p>
      <button onClick={() => addToCart(item)}>Add to Cart</button>
    </div>
  );
}
