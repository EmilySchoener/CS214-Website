// Filename - pages/unit3.jsx
//import React, {useState} from "react";
import React, { useEffect, useState } from 'react';
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";
import { Splitter, SplitterPanel } from 'primereact/splitter';

/*
const Unit3 = () => {
    //The Initial state is 1 for the number of cases.
    const getInitialState = () => {
    return "1";
    }
*/
const Unit3 = () => {
    let initial = ["2", "S", "1", "2", "", "S(n-1) + S(n-2)"]
    //Variables
    const [cases, setCases] = useState(initial[0]);
    const [char, setChar] = useState(initial[1]);
    const [base1, setBase1] = useState(initial[2]);
    const [base2, setBase2] = useState(initial[3]);
    const [base3, setBase3] = useState(initial[4]);
    const [relation, setRelation] = useState(initial[5]);
    const [responseData, setResponseData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            const response = await axios.post("http://127.0.0.1:5000/3_1", {
                cases,
                char,
                base1,
                base2,
                base3,
                relation,
            });
            console.log("Response from server:", response.data);
            fetchData();
        } catch (error) {
            console.error("Error:", error);
        }
    }

    //For input changes
    const casesChange= (e) => {
        setCases(e.target.value);
    }
    const charChange= (e) => {
        setChar(e.target.value);
    }
    const base1Change= (e) => {
        setBase1(e.target.value);
        initial[2] = e.target.value
    }
    const base2Change= (e) => {
        setBase2(e.target.value);
    }
    const base3Change= (e) => {
        setBase3(e.target.value);
    }
    const relationChange= (e) => {
        setRelation(e.target.value);
    }

    const fetchData = () => {
        // Make an HTTP GET request to your Flask backend
    axios.get("http://localhost:5000/3_1")
      .then(response => {
        // Update the state with the response data
        setResponseData(response.data);
      })
      .catch(error => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
    }

    useEffect(() => fetchData(), []);

    //What is on the webpage.
    return (
        <div>
            <h1>
                Section 3.1 webpage.
            </h1>
            <Splitter>
                <SplitterPanel minsize={50}>
            <form onSubmit={handleSubmit}>
                How many base cases do you have?
                <select id="dropdown" value={cases} onChange={casesChange}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
                <br/>
                <label>What character are you using?
                    <input
                        onChange={charChange}
                        type="text"
                        value={char || ""}
                        placeholder="Enter Here"
                    />
                </label>
                <br/>
                <label>
                    {char}(1)=
                    <input
                        onChange={base1Change}
                        type="text"
                        value={base1}
                        placeholder="Enter Base Case Here"
                    />
                </label>
                <br/>
                <label>
                    {char}(2)=
                    <input
                        onChange={base2Change}
                        type="text"
                        value={base2}
                        placeholder="Enter Base Case Here"
                    />
                </label>
                <br/>
                <label>
                    {char}(3)=
                    <input
                        onChange={base3Change}
                        type="text"
                        value={base3}
                        placeholder="Enter Base Case Here"
                    />
                </label>
                <br/>
                <p>Enter in the recurrence relation: </p>
                <label>
                    {char}(n) =
                    <input
                        onChange={relationChange}
                        type="text"
                        value={relation}
                        placeholder="Enter Relation Here"
                    />
                </label>
                <br/>
                <button
                    type="submit">
                    Submit
                </button>
            </form>

            <h2>Solution</h2>
            <h2>Response from Flask Backend</h2>
            {responseData !== null && Array.isArray(responseData) ? (
                <ul>
                    {responseData.map((item, index) => (
                        <li key={index}>{item}</li>
                    ))}
                </ul>
            ) : (
                <p> ... Loading ...</p>
            )}
                    </SplitterPanel>
                <SplitterPanel minsize={50}>
                    <h2>Example:</h2>
                    <p>
                        2 Base Cases<br/>
                        Character = S<br/>
                        S(1) = 1<br/>
                        S(2) = 2<br/>
                        S(n) = S(n-1) + S(n-2)<br/>
                    </p>
                    <p>
                        Solution:<br/>
                        S(3)=3<br/>
                        S(4)=5<br/>
                        S(5)=8<br/>
                        S(6)=13<br/>
                        S(7)=21<br/>
                    </p>
                </SplitterPanel>
            </Splitter>

        </div>
    );
};




export default Unit3;