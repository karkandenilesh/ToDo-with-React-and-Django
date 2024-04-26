// import "./Master.css";
import React, { useState, useEffect } from "react";
import { Row, Col, Table } from "react-bootstrap";
// import Product from "../components/Product";
import axios from "axios";
// import "./screens.css";
import { Link } from "react-router-dom";

function VendorMaster() {
  const [Vendor, setVendor] = useState([]);

  useEffect(() => {
    async function fetchVendor() {
      const { data } = await axios.get("http://127.0.0.1:8000/api/vendor");
      setVendor(data);
    }

    fetchVendor();
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
              <th>Vendor_ID</th>
              <th>Vendor_name</th>
              <th>Contact</th>
              <th>Email</th>
              <th>GST No.</th>
              <th>Created By</th>
              <th>Created At</th>
            </tr>
          </thead>
          <tbody>
            {Vendor.map((Vendor) => (
              <tr key={Vendor.Emp_ID}>
                {/* <td>
              <Link to={`/Employee/${Employee._id}`}>{Employee.name}</Link>
            </td> */}
                <td>{Vendor.Vendor_ID}</td>
                <td>{Vendor.Vendor_name}</td>
                <td>{Vendor.Contact}</td>
                <td>{Vendor.Email}</td>
                <td>{Vendor.gst_no}</td>
                <td>{Vendor.Created_by}</td>
                <td>{Vendor.date_created}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default VendorMaster;
