// Filename - pages/unit5.jsx
import React from "react";
import { Link } from 'react-router-dom'

const Unit5 = () => {
    return (
        <div>
            <h1>
                Unit 5 webpage. Use this to go to sections in unit 5.
            </h1>
            <Link to="/unit5/section5_1/">
                Section 5.1
            </Link>
            <br/>
            <Link to="/unit5/section5_2/">
                Section 5.2
            </Link>
            <br/>
            <Link to="/unit5/section5_4/">
                Section 5.4
            </Link>
            <br/>
            <Link to="/unit5/section5_5/">
                Section 5.5
            </Link>
            <br/>
            <Link to="/unit5/section5_7/">
                Section 5.7
            </Link>
        </div>
    );
};

export default Unit5;