//react imports
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

//pages components
import App from './pages/App';
import About from './pages/About';
import Contact from './pages/Contact';
import reportWebVitals from './reportWebVitals';

//routing imports
import { createBrowserRouter, RouterProvider } from "react-router-dom"
import User from './pages/User';

//define the paths
const paths = createBrowserRouter([
  {
    path: '/',
    element: <App/>
  },
  {
    path: '/about',
    element: <About/>
  },
  {
    path: '/contact',
    element: <Contact/>
  },
  {
    path: '/user/:userId',
    element: <User/>
  }
])


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={paths} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
