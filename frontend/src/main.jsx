import React from 'react'
import ReactDOM from 'react-dom/client'
import Navbar from './components/Navbar';
import Home from "./Home";
import './index.css'
import Features from './components/Features';
import FooterComponent from './components/FooterComponent';
import HeroSection from './components/HeroSection';
import FileSummary from './components/FileSummary';
import AboutUs from './components/AboutUs';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>

    <>
      <Navbar />
      <HeroSection />
      <Features />
      <FileSummary />
      <AboutUs />
      <FooterComponent />
    </>
  </React.StrictMode>

