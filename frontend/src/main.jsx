import React from 'react'
import ReactDOM from 'react-dom/client'
import Features from './components/Features';
import FooterComponent from './components/FooterComponent';
import HeroSection from './components/HeroSection';
import Navbar from './components/Navbar';
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <>
      <Navbar />
      <HeroSection />
      <Features />
      <FooterComponent />
    </>
  </React.StrictMode>,
)
