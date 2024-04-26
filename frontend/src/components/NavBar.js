import React from "react";
import { useCookies } from "react-cookie";
// import React from "react";
import { NavLink, Link } from "react-router-dom";
import {
  Container,
  Row,
  Navbar,
  Nav,
  Button,
  NavDropdown,
} from "react-bootstrap";
// import "./Header.css";

function NavBar() {
  const [token, SetToken, removeToken] = useCookies(["mytoken"]);

  const logoutBtn = () => {
    removeToken(["mytoken"]);
  };

  return (
    <>
      <Container className="fb">
        <Row>
          <Navbar
            fixed="top"
            variant="dark"
            bg="dark"
            expand="sm"
            className="custom-navbar"
          >
            <Container fluid>
              <Navbar.Brand>
                {/* <img src="securens.ico" height={30} width={30} /> */}
                &nbsp; ToDo
              </Navbar.Brand>
              <Navbar.Toggle aria-controls="my-nav" />
              <Navbar.Collapse id="my-nav">
                <Nav className="me-auto fw-bold">
                  <Nav.Link as={Link} to="/">
                    Home
                  </Nav.Link>
                </Nav>
                <form action="" className="w-75">
                  <input
                    type="text"
                    className="border text-yellow"
                    placeholder="Search....."
                  />
                </form>
                <button className="btn btn-success"><a className="nav-link active" onClick={logoutBtn}>
                  Log out
                </a></button>
              </Navbar.Collapse>
            </Container>
          </Navbar>
        </Row>
      </Container>
    </>
  );
}

export default NavBar;
