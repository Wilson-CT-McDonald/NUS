import "./Company.css";
function Company(props) {
  // Destructuring with default values
  const {
    companyName = "unknown company",
    details = "No details",
    children,
  } = props;
  //   const buttonHandler = (companyName) => {
  //     console.log("button Clicked: " + companyName);
  //   };
  return (
    <div className="details">
      <h1>
        Company Name: <span>{companyName} </span>
      </h1>
      <p>{details}</p>
      {children}
      <button className="primary-btn-md">Select {companyName}</button>
      {/* { <button
        onClick={() => {
          buttonHandler(companyName);
        }}
      >
        Select {companyName}
      </button>} */}
    </div>
  );
}

export default Company;
