// Filename - pages/unit1.jsx
import React from "react";
import { Link } from 'react-router-dom'

const Unit1 = () => {
    return (
        <div>
            <h1>
                Section 1.1 and 1.3 webpage.
            </h1>
            <Link to="/unit1/section1_1/">
              Section 1.1
            </Link>
        </div>
    );
};

export default Unit1;