import React, { useEffect, useState } from "react";
import { fetchMenu, placeOrder } from "../services/api";
import MenuItem from "../components/MenuItem";
import Cart from "../components/Cart";

export default function MenuPage() {
  const [menu, setMenu] = useState([]);
  const [cart, setCart] = useState([]);
  const [table, setTable] = useState(null);

  // ✅ Get table number from URL
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const tableParam = params.get("table");
    if (tableParam) {
      setTable(parseInt(tableParam));
    }
  }, []);

  // Load menu items
  useEffect(() => {
    fetchMenu().then(data => setMenu(data));
  }, []);

  const addToCart = (item) => {
    const existing = cart.find(i => i.id === item.id);
    if (existing) {
      setCart(cart.map(i =>
        i.id === item.id ? { ...i, quantity: i.quantity + 1 } : i
      ));
    } else {
      setCart([...cart, { ...item, quantity: 1 }]);
    }
  };

  const removeFromCart = (item) => {
    setCart(cart.filter(i => i.id !== item.id));
  };

  const checkout = async () => {
    if (!table) {
      alert("⚠️ No table number detected. Please scan the QR code from your table.");
      return;
    }

    const order = {
      table_number: table,
      items: cart.map(c => ({ menu_id: c.id, quantity: c.quantity }))
    };

    await placeOrder(order);
    alert(`✅ Order placed for table ${table}!`);
    setCart([]);
  };

  return (
    <div className="menu-page">
      <h1>MenuLink – Digital Menu</h1>
      {table ? <h3>📍 Table {table}</h3> : <p>⚠️ No table detected</p>}
      
      <div className="menu-grid">
        {menu.map(item => (
          <MenuItem key={item.id} item={item} addToCart={addToCart} />
        ))}
      </div>

      <Cart cart={cart} removeFromCart={removeFromCart} checkout={checkout} />
    </div>
  );
}
