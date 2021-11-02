import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import HomePage from "./pages/HomePage";
import AppPage from "./pages/AppPage";
import SignUpPage from "./pages/SignUpPage";
import LoginPage from "./pages/LoginPage";
import ListPage from "./pages/ListPage";

export default function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/app">
          <AppPage />
        </Route>
        <Route path="/signup">
          <SignUpPage />
        </Route>
        <Route path="/login">
          <LoginPage />
        </Route>
        <Route exact path="/">
          <HomePage />
        </Route>
        <Route path="/app/:id">
          <ListPage />
        </Route>
      </Switch>
    </Router>
  );

}
