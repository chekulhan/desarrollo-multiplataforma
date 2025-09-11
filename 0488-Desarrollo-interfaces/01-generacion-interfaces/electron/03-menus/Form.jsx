import { useState } from 'react';

export default function Form() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Hello ${name}, your email is ${email}`);
    console.log({ name, email });
  };

  return (
    <form onSubmit={handleSubmit} style={{ padding: '20px' }}>
      <div>
        <label>
          Name:
          <input 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
            style={{ marginLeft: '10px' }}
          />
        </label>
      </div>

      <div style={{ marginTop: '10px' }}>
        <label>
          Email:
          <input 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
            style={{ marginLeft: '10px' }}
          />
        </label>
      </div>

      <button type="submit" style={{ marginTop: '15px' }}>Submit</button>
    </form>
  );
}
