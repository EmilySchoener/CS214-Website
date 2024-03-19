import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";
import logo from "../images/logo.png";

const Navbar = () => {
    return (
        <>
            <Nav>
                <NavMenu>
                    <img src={logo} width={165} height={100}/>
                    <NavLink to="/" activeStyle>
                        Home
                    </NavLink>
                    <NavLink to="/about" activeStyle>
                        About
                    </NavLink>
                    <NavLink to="/unit1" activeStyle>
                        Unit 1
                    </NavLink>
                    <NavLink to="/unit3" activeStyle>
                        Unit 3
                    </NavLink>
                    <NavLink to="/unit4" activeStyle>
                        Unit 4
                    </NavLink>
                    <NavLink to="/unit5" activeStyle>
                        Unit 5
                    </NavLink>
                    <NavLink to="/unit6" activeStyle>
                        Unit 6
                    </NavLink>
                    <NavLink to="/unit7" activeStyle>
                        Unit 7
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;