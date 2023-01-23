import React, {useState} from 'react';
import './App.css';
import UFClogo from './Images/UFCLOGO.png';
import Spinner from './Components/Loader';

function App() {

  const [fighterWin, setFighterWin] = useState('');
  const [f1fn, setF1fn] = useState('');
  const [f1ln, setF1ln] = useState('');
  const [f2fn, setF2fn] = useState('');
  const [f2ln, setF2ln] = useState('');
  const [readout, setReadout] = useState('');
  const [waitMessage, setWaitMessage] = useState('');  
  const [isLoading, setIsLoading] = useState(false);

   
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    const fighterInput = { f1fn, f1ln, f2fn, f2ln }
    setIsLoading(true);
    setFighterWin('loading...');
    setReadout('');
    const longWait = setTimeout(() => {
      setWaitMessage('this may take awhile');
    }, "12000")
  
    try {
      const res = await fetch("/prediction", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(fighterInput)
      });

      const data = await res.json();

      setFighterWin(data?.winner);
      setReadout('The predicted winner is:');
      setIsLoading(false);
      setWaitMessage('');
      clearTimeout(longWait);
    } catch (e) {
      console.error(e);
      setWaitMessage('');
      setFighterWin('');
      setReadout('Check your Spelling');
      setIsLoading(false);
      clearTimeout(longWait);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <title>UFC Fight Predictor</title>
        <img src={UFClogo} className="App-logo" alt="logo" />
        <p>
        <strong>FIGHT PREDICTOR</strong>
        </p>
        <p>
          Enter the first and last names of the fighters you would like to compare below:
        </p>        
      </header>
      <h1 className="App-body">
        <form 
        action ="/prediction" 
        method="post" 
        className="fighter-form"
        onSubmit={handleSubmit}> 
          <p className="fighter-inputs">
            <label htmlFor="fighter_1_fn">
            Fighter 1:
            </label>  
            <br></br>       
            <input name="f1fn" 
            type="text" 
            id="fighter_1_fn" 
            placeholder="First Name" 
            required
            value={f1fn}
            onChange={(e) => setF1fn(e.target.value)}>
            </input>
            <label htmlFor="fighter_1_ln">
            </label>
            <input 
            name="f1ln" 
            type="text" 
            id="fighter_1_ln" 
            placeholder="Last Name" 
            required
            value={f1ln}
            onChange={(e) => setF1ln(e.target.value)}>
            </input>
            <label htmlFor="fighter_2_fn">
              <br/>
            Fighter 2:
            <br></br>
            </label>
            <input 
            name="f2fn" 
            type="text" 
            id="fighter_2_fn" 
            placeholder="First Name" 
            required
            value={f2fn}
            onChange={(e) => setF2fn(e.target.value)}>
            </input>
            <label htmlFor="fighter_2_ln">
            </label>
            <input 
            name="f2ln" 
            type="text" 
            id="fighter_2_ln" 
            placeholder="Last Name" 
            required
            value={f2ln}
            onChange={(e) => setF2ln(e.target.value)}>
            </input>
        </p>
        <button 
        id="submit" 
        name="submit"
        className="input-button"
        disabled={isLoading}>Who Will Win?</button>
        {isLoading ? <Spinner /> : handleSubmit}
      </form>
    <p className="bottom-read">{readout} {fighterWin} {waitMessage}</p>
     </h1>
     <footer>
      Do not make bets using this information, seriously, it is only for fun. 
      Unless you want to I guess, but it's not our fault if you lose all your money.
      </footer> 
      <footer className="footer-main">
        Data pulled from the <a
          className="App-link"
          href="https://www.ufc.com/"
          target="_blank"
          rel="noopener noreferrer">UFC website</a>
      </footer>
      <footer>
        <br> 
        </br>
      </footer>
    </div>
  );
}

export default App;