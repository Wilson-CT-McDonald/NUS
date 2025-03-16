import React from "react";
import ReactDOM from "react-dom/client";
import "./App";
import App from "./App";
import "./styles.css";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  // without the fragment, it wont work
  <React.Fragment>
    <h1>Hello World</h1>
    <h2>Welcome to the session</h2>
    <App />
  </React.Fragment>
);
