import "./App.css";
import Company from "./components/company/Company";

export default function App() {
  return (
    <div className="container">
      <h1 className="main-title"> I'm from App Component </h1>
      <Company companyName="Google" details="search for anything" />
      <Company companyName="Amazon" details="purchase anything" />
      <Company companyName="Youtube" details="watch anything" />
      <Company />
      <Company>
        <h1>I'm from app component but load from company component</h1>
      </Company>
    </div>
  );
}
