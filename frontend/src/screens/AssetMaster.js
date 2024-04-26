// import "./Master.css";
import React, { useState, useEffect } from "react";
import { Row, Col, Table } from "react-bootstrap";
// import Product from "../components/Product";
import axios from "axios";
// import "./screens.css";
import { Link } from "react-router-dom";
import NavBar from "../components/NavBar";

function AssetMaster() {
  const [Asset, setAsset] = useState([]);

  useEffect(() => {
    async function fetchAsset() {
      const { data } = await axios.get("http://127.0.0.1:8000/api/asset");
      setAsset(data);
    }

    fetchAsset();
  }, []);

  return (
    <div className="d-flex">
      <NavBar />
      <div className="col-auto">
        {/* <Navbars />
        <Sidebar /> */}
      </div>
      <div>
        <table className="creative-table">
          <thead>
            <tr>
              <th>Asset Serial Number</th>
              <th>Model Number</th>
              <th>Model Name</th>
              <th>Asset Cat ID</th>
              <th>ERP Code</th>
              <th>Invoice No.</th>
              <th>Invoice Date</th>
              <th>PO No.</th>
              <th>PO Date</th>
              <th>Cost Of Unit</th>
              <th>Warranty SDate</th>
              <th>Warranty EDate</th>
              <th>GRN No.</th>
              <th>GRN Date</th>
              <th>Vendor ID</th>
              <th>Created By</th>
              <th>Date Created</th>
            </tr>
          </thead>
          <tbody>
            {Asset.map((Asset) => (
              <tr key={Asset.asset_serial_number}>
                {/* <td>
              <Link to={`/Employee/${Employee._id}`}>{Employee.name}</Link>
            </td> */}
                <td>{Asset.asset_serial_number}</td>
                <td>{Asset.model_number}</td>
                <td>{Asset.model_name}</td>
                <td>{Asset.asset_cat_ID}</td>
                <td>{Asset.erp_code}</td>
                <td>{Asset.invoice_number}</td>
                <td>{Asset.invoice_date}</td>
                <td>{Asset.po_number}</td>
                <td>{Asset.po_date}</td>
                <td>{Asset.cost_of_unit}</td>
                <td>{Asset.warranty_sdate}</td>
                <td>{Asset.warranty_edate}</td>
                <td>{Asset.grn_number}</td>
                <td>{Asset.grn_date}</td>
                <td>{Asset.Vendor_ID}</td>
                <td>{Asset.Created_by}</td>
                <td>{Asset.date_created}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default AssetMaster;
