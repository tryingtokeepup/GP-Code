import React from 'react';

export default class Sayo extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      state: 'happy'
    };
  }

  render() {
    return (
      <React.Fragment>
        <h1>Sayo bayo daze.</h1>
      </React.Fragment>
    );
  }
}
