import React from 'react';
import UserService from './components/UserService';
import PaymentService from './components/PaymentService';
import ProductService from './components/ProductService';

const App = () => {
  return (
    <div>
      <h1>Microservices Example</h1>
      <UserService />
      <PaymentService />
      <ProductService />
    </div>
  );
};

export default App;