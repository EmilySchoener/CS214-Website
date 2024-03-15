// Filename - pages/unit6.jsx
import React from "react";
import { Link } from 'react-router-dom'

const Unit6 = () => {
    return (
        <div>
            <h1>
                Section 1.1 and 1.2 webpage.
            </h1>
            <Link to="/unit6/section6_1/">
              Section 6.1
            </Link>
            <br />
            <Link to="/unit6/section6_2/">
              Section 6.2
            </Link>
        </div>
    );
};

export default Unit6;