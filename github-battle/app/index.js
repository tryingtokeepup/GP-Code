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
function showWarning() {
  return true;
}
export default class App extends React.Component {
  render() {
    const authed = isAuthed();

    const name = 'Kai';
    // this is the description of the UI

    return (
      <div>
        <h1>📱</h1>
        {showWarning() === true && <h3>😤</h3>}
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
