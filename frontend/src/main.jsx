import React from 'react'
import ReactDOM from 'react-dom/client'
import Navbar from './components/Navbar';
import Home from "./Home";
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <div className="bg-neutral-900 min-h-screen">
    <Navbar />
      <Home />
    
    </div>
  </React.StrictMode>,
)
