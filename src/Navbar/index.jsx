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
                        Chapter 1
                    </NavLink>
                    <NavLink to="/unit3" activeStyle>
                        Chapter 3
                    </NavLink>
                    <NavLink to="/unit4" activeStyle>
                        Chapter 4
                    </NavLink>
                    <NavLink to="/unit5" activeStyle>
                        Chapter 5
                    </NavLink>
                    <NavLink to="/unit6" activeStyle>
                        Chapter 6
                    </NavLink>
                    <NavLink to="/unit7" activeStyle>
                        Chapter 7
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;