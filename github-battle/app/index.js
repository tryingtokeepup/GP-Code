import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Popular from './components/Popular';
import Battle from './components/Battle';

export default class App extends React.Component {
  render() {
    return (
      <div className="container">
        <Battle />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));

// Components => we build the app by stringing components together
// Composed of the following three things:
// State
// Lifecycle => fetching data from api, adding component to DOM
// UI
