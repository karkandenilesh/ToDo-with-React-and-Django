// import React, { useState, useEffect } from "react";
// import { Row, Col, Table } from "react-bootstrap";
// import Product from "../components/Product";
// import axios from "axios";
// import "./screens.css";
// import { Link } from "react-router-dom";

// function EmployeeMaster() {
//   const [Employee, setEmployee] = useState([]);

//   useEffect(() => {
//     async function fetchEmployee() {
//       const { data } = await axios.get("http://127.0.0.1:8000/api/employee");
//       setEmployee(data);
//     }

//     fetchEmployee();
//   }, []);

//   return (
//     <Table class="table" striped bordered hover responsive>
//       <thead>
//         <tr>
//           <th>F_Name</th>
//           <th>L_Name</th>
//           <th>Designation</th>
//           <th>Department</th>
//           <th>Date_Of_Joining</th>
//           <th>Date_Of_Exit</th>
//           <th>Email</th>
//           <th>Emp_Status</th>
//           <th>Created By</th>
//           <th>Created At</th>
//         </tr>
//       </thead>
//       <tbody>
//         {Employee.map((Employee) => (
//           <tr key={Employee.Emp_ID}>
//             {/* <td>
//               <Link to={`/Employee/${Employee._id}`}>{Employee.name}</Link>
//             </td> */}
//             <td>{Employee.F_name}</td>
//             <td>{Employee.L_name}</td>
//             <td>{Employee.Designation_ID}</td>
//             <td>{Employee.Dept_ID}</td>
//             <td>{Employee.Date_of_joining}</td>
//             <td>{Employee.Date_of_exit}</td>
//             <td>{Employee.Email_ID}</td>
//             <td>{Employee.Emp_status ?? "Active"}</td>
//             <td>{Employee.Created_by}</td>
//             {/* <td>{Employee.Created_by ? Employee.Created_by.User : "N/A"}</td> */}
//             <td>{Employee.date_created}</td>
//           </tr>
//         ))}
//       </tbody>
//     </Table>
//   );
// }

// export default EmployeeMaster;

// import React from "react";
// import Sidebar from "./Sidebar";
// import Navbars from "./Navbars";

// import "./Master.css";
import React, { useState, useEffect } from "react";
import { Row, Col, Table } from "react-bootstrap";
// import Product from "../components/Product";
import axios from "axios";
// import "./screens.css";
import { Link } from "react-router-dom";

function EmployeeMaster() {
  const [Employee, setEmployee] = useState([]);

  useEffect(() => {
    async function fetchEmployee() {
      const { data } = await axios.get("http://127.0.0.1:8000/api/employee");
      setEmployee(data);
    }

    fetchEmployee();
  }, []);

  return (
    <div className="d-flex">
      <div className="col-auto">
        {/* <Navbars />
        <Sidebar /> */}
      </div>
      <div>
        <table className="creative-table">
          <thead>
            <tr>
              <th>F_Name</th>
              <th>L_Name</th>
              <th>Designation</th>
              <th>Department</th>
              <th>Date_Of_Joining</th>
              <th>Date_Of_Exit</th>
              <th>Email</th>
              <th>Emp_Status</th>
              <th>Created By</th>
              <th>Created At</th>
            </tr>
          </thead>
          <tbody>
            {Employee.map((Employee) => (
              <tr key={Employee.Emp_ID}>
                {/* <td>
              <Link to={`/Employee/${Employee._id}`}>{Employee.name}</Link>
            </td> */}
                <td>{Employee.F_name}</td>
                <td>{Employee.L_name}</td>
                <td>{Employee.Designation_ID}</td>
                <td>{Employee.Dept_ID_id}</td>
                <td>{Employee.Date_of_joining}</td>
                <td>{Employee.Date_of_exit}</td>
                <td>{Employee.Email_ID}</td>
                <td>{Employee.Emp_status ?? "Active"}</td>
                <td>{Employee.Created_by}</td>
                {/* <td>{Employee.Created_by ? Employee.Created_by.User : "N/A"}</td> */}
                <td>{Employee.date_created}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default EmployeeMaster;
