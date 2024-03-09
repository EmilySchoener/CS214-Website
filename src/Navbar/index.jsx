import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";

const Navbar = () => {
    return (
        <>
            <Nav>
                <NavMenu>
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
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;