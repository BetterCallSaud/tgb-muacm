import Home from "./Views/Home/Home.view";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { HashRouter, Link } from "react-router-dom";
import { Switch } from 'react-router';

function App() {
  return (
    <div className="App">
      <HashRouter basename="/">
        <Switch>
          <Route 
            path="/" 
            exact component={Home} 
          />
        </Switch>
      </HashRouter>
    </div>
  );
}

export default App;
