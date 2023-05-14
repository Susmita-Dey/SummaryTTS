import React from 'react'
import ReactDOM from 'react-dom/client'
import Navbar from './components/Navbar';
import './index.css'
import Features from './components/Features';
import FooterComponent from './components/FooterComponent';
import HeroSection from './components/HeroSection';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <>
      <Navbar />
      <HeroSection />
      <Features />
      <FooterComponent />
    </>
  </React.StrictMode>
)
