import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Form from './Form';

const { ipcRenderer } = window.require('electron');

function App() {
  const [count, setCount] = useState(0)
  const [showForm, setShowForm] = useState(false);



  useEffect(() => {
    ipcRenderer.on('open-form', () => {
      setShowForm(true);
    });

    return () => {
      ipcRenderer.removeAllListeners('open-form');
    };
  }, []);



  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>

      {showForm && (
        <div style={{
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
          background: 'rgba(0,0,0,0.5)',
          display: 'flex', justifyContent: 'center', alignItems: 'center'
        }}>
          <div style={{ background: 'white', padding: '20px', borderRadius: '8px' }}>
            <Form />
            <button onClick={() => setShowForm(false)} style={{ marginTop: '10px' }}>
              Close
            </button>
          </div>
        </div>
      )}

    </>
  )
}

export default App
