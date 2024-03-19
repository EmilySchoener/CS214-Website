// Filename - pages/unit3.jsx
import React, {useState} from "react";
import { Button, Form } from "react-bootstrap";
import { useForm } from "react-hook-form";
import axios from "axios";

/*
const Unit3 = () => {
    //The Initial state is 1 for the number of cases.
    const getInitialState = () => {
    return "1";
    }
*/
const Unit3 = () => {
    //Variables
    const [cases, setCases] = useState("1");
    const [char, setChar] = useState("");
    const [base1, setBase1] = useState("");
    const [base2, setBase2] = useState("");
    const [base3, setBase3] = useState("");
    const [relation, setRelation] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            e.preventDefault(); //This will stop the handler from emptying the text box.
            alert (`Cases Chosen: ${cases}, Char Chosen: ${char}
                \nBases Chosen: ${base1}\n
                Relation: ${char}(n) = ${relation}`);
            const response = await axios.post("http://127.0.0.1:5000/submit", {
                cases,
                char,
                base1,
                base2,
                base3,
                relation,
            });
            console.log("Response from server:", response.data);
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

    /*
    //When user presses the submit button.
    const handleSubmit = (e) => {
        e.preventDefault(); //This will stop the handler from emptying the text box.
        alert (`Cases Chosen: ${cases}, Char Chosen: ${char}
                \nBases Chosen: ${bases}\n
                Relation: ${char}(n) = ${relation}`);
    }*/

    //What is on the webpage.
    return (
        <div>
            <h1>
                Section 3.1 webpage.
            </h1>
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
                        value={char}
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
        </div>
    );
};

export default Unit3;