import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// Components => we build the app by stringing components together
// Composed of the following three things:
// State
// Lifecycle => fetching data from api, adding component to DOM
// UI

function isAuthed() {
  return true;
}
export default class App extends React.Component {
  render() {
    const authed = isAuthed();
    const name = 'Kai';
    // this is the description of the UI
    return (
      <div>
        <h1>Hi, my name is {name}</h1>
        <p>Hello and happy 4th of July!</p>
        <p>Today is {new Date().toLocaleString()}</p>
        <p>What is 2 + 2? It equals {2 + 2}</p>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
